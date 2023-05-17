import streamlit as st
from streamlit_option_menu import option_menu
from module.api_ingesion.apiFunc import *


def apiIngestion():
    st.title('API INGESTION SETUP')

    selected = option_menu(None, ["Shopify", 'Netsuite', 'REST API'],
                           icons=None, default_index=0, orientation="horizontal")

    if selected.lower() == 'shopify':
        query = shopifyTable()

    elif selected.lower() == 'netsuite':
        query = netsuitTable()
    elif selected.lower() == 'rest api':
        query = restApiTable()
