from sqlalchemy import create_engine
import pandas as pd


class GetDataFromPostgres:
    def __init__(self, url, dbtable, user, password, database, port):
        self.url = url
        self.dbtable = dbtable
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.engine = create_engine(
            f"postgresql://{self.user}:{self.password}@{self.url}:{self.port}/{self.database}")

    def fetch_df(self):
        """
        This Function Can Fetch Data From Postgres And Return Pandas DataFrame Of That Data.

        :return: Pandas DataFrame
        """
        df = pd.read_sql(f"SELECT * FROM {self.dbtable}", self.engine)

        return df

    def execute_query(self, query):
        """
        This Function Executes The Given Query On Postgres.

        :param query: Query To Execute On Snowflake
        :return: Pandas DataFrame
        """
        df = pd.read_sql(query, self.engine)

        return df
