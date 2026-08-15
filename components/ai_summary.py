import streamlit as st
from services.ai_service import generate_ai_summary


def generate_dashboard_summary(df):

    total = len(df)

    p1 = len(df[df["Priority"] == "P1"])

    sla = (df["SLA_Met"] == "Yes").mean() * 100

    top_app = df["Application"].value_counts().idxmax()

    top_group = df["Assignment_Group"].value_counts().idxmax()

    prompt = f"""
You are an ITSM Service Delivery Consultant.

Analyze the following dashboard metrics and provide:

1. Executive Insights
2. Business Risks
3. Recommendations
4. Next Steps

Metrics

Total Incidents : {total}

P1 Incidents : {p1}

SLA Compliance : {sla:.2f}%

Top Application : {top_app}

Top Assignment Group : {top_group}

Keep the response professional using bullet points.
"""

    with st.spinner("🤖 AI is analyzing incident data..."):

        result = generate_ai_summary(prompt)

    st.success(result)