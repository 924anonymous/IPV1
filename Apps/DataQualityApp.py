import streamlit as st
import GetData
import Utility
import json
import os
import pandas as pd


def dataquality_app():
    pd.set_option('display.max_colwidth', None)
    st.markdown("<h1 style='text-align: center;'>Data Quality</h1>", unsafe_allow_html=True)
    st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)
    try:
        postgres_obj = GetData.GetDataFromPostgres(**st.secrets['postgres'])
        log_df = postgres_obj.execute_query('select * from config.error_table')
    except Exception as e:
        st.error(e)
    else:
        try:
            fdf = pd.DataFrame()

            fdf['created_at'] = log_df.apply(lambda x: json.loads(x['errorneous_records'])['created_at'], axis=1)
            fdf['updated_at'] = postgres_obj.execute_query("select current_timestamp::timestamp;").iloc[0][
                'current_timestamp']

            log_df["errorneous_records"] = log_df.apply(
                lambda row: Utility.key_operations(row["errorneous_records"], 'delete', '', ''), axis=1)

            hide_table_row_index = """
                                    <style>
                                    thead tr th:first-child {display:none}
                                    tbody th {display:none}
                                    </style>
                                    """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            all_rules_dict = {'All Rules': ['Null Check', 'Length Check', 'Boolean Check']}
            all_rules_df = pd.DataFrame(all_rules_dict)
            df_applied_rule = log_df.filter(items=['column_name', 'check_name']).drop_duplicates()
            df_applied_rule['fix_value'] = ''

            with st.container():
                left_col, right_col = st.columns(2)
                with left_col:
                    st.table(all_rules_df)
                with right_col:
                    with st.form("form_fix"):
                        le_col, mid_col, ri_col = st.columns(3)
                        for ind in df_applied_rule.index:
                            with le_col:
                                col_nm = st.text_input('Column Name', value=df_applied_rule['column_name'][ind])
                            with mid_col:
                                chk_nm = st.text_input('Check Name', value=df_applied_rule['check_name'][ind])
                            with ri_col:
                                f_val = st.text_input('Fix Value', value='', key=ind)
                        submitted = st.form_submit_button("Submit")
                        if submitted:
                            for _ in range(len(df_applied_rule)):
                                log_df["errorneous_records"] = log_df.apply(
                                    lambda row: Utility.key_operations(row["errorneous_records"], 'add', col_nm, f_val),
                                    axis=1)

                            fdf['errorneous_records'] = log_df['errorneous_records']
                            fdf.to_parquet('rep.parquet', engine='auto', compression='snappy')
                            with open("rep.parquet", "rb") as file:
                                btn = st.download_button(
                                    label="Download Parquet File",
                                    data=file,
                                    file_name="rep.parquet"
                                )
                            if btn:
                                try:
                                    os.remove('./rep.parquet')
                                except OSError as error:
                                    pass
        except Exception as e:
            st.error(e)
