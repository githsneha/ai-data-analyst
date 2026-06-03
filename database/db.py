# database/db.py

import sqlite3
import pandas as pd

DB_NAME = "database.db"


def save_dataframe(
    df,
    table_name="uploaded_data"
):

    conn = None

    try:

        conn = sqlite3.connect(
            DB_NAME
        )

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        conn.commit()

    except Exception as e:

        raise Exception(
            f"Error saving dataframe: {e}"
        )

    finally:

        if conn:
            conn.close()


def run_query(query):

    conn = None

    try:

        conn = sqlite3.connect(
            DB_NAME
        )

        result = pd.read_sql_query(
            query,
            conn
        )

        return result

    except Exception as e:

        raise Exception(
            f"SQL Execution Error: {e}"
        )

    finally:

        if conn:
            conn.close()