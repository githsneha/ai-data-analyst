# ai/dataset_explainer.py

def explain_dataset(df):

    num_rows = df.shape[0]
    num_cols = df.shape[1]

    columns = list(df.columns)

    missing_values = int(df.isnull().sum().sum())

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        exclude=["int64", "float64"]
    ).columns.tolist()

    explanation = f"""
### Dataset Overview

- Total Rows: {num_rows:,}
- Total Columns: {num_cols}
- Missing Values: {missing_values}

### Columns

{', '.join(columns)}

### Numeric Columns

{', '.join(numeric_cols) if numeric_cols else 'None'}

### Categorical Columns

{', '.join(categorical_cols) if categorical_cols else 'None'}

### Possible Analyses

- Summary statistics
- Trend analysis
- Category comparison
- Aggregation and grouping
- Top performing categories/products
- Distribution analysis

### Business Use Cases

- KPI Monitoring
- Sales Analysis
- Customer Analysis
- Product Performance Analysis
- Operational Reporting
"""

    return explanation