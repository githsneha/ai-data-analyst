# utils/schema_detector.py

def get_schema(df):

    schema_lines = []

    for column in df.columns:

        dtype = str(df[column].dtype)

        schema_lines.append(
            f"{column}: {dtype}"
        )

    return "\n".join(schema_lines)