import streamlit as st
import GetData
import pandas as pd
import plotly.express as px
import Utility


def operations_app():
    st.markdown("<h1 style='text-align: center;'>Data Operations Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)
    try:
        postgres_obj = GetData.GetDataFromPostgres(**st.secrets['postgres'])
        df = postgres_obj.fetch_df()
        log_df = postgres_obj.execute_query(Utility.log_query)
    except Exception as e:
        st.error(e)
    else:
        try:
            if len(df) > 0:
                count_of_null_records = df['mining_data_Indicator Unit'].isnull().sum()
                count_of_clean_records = len(df) - count_of_null_records

                dict_for_null_clean_records_df = {'Label': ["Erroneous Records", 'Clean Records'],
                                                  'Record Count': [count_of_null_records, count_of_clean_records]}

                df_for_null_clean_pie_chart = pd.DataFrame(dict_for_null_clean_records_df)

                fig_pie_null_clean_records = px.pie(df_for_null_clean_pie_chart, values="Record Count",
                                                    names="Label",
                                                    title="Record Statistics",
                                                    color_discrete_sequence=px.colors.sequential.RdBu
                                                    )
                fig_pie_null_clean_records.update_traces(marker=dict(colors=['red', 'green']))

                fig_pie_null_clean_records.update_layout(Utility.layout)

                fig_bar_src_cu_fil_rec_count = px.bar(log_df,
                                                      y=log_df['record_count'],
                                                      x=log_df['data_layer'],
                                                      title='Data Flow',
                                                      labels={'record_count': 'Record Count',
                                                              'data_layer': 'Data Layer'})

                fig_bar_src_cu_fil_rec_count.update_layout(Utility.layout)
                fig_bar_src_cu_fil_rec_count.update_traces(marker_color='#3a92f0')
                fig_bar_src_cu_fil_rec_count.update_xaxes(showgrid=False)
                fig_bar_src_cu_fil_rec_count.update_yaxes(showgrid=False)

                left_col, right_col = st.columns(2)
                with left_col:
                    st.plotly_chart(fig_pie_null_clean_records, use_container_width=True)
                with right_col:
                    st.plotly_chart(fig_bar_src_cu_fil_rec_count, use_container_width=True)
            else:
                st.error('Statistics Data Not Available At Source Location, No Dashboards To Display 🧐')
        except Exception as e:
            st.error(e)
