# utils/data_loader.py

import pandas as pd
import streamlit as st


@st.cache_data
def load_file(uploaded_file):
    try:

        # CSV Files
        if uploaded_file.name.lower().endswith(".csv"):

            try:
                df = pd.read_csv(
                    uploaded_file,
                    header=0,
                    sep=None,
                    engine="python",
                    encoding="utf-8",
                    on_bad_lines="skip"
                )

            except UnicodeDecodeError:

                uploaded_file.seek(0)

                df = pd.read_csv(
                    uploaded_file,
                    header=0,
                    sep=None,
                    engine="python",
                    encoding="latin1",
                    on_bad_lines="skip"
                )

        # Excel Files
        elif uploaded_file.name.lower().endswith(".xlsx"):

            df = pd.read_excel(
                uploaded_file,
                header=0
            )

        else:

            raise ValueError(
                "Unsupported file format. Please upload a CSV or XLSX file."
            )

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Clean column names
        df.columns = (
            df.columns
            .astype(str)
            .str.strip()
            .str.replace("\n", " ", regex=False)
            .str.replace("\r", " ", regex=False)
            .str.replace(" ", "_", regex=False)
            .str.lower()
        )

        # Check if dataset is empty
        if df.empty:
            raise ValueError(
                "The uploaded file contains no valid data."
            )

        return df

    except Exception as e:

        raise Exception(
            f"Error loading file: {str(e)}"
        )
