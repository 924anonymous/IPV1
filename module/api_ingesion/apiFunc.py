import streamlit as st
import module.api_ingesion.insert_queries as queries
from module.common_functions import insertData


def shopifyTable():
    with st.form('shopify_form'):
        col1, col2 = st.columns(2)

        with col1:
            url = st.text_input('Url')
            params = st.text_input('Parameters')
            headers = st.text_input('Headers')

        with col2:
            timeout = st.text_input('Timeout')
            auth_user = st.text_input('Authenticated User')
            auth_password = st.text_input('Authenticated Password')

        submitted = st.form_submit_button("Insert Data Into DB", type='primary')


def netsuitTable():
    with st.form('netsuit_form'):
        col1, col2 = st.columns(2)

        with col1:
            server_host = st.text_input('Host')
            port = st.text_input('Port')
            user = st.text_input('User')
            password = st.text_input('Password')

        with col2:
            account_id = st.text_input('Account Id')
            role_id = st.text_input('Role Id')
            table_name = st.text_input('Table Name')
            query = st.text_input('Query')

        submitted = st.form_submit_button("Insert Data Into DB", type='primary')


def restApiTable():
    with st.form('rest_api_form'):
        col1, col2 = st.columns(2)

        with col1:
            url = st.text_input('Url')
            auth_type = st.selectbox(
                'Authentication Type',
                ('Select Auth Type', 'BasicAuth', 'Api Key', 'Jwt Token', 'Bearer Token'))
            params = st.text_input('Params')
            api_key = st.text_input('Api Key')
            bearer_token = st.text_input('Bearer Token')

        with col2:
            timeout = st.text_input('Timeout')
            headers = st.text_input('Headers')
            auth_user = st.text_input('Auth User')
            auth_password = st.text_input('Auth Password')
            jwt_token = st.text_input('Jwt Token')

        submitted = st.form_submit_button("Insert Data Into DB", type='primary')
