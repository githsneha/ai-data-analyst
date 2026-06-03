# AI-Powered Data Analytics Platform

An intelligent analytics platform that enables users to upload datasets, query data using natural language, automatically generate SQL queries using Gemini AI, create interactive visualizations, and receive AI-generated business insights.

##  Features

### Dataset Upload
- Upload CSV datasets through a simple Streamlit interface
- Automatic schema detection
- Dynamic SQLite database creation

### Natural Language to SQL
Ask questions in plain English such as:

> Show the top 10 customers by revenue

> Which region generated the highest sales?

> What is the average order value?

The platform automatically converts these questions into executable SQL queries using Gemini AI.

### Interactive Visualizations
- Bar Charts
- Pie Charts
- Line Charts
- Scatter Plots

Built with Plotly for interactive exploration.

### AI-Generated Business Insights
The application analyzes query results and generates:
- Key observations
- Business recommendations
- Trend analysis
- Performance summaries

###  Export Results
- Download query outputs as CSV files
- Use results for further reporting and analysis

### Data Preprocessing
- Removes duplicate records before loading datasets
- Automatically detects dataset schema

---

## Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Streamlit | Web Interface |
| SQLite | Database |
| Pandas | Data Processing |
| Plotly | Visualizations |
| Gemini API | LLM Integration |

---

##  Project Structure

```text
ai-data-analyst/
│
├── ai/
│   ├── dataset_explainer.py
│   ├── gemini_client.py
│   ├── insight_generator.py
│   ├── question_classifier.py
│   └── sql_generator.py
│
├── data/
│   └── uploads/
│
├── database/
│   ├── db.py
│   └── __init__.py
│
├── utils/
│   ├── data_loader.py
│   ├── schema_detector.py
│   └── __init__.py
│
├── visualization/
│   ├── charts.py
│   └── __init__.py
│
├── app.py
├── database.db
├── requirements.txt
└── .env
```

---

## How It Works

```text
User Uploads CSV
        │
        ▼
Dataset Processing
(Remove Duplicates)
        │
        ▼
Schema Detection
        │
        ▼
Natural Language Query
        │
        ▼
Gemini AI
(SQL Generation)
        │
        ▼
SQLite Execution
        │
        ▼
Results + Charts
        │
        ▼
AI Business Insights
```

---

## Example Workflow

### User Question

```text
Show the top 5 products by sales
```

### Generated SQL

```sql
SELECT product_name,
SUM(sales) AS total_sales
FROM dataset
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 5;
```

### Output

- Query Results
- Interactive Visualization
- AI Generated Insights
- Downloadable CSV

---

## Installation

### Clone Repository

```bash
git clone https://github.com/githsneha/ai-data-analyst.git
cd ai-data-analyst
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## Key Highlights

- Natural Language to SQL using Gemini AI
- Interactive Analytics Dashboard
- AI-Powered Business Intelligence
- Automated Schema Detection
- CSV Export Functionality
- Streamlit-Based User Interface

---

## Future Improvements

- Multi-dataset analysis
- Data quality reporting
- Dashboard export to PDF
- Predictive analytics
- Voice-to-query support
- Conversational analytics assistant

---

## ⭐ If you found this project useful, consider giving it a star.