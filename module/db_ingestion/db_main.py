import streamlit as st
from streamlit_option_menu import option_menu
from module.db_ingestion.single_table import singleTable
from module.db_ingestion.multi_table import multiTable


def dbIngestion():
    st.title('INGESTION CONFIGURATION SETUP')

    selected = option_menu(None, ["Multi Table", 'Single Table'],
                           icons=None, default_index=0, orientation="horizontal")

    if selected.lower() == 'single table':
        singleTable()

    elif selected.lower() == 'multi table':
        multiTable()
