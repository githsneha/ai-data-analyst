import streamlit as st

from utils.data_loader import load_file
from utils.schema_detector import get_schema

from database.db import (
    save_dataframe,
    run_query
)

from ai.sql_generator import generate_sql
from ai.insight_generator import generate_insight
from ai.question_classifier import classify_question
from ai.dataset_explainer import explain_dataset

from visualization.charts import create_chart


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Data Analyst",
    layout="wide"
)

st.title("AI Data Analyst")

st.caption(
    "Upload any CSV/Excel file and analyze it using AI"
)


# =====================================
# SESSION STATE
# =====================================

if "question_history" not in st.session_state:
    st.session_state.question_history = []

if "dataset_loaded" not in st.session_state:
    st.session_state.dataset_loaded = False


# =====================================
# FILE UPLOAD
# =====================================

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    try:

        # =====================================
        # LOAD DATA
        # =====================================

        df = load_file(uploaded_file)

        if not st.session_state.dataset_loaded:

            save_dataframe(df)

            st.session_state.dataset_loaded = True

        schema = get_schema(df)

        # =====================================
        # DATASET OVERVIEW
        # =====================================

        st.success(" Dataset Loaded Successfully")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Rows",
            f"{df.shape[0]:,}"
        )

        col2.metric(
            "Columns",
            df.shape[1]
        )

        col3.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # =====================================
        # SCHEMA
        # =====================================

        with st.expander(
            "Detected Dataset Schema"
        ):

            st.code(schema)

        # =====================================
        # SUGGESTED QUESTIONS
        # =====================================

        st.subheader(
            "Suggested Questions"
        )

        st.markdown("""
- What is this dataset about?
- Describe the columns
- Show top 10 products by quantity sold
- Show quantity sold by country
- Show average unit price by country
- Show top categories
- Which category performs best?
""")

        st.divider()

        # =====================================
        # QUESTION INPUT
        # =====================================

        question = st.text_input(
            "Ask a question about your data",
            placeholder="Example: Show total sales by country",
            key="main_question"
        )

        # =====================================
        # STORE HISTORY
        # =====================================

        if question and question not in st.session_state.question_history:

            st.session_state.question_history.append(
                question
            )

        # =====================================
        # SIDEBAR HISTORY
        # =====================================

        with st.sidebar:

            st.header("Question History")

            if len(st.session_state.question_history) == 0:

                st.info(
                    "No questions asked yet"
                )

            else:

                for q in reversed(
                    st.session_state.question_history
                ):

                    st.write(
                        "•",
                        q
                    )

        # =====================================
        # PROCESS QUESTION
        # =====================================

        if question:

            query_type = classify_question(
                question
            )

            # =====================================
            # DATASET MODE
            # =====================================

            if query_type == "dataset":

                explanation = explain_dataset(
                    df
                )

                st.subheader(
                    "Dataset Understanding"
                )

                st.markdown(
                    explanation
                )

            # =====================================
            # ANALYSIS MODE
            # =====================================

            else:

                with st.spinner(
                    "Generating SQL..."
                ):

                    sql = generate_sql(
                        question,
                        schema
                    )

                st.subheader(
                    "Generated SQL"
                )

                st.code(
                    sql,
                    language="sql"
                )

                try:

                    result = run_query(
                        sql
                    )

                    st.subheader(
                        "Results"
                    )

                    st.dataframe(
                        result,
                        use_container_width=True
                    )

                    # =====================================
                    # DOWNLOAD
                    # =====================================

                    csv = result.to_csv(
                        index=False
                    )

                    st.download_button(
                        label="⬇ Download Results",
                        data=csv,
                        file_name="results.csv",
                        mime="text/csv"
                    )

                    # =====================================
                    # CHART
                    # =====================================

                    chart = create_chart(
                        result
                    )

                    if chart:

                        st.subheader(
                            "Visualization"
                        )

                        st.plotly_chart(
                            chart,
                            use_container_width=True
                        )

                    # =====================================
                    # INSIGHTS BUTTON
                    # =====================================

                    if not result.empty:

                        if st.button(
                            "Generate AI Insights"
                        ):

                            with st.spinner(
                                "Generating AI Insights..."
                            ):

                                insights = generate_insight(
                                    result
                                )

                            st.subheader(
                                "AI Insights"
                            )

                            st.write(
                                insights
                            )

                    else:

                        st.warning(
                            "Query executed successfully but returned no data."
                        )

                except Exception as e:

                    st.error(
                        f"Query Failed: {e}"
                    )

    except Exception as e:

        st.error(
            f"Dataset Processing Failed: {e}"
        )