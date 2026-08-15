# 📊 ITSM Dashboard

The application provides an interactive ITSM dashboard in addition to the AI Knowledge Assistant.

The dashboard is designed to provide a consolidated view of ITSM operational performance and trends.

## Dashboard Capabilities

The dashboard provides:

- 📌 ITSM KPI cards
- 📊 Incident analysis
- 📈 Trend visualizations
- 📉 Performance analysis
- 🔎 Interactive filtering
- 📋 Operational data views
- 📊 Plotly-based charts
- 🤖 AI-powered ITSM knowledge assistance

## Dashboard Workflow

```text
ITSM Data
    |
    v
Data Processing
    |
    v
Pandas
    |
    v
KPI Calculation
    |
    +-------------------+
    |                   |
    v                   v
KPI Cards          Plotly Charts
    |                   |
    +---------+---------+
              |
              v
       Streamlit Dashboard
