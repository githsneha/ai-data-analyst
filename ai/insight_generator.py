# ai/insight_generator.py

from ai.gemini_client import ask_gemini


def generate_insight(df):

    prompt = f"""
You are a senior business analyst.

Analyze the following query result:

{df.head(20).to_string()}

Generate exactly 3 insights.

Rules:
- Use bullet points.
- Maximum 15 words per insight.
- Focus on business value.
- No introduction.
- No conclusion.
- No headings.
- No paragraphs.
- Be specific and concise.

Example Output:

• Product A contributes the highest sales volume.
• Sales are concentrated in a few categories.
• Top products account for most revenue.
"""

    return ask_gemini(prompt)


    