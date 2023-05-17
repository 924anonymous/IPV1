import streamlit as st
import psycopg2


def runInsertQuery(conn, query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
            cur.close()
    except Exception as e:
        conn.rollback()
        cur.close()
        raise Exception(e)


def runSelectQuery(conn, query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            row = cur.fetchall()
            cur.close()
            return row
    except Exception as e:
        if conn:
            cur.close()
        raise Exception(e)


def init_connection():
    return psycopg2.connect(**st.secrets["postgres_ni"])


def postgresdb():
    # establishing the connection
    conn = init_connection()

    return conn
