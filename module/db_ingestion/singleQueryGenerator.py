import module.db_ingestion.insert_queries as queries
from module.common_functions import insertData
import streamlit as st
from module.common_functions import getData


def singleQueryGenerator(option):
    if option.lower() == 'db_ingestion_config_details':

        # DATABASE_NAME,SCHEMA_NAME,TABLE_NAME,COLUMNS_TO_SELECT,SRC_PATH,RAW_BUCKET_NAME,
        # RAW_TGT_PATH,CURATED_BUCKET_NAME,CURATED_TGT_PATH,MODE,LIMITDATACHECK,INCR_COLUMN_NAME,
        # LIMITDATACONSTRAINT,INCREMENTAL_COND_CHECK
        # ,COLUMNS_TO_SELECT_CHECK,INCR_COLUMN_TIMESTAMP_FORMAT,INCR_COLUMN_TIMESTAMP_COND_CHECK

        with st.form('single_table_form'):

            query = 'select distinct database_type from config.db_conn_details;'
            data = getData(query)
            db_type = [dbs[0] for dbs in data]

            database_type = st.selectbox('Select Database Type', db_type)

            col1, col2 = st.columns(2)
            col3, col4 = st.columns(2)

            with col1:
                db_name = st.text_input('Source Database Name', key=1)
                table_name = st.text_input('Source Table Name', key=3)
                columns_to_select_check = st.selectbox('Columns To Select Check', ('No', 'Yes'))
                limitDataCheck = st.selectbox('Data Check Limit', ('No', 'Yes'))
                incremental_cond_check = st.selectbox('Incremental Condition Check', ('No', 'Yes'))

                st.divider()

            with col2:
                schema_name = st.text_input('Source Schema Name', key=2)
                st.text_input('')
                columns_to_select = st.text_input('Columns To Select', key=4)
                limitDataConstraint = st.text_input('Set Limit Data Constraints', key=13)
                incr_column_name = st.text_input('Incremental Column Name', key=12)

                st.divider()

            with col3:
                mode = st.selectbox('Write Mode', ('Select Mode..', 'Overwrite', 'Append'))
                if mode.lower() == 'select mode..':
                    mode = ''
                src_bucket_name = st.text_input('S3 Source Bucket Name', key=21)
                raw_bucket_name = st.text_input('S3 Raw Bucket Name', key=6)
                curated_bucket_name = st.text_input('S3 Curated Bucket Name', key=8)

            with col4:
                st.text_input('', key=20)
                src_path = st.text_input('S3 Source Folder Path', key=5)
                raw_tgt_path = st.text_input('S3 Raw Folder Path', key=7)
                curated_tgt_path = st.text_input('S3 Curated Folder Path', key=9)

                incr_column_timestamp_cond_check = 'no'  # st.selectbox('Incremental Column Timestamp Condition Check',('No','Yes'))
                if incr_column_timestamp_cond_check.lower() == 'yes':
                    incr_column_timestamp_format = st.text_input('Incremental Column Timestamp Format', key=16)
                else:
                    incr_column_timestamp_format = ''

            query = f"select distinct id from config.db_conn_details where database_name ='{db_name}' and database_type = '{database_type}';"
            connection_id = None
            if db_name != '' and db_name is not None:
                data = getData(query)
                connection_id = data[0][0]

            update_query_db_ing = queries.update_dbingestion_config_details.format(database_name=db_name,
                                                                                   schema_name=schema_name,
                                                                                   table_name=table_name)

            query = queries.db_ingestion_config_details_query.format(db_name=db_name, schema_name=schema_name,
                                                                     table_name=table_name,
                                                                     columns_to_select=columns_to_select,
                                                                     src_path=src_path,
                                                                     raw_bucket_name=raw_bucket_name,
                                                                     raw_tgt_path=raw_tgt_path,
                                                                     curated_bucket_name=curated_bucket_name,
                                                                     curated_tgt_path=curated_tgt_path,
                                                                     mode=mode.lower(),
                                                                     limitDataCheck=limitDataCheck.lower(),
                                                                     incr_column_name=incr_column_name,
                                                                     limitDataConstraint=limitDataConstraint,
                                                                     incremental_cond_check=incremental_cond_check.lower(),
                                                                     columns_to_select_check=columns_to_select_check.lower(),
                                                                     incr_column_timestamp_format=incr_column_timestamp_format,
                                                                     incr_column_timestamp_cond_check=incr_column_timestamp_cond_check.lower(),
                                                                     connection_id=connection_id)
            submitted = st.form_submit_button("Insert Data Into DB", type='primary')
            if submitted:
                insertData(update_query_db_ing)
                insertData(query)
                st.success('Data Inserted Into DB Successfully')

    elif option.lower() == "incremental_config_details":
        with st.form("inc_dtl"):
            left_col, right_col = st.columns(2)
            with left_col:
                db_name = st.text_input('Source Database Name')
                table_name = st.text_input('Source Table Name')
                column_name = st.text_input('Column Name')
            with right_col:
                schema_name = st.text_input('Source Schema Name')
                operator = st.text_input('Operator ("<" or ">" or "=")')
                value = st.text_input('Column Value')

            update_query_inc_dtl = queries.update_incremental_details.format(database_name=db_name,
                                                                             schema_name=schema_name,
                                                                             table_name=table_name)

            inc_query = queries.incremental_config_details_query.format(db_name=db_name,
                                                                        schema_name=schema_name,
                                                                        table_name=table_name,
                                                                        value=value,
                                                                        column_name=column_name,
                                                                        operator=operator)

            submitted = st.form_submit_button("Insert Data Into DB", type='primary')
            if submitted:
                insertData(update_query_inc_dtl)
                insertData(inc_query)
                st.success('Data Inserted Into DB Successfully')
