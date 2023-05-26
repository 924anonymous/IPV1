import streamlit as st


def insertData(query):
    # db = st.selectbox('Choose database',('Select databse..','Postgres','MySQL','Oracle'))
    db = 'postgres'
    if db.lower() == 'postgres':
        from module.dbConnection import postgresdb
        conn = postgresdb()
    if conn:
        try:
            print('Connection Estabished')
            from module.dbConnection import runInsertQuery
            # Executing an query using the execute() method
            runInsertQuery(conn, query)
        except Exception as e:
            print(f'Error : {e}')
        # Closing the connection
        conn.close()


def getData(query):
    # db = st.selectbox('Choose database',('Select databse..','Postgres','MySQL','Oracle'))
    db = 'postgres'
    if db.lower() == 'postgres':
        from module.dbConnection import postgresdb
        conn = postgresdb()
    if conn:
        try:
            print('Connection Estabished')
            from module.dbConnection import runSelectQuery
            # Executing an query using the execute() method
            rows = runSelectQuery(conn, query)
            return rows
        except Exception as e:
            print(f'Error : {e}')
        # Closing the connection
        conn.close()
