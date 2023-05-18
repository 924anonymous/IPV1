import streamlit as st
import GetData
import plotly.express as px
import Utility


def dashboard_app():
    st.markdown("<h1 style='text-align: center;'>Mining Production Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)
    try:
        postgres_obj = GetData.GetDataFromPostgres(**st.secrets['postgres'])
        df = postgres_obj.fetch_df()
    except Exception as e:
        st.error(e)
    else:
        try:
            if len(df) > 0:
                copper_df = df[['mining_data_Date', 'mining_data_Value', 'mining_data_Indicator Unit']][
                    (df['mining_data_Location Name'] == 'India') & (
                            df['mining_data_Indicator Name'] == 'Production of copper, refined') & (
                            df['mining_data_Date'] > '2010-12-31')].sort_values(by=["mining_data_Date"], ascending=True)

                fig_bar_copper_mine = px.bar(copper_df, y=copper_df['mining_data_Value'],
                                             x=copper_df['mining_data_Date'],
                                             title='Production of copper, Refined',
                                             labels={'mining_data_Value': 'Production Value (tonnes (metric))', 'mining_data_Date': 'Date'})
                fig_line_copper_mine = px.line(copper_df, y=copper_df["mining_data_Value"],
                                               x=copper_df["mining_data_Date"],
                                               title='Production of copper, Refined',
                                               labels={'mining_data_Value': 'Production Value (tonnes (metric))', 'mining_data_Date': 'Date'},
                                               markers=True)

                zinc_df = df[['mining_data_Date', 'mining_data_Value', 'mining_data_Indicator Unit']][
                    (df['mining_data_Location Name'] == 'India') & (
                            df['mining_data_Indicator Name'] == 'Production of zinc, mine') & (
                            df['mining_data_Date'] > '2010-12-31')].sort_values(by=["mining_data_Date"], ascending=True)

                fig_bar_zinc_mine = px.bar(zinc_df, y=zinc_df['mining_data_Value'], x=zinc_df['mining_data_Date'],
                                           title='Production of zinc, mine',
                                           labels={'mining_data_Value': 'Production Value (tonnes (metal content))', 'mining_data_Date': 'Date'})
                fig_line_zinc_mine = px.line(zinc_df, y=zinc_df["mining_data_Value"], x=zinc_df["mining_data_Date"],
                                             title='Production of zinc, mine',
                                             labels={'mining_data_Value': 'Production Value (tonnes (metal content))', 'mining_data_Date': 'Date'},
                                             markers=True)

                fig_bar_zinc_mine.update_layout(Utility.layout)
                fig_bar_copper_mine.update_traces(marker_color='#3a92f0')
                fig_bar_copper_mine.update_xaxes(showgrid=False)
                fig_bar_copper_mine.update_yaxes(showgrid=False)

                fig_bar_copper_mine.update_layout(Utility.layout)
                fig_bar_zinc_mine.update_traces(marker_color='#3a92f0')
                fig_bar_zinc_mine.update_xaxes(showgrid=False)
                fig_bar_zinc_mine.update_yaxes(showgrid=False)

                fig_line_copper_mine.update_traces(line_color='#92fa23')
                fig_line_copper_mine.update_layout(Utility.layout)

                fig_line_zinc_mine.update_traces(line_color='#92fa23')
                fig_line_zinc_mine.update_layout(Utility.layout)

                left_col, right_col = st.columns(2)
                with left_col:
                    st.plotly_chart(fig_bar_copper_mine, use_container_width=True)
                    st.plotly_chart(fig_bar_zinc_mine, use_container_width=True)
                with right_col:
                    st.plotly_chart(fig_line_copper_mine, use_container_width=True)
                    st.plotly_chart(fig_line_zinc_mine, use_container_width=True)
            else:
                st.error('Data Not Available At Source Location, No Dashboards To Display 🧐')
        except Exception as e:
            st.error(e)
