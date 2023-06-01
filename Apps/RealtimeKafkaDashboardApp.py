import streamlit as st
import snowflake.connector
import plotly.graph_objects as go
import plotly.express as px
from streamlit_autorefresh import st_autorefresh


def realtime_kafka_dashboard_app():
    st.markdown("<h1 style='text-align: center;'>RealTime Sales Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

    st_autorefresh(interval=1 * 60 * 1000, key="datarefresh")

    try:
        @st.cache_resource
        def init_connection():
            return snowflake.connector.connect(**st.secrets["snowflake"])

        conn = init_connection()
        cur = conn.cursor()

        def get_df(query):
            cur.execute(query)
            df = cur.fetch_pandas_all()
            return df

        main_df = get_df("SELECT * FROM KAFKA.KAFKA_SCHEMA.SALES")
    except Exception as e:
        st.error(e)
    else:
        try:
            if len(main_df) > 0:
                total_sales = int(main_df["TOTAL"].sum())
                average_rating = round(main_df["RATING"].mean(), 1)
                star_rating = ":star:" * int(round(average_rating, 0))
                average_sale_by_transaction = round(main_df["TOTAL"].mean(), 2)

                left_column, middle_column, right_column = st.columns(3)
                with left_column:
                    st.subheader("Total Sales:")
                    st.subheader(f"US $ {total_sales:,}")
                with middle_column:
                    st.subheader("Average Rating:")
                    st.subheader(f"{average_rating} {star_rating}")
                with right_column:
                    st.subheader("Average Sales Per Transaction:")
                    st.subheader(f"US $ {average_sale_by_transaction}")

                st.markdown("""---""")

                sales_by_product_line = (
                    main_df.groupby(by=["PRODUCT_LINE"]).sum()[["TOTAL"]].sort_values(by="TOTAL")
                )

                fig_product_sales = px.bar(
                    sales_by_product_line,
                    x=sales_by_product_line.index,
                    y='TOTAL',
                    orientation="v",
                    title="<b>Sales by Product Line</b>",
                    color_discrete_sequence=["#346ae0"],
                    template="plotly_white",
                )
                fig_product_sales.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False))
                )
                left_column, right_column = st.columns(2)
                left_column.plotly_chart(fig_product_sales, use_container_width=True)

                fig_line_chart_product_sales = px.line(sales_by_product_line, x="TOTAL", y=sales_by_product_line.index,
                                                       title='<b>Sales by Product Lines<b>',
                                                       color_discrete_sequence=["#e81e3c"])

                fig_line_chart_product_sales.update_layout(
                    plot_bgcolor="rgba(0,0,0,0)",
                    xaxis=(dict(showgrid=False)),
                    yaxis=dict(showgrid=False)
                )

                fig_line_chart_product_sales.update_traces(
                    go.Scatter(mode='lines+markers', line=dict(color="#32f224", width=2)))

                right_column.plotly_chart(fig_line_chart_product_sales, use_container_width=True)
            else:
                st.error("Data Not Available At Source Location, No Dashboards To Display 🧐")
        except Exception as e:
            st.error(e)
