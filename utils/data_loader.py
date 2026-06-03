# utils/data_loader.py

import pandas as pd
import streamlit as st


@st.cache_data
def load_file(uploaded_file):

    try:

        if uploaded_file.name.lower().endswith(".csv"):

            df = pd.read_csv(
                uploaded_file,
                header=0,
                encoding="latin1"
            )

        elif uploaded_file.name.lower().endswith(".xlsx"):

            df = pd.read_excel(
                uploaded_file,
                header=0
            )

        else:

            raise ValueError(
                "Unsupported file format. Please upload CSV or XLSX."
            )

        # Remove duplicate rows
        df = df.drop_duplicates()
        

        # Clean column names
        df.columns = (
            df.columns
            .astype(str)
            .str.strip()
            .str.replace("\n", " ", regex=False)
            .str.replace("\r", " ", regex=False)
        )

        return df

    except Exception as e:

        raise Exception(
            f"Error loading file: {e}"
        )