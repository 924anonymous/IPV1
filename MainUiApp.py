import streamlit as st
from streamlit_option_menu import option_menu
from Apps import DashboardApp, UtilityApp, OperationsApp, DataQualityApp

st.set_page_config(
    page_title="MultiUtility Application",
    page_icon="⚙",
    layout="wide"
)

with st.sidebar:
    selected_option = option_menu(
        "App Gallery",
        ["Dashboard", "Accelerator", "Operations", "Data Quality"],
        icons=["graph-up-arrow", "person-badge", "gear", "check-circle"],
        styles={
            "container": {"padding": "5!important", "background-color": "#1b0c24"},
            "icon": {"color": "#e9f229", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#6e797a"},
            "nav-link-selected": {"background-color": "fab055"},
        }
    )

if selected_option == 'Accelerator':
    UtilityApp.utility_app()
if selected_option == 'Dashboard':
    DashboardApp.dashboard_app()
if selected_option == "Operations":
    OperationsApp.operations_app()
if selected_option == "Data Quality":
    DataQualityApp.dataquality_app()
