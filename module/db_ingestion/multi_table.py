import streamlit as st
from module.db_ingestion.multiQueryGenerator import multiQueryGenerator


def multiTable():
    # """
    # Purpose : for creating multiple insert queries
    # input : taking user input
    # output : sql file having multiple insert queries
    # """

    # drop down list :  'sfload_config_details', 'sf_load_stg_config_details','sf_load_curated_config','incremental_config_details','dbingestion_block_driver_details','sf_load_block_driver_details','incremental_tables_list'

    option_dic = {
        'DB Ingestion Configuration Details': 'db_ingestion_config_details',
        'DB Incremental Configuration Details': 'incremental_config_details',
        'DB Ingestion Block Driver Details': 'dbingestion_block_driver_details'
    }

    multi_option = st.selectbox(
        'Select Configuration Process Name : ',
        ('Select Process Type..', 'DB Ingestion Configuration Details', 'DB Incremental Configuration Details',
         'DB Ingestion Block Driver Details'))

    if multi_option.lower() == 'select process type..':
        st.write('Please Select Process Type..')
    else:
        path = st.text_input('Select File Path : ')

        if path:
            st.write('Config Generation Starts..')
            try:
                text_output = multiQueryGenerator(option_dic[multi_option], path)
                st.write('Config Generated Successfully..')
                st.write('Download File From Below : ')
                st.download_button('Download Text File ', text_output)
            except Exception as e:
                st.write(f'Error : {e}')
