# ai/sql_generator.py

from ai.gemini_client import ask_gemini


def generate_sql(question, schema):

    prompt = f"""
You are an expert SQLite analyst.

Database Type:
SQLite

Table Name:
uploaded_data

Schema:
{schema}

Important Rules:

1. Return ONLY valid SQLite SQL.
2. Use ONLY the table name uploaded_data.
3. Use ONLY columns present in the schema.
4. Never explain the query.
5. Never use markdown.
6. Never write ```sql.
7. Return exactly ONE SQL query.

Query Generation Guidelines:

- If user asks for top categories, best categories, category analysis:
  use GROUP BY on the most relevant categorical column.

- If user asks for top products, best products, most sold items:
  use GROUP BY and SUM().

- If user asks for average:
  use AVG().

- If user asks for total:
  use SUM().

- If user asks for count:
  use COUNT().

- If user asks for trend over time:
  use date columns and ORDER BY date.

- Always provide meaningful aliases:
  Example:
  SUM(Quantity) AS TotalQuantity

- Limit large result sets to 10 rows unless user specifies otherwise.

Examples:

Question:
Show top products

SQL:
SELECT
    Description,
    SUM(Quantity) AS TotalQuantity
FROM uploaded_data
GROUP BY Description
ORDER BY TotalQuantity DESC
LIMIT 10;

Question:
Show sales by country

SQL:
SELECT
    Country,
    SUM(Quantity) AS TotalQuantity
FROM uploaded_data
GROUP BY Country
ORDER BY TotalQuantity DESC;

User Question:
{question}
"""

    sql = ask_gemini(prompt)

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.replace("SQL", "")

    return sql.strip()