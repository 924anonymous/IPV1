# importing libraries
import streamlit as st
from streamlit_option_menu import option_menu
from module.db_ingestion.db_main import dbIngestion
from module.api_ingesion.api_main import apiIngestion


# """
# Purpose : main function for calling all module
# input : process name and path of the csv file
# output : sql file having multiple sql queries
# """

def utility_app():
    st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

    with st.sidebar:
        selected = option_menu("Services", ["DB Ingestion", 'API Ingestion'],
                               icons=[], menu_icon="filter-left", default_index=0)

    if selected.lower() == 'db ingestion':
        dbIngestion()

    if selected.lower() == 'api ingestion':
        apiIngestion()
