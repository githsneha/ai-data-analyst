# visualization/charts.py

import pandas as pd
import plotly.express as px


def create_chart(df):

    try:

        if df.empty:
            return None

        if len(df.columns) < 2:
            return None

        # Detect numeric columns
        numeric_cols = df.select_dtypes(
            include="number"
        ).columns.tolist()

        # Detect non-numeric columns
        categorical_cols = df.select_dtypes(
            exclude="number"
        ).columns.tolist()

        if len(numeric_cols) == 0:
            return None

        # =================================
        # DATE TREND
        # =================================

        for col in df.columns:

            if "date" in col.lower():

                fig = px.line(
                    df,
                    x=col,
                    y=numeric_cols[0],
                    markers=True,
                    title=f"{numeric_cols[0]} Over Time"
                )

                return fig

        # =================================
        # PIE CHART
        # =================================

        if (
            len(categorical_cols) > 0
            and len(df) <= 6
        ):

            fig = px.pie(
                df,
                names=categorical_cols[0],
                values=numeric_cols[0],
                title="Distribution"
            )

            return fig

        # =================================
        # BAR CHART
        # =================================

        if len(categorical_cols) > 0:

            x_col = categorical_cols[0]
            y_col = numeric_cols[0]

            chart_df = df.sort_values(
                by=y_col,
                ascending=False
            )

            fig = px.bar(
                chart_df,
                x=x_col,
                y=y_col,
                title=f"{y_col} by {x_col}"
            )

            return fig

        # =================================
        # SCATTER PLOT
        # =================================

        if len(numeric_cols) >= 2:

            fig = px.scatter(
                df,
                x=numeric_cols[0],
                y=numeric_cols[1],
                title=f"{numeric_cols[1]} vs {numeric_cols[0]}"
            )

            return fig

        # =================================
        # HISTOGRAM
        # =================================

        fig = px.histogram(
            df,
            x=numeric_cols[0],
            title=f"Distribution of {numeric_cols[0]}"
        )

        return fig

    except Exception as e:

        print(
            f"Chart Error: {e}"
        )

        return None