import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ----------------------------------------------------------
# 1. PRIORITY CHART
# ----------------------------------------------------------
def priority_chart(df: pd.DataFrame):
    """Priority Distribution Pie Chart"""
    if df.empty or "Priority" not in df.columns:
        st.warning("No priority data available.")
        return

    fig = px.pie(
        df,
        names="Priority",
        hole=0.45,
        title="Priority Distribution"
    )

    fig.update_layout(height=420, legend_title="Priority")
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 2. ASSIGNMENT GROUP CHART
# ----------------------------------------------------------
def assignment_group_chart(df: pd.DataFrame):
    """Assignment Group Analysis Horizontal Bar Chart"""
    if df.empty or "Assignment_Group" not in df.columns:
        st.warning("No assignment group data available.")
        return

    assignment = (
        df["Assignment_Group"]
        .value_counts()
        .reset_index()
    )
    assignment.columns = ["Assignment_Group", "Count"]

    fig = px.bar(
        assignment,
        x="Count",
        y="Assignment_Group",
        orientation="h",
        text="Count",
        title="Assignment Groups"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(height=420, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 3. REGION CHART
# ----------------------------------------------------------
def region_chart(df: pd.DataFrame):
    """Region Analysis Bar Chart"""
    if df.empty or "Region" not in df.columns:
        st.warning("No region data available.")
        return

    region = (
        df["Region"]
        .value_counts()
        .reset_index()
    )
    region.columns = ["Region", "Count"]

    fig = px.bar(
        region,
        x="Region",
        y="Count",
        text="Count",
        title="Region Analysis"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 4. STATUS CHART
# ----------------------------------------------------------
def status_chart(df: pd.DataFrame):
    """Incident Status Donut Chart"""
    if df.empty or "Status" not in df.columns:
        st.warning("No status data available.")
        return

    status = (
        df["Status"]
        .value_counts()
        .reset_index()
    )
    status.columns = ["Status", "Count"]

    fig = px.pie(
        status,
        values="Count",
        names="Status",
        hole=0.45,
        title="Incident Status"
    )

    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 5. MONTHLY TREND CHART
# ----------------------------------------------------------
def monthly_trend_chart(df: pd.DataFrame):
    """Monthly Incident Trend Line Chart"""
    if df.empty or "Opened_Date" not in df.columns:
        st.warning("No trend data available.")
        return

    trend = df.copy()
    trend["Opened_Date"] = pd.to_datetime(trend["Opened_Date"], errors="coerce")
    trend = trend.dropna(subset=["Opened_Date"])

    if trend.empty:
        st.warning("No valid dates found for monthly trend.")
        return

    monthly = (
        trend.groupby(trend["Opened_Date"].dt.to_period("M"))
        .size()
        .reset_index(name="Incidents")
    )
    monthly["Opened_Date"] = monthly["Opened_Date"].astype(str)

    fig = px.line(
        monthly,
        x="Opened_Date",
        y="Incidents",
        markers=True,
        title="Monthly Incident Trend"
    )

    fig.update_layout(height=420, xaxis_title="Month", yaxis_title="Incident Count")
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 6. TOP APPLICATIONS CHART
# ----------------------------------------------------------
def top_applications_chart(df: pd.DataFrame):
    """Top 10 Applications Bar Chart"""
    if df.empty or "Application" not in df.columns:
        st.warning("No application data available.")
        return

    apps = (
        df["Application"]
        .value_counts()
        .head(10)
        .reset_index()
    )
    apps.columns = ["Application", "Incidents"]

    fig = px.bar(
        apps,
        x="Application",
        y="Incidents",
        text="Incidents",
        title="Top 10 Applications"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 7. CATEGORY CHART
# ----------------------------------------------------------
def category_chart(df: pd.DataFrame):
    """Incident Categories Bar Chart"""
    if df.empty or "Category" not in df.columns:
        st.warning("No category data available.")
        return

    category = (
        df["Category"]
        .value_counts()
        .reset_index()
    )
    category.columns = ["Category", "Incidents"]

    fig = px.bar(
        category,
        x="Category",
        y="Incidents",
        text="Incidents",
        title="Incident Categories"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(height=420)
    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 8. RESOLUTION TIME CHART
# ----------------------------------------------------------
def resolution_time_chart(df: pd.DataFrame):
    """Resolution Time Distribution Binned Chart"""
    if df.empty or "Resolution_Hours" not in df.columns:
        st.warning("No resolution time data available.")
        return

    temp = df.copy()
    bins = [0, 4, 8, 24, 72, 1000]
    labels = ["0-4 Hours", "4-8 Hours", "8-24 Hours", "1-3 Days", "3+ Days"]

    temp["Resolution Band"] = pd.cut(
        temp["Resolution_Hours"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    summary = (
        temp["Resolution Band"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    summary.columns = ["Resolution Band", "Incidents"]

    fig = px.bar(
        summary,
        x="Resolution Band",
        y="Incidents",
        text="Incidents",
        color="Resolution Band",
        title="Resolution Time Distribution"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Resolution Time",
        yaxis_title="Incident Count"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 9. INCIDENT AGING CHART
# ----------------------------------------------------------
def incident_aging_chart(df: pd.DataFrame):
    """Incident Aging Analysis Chart"""
    if df.empty or "Resolution_Hours" not in df.columns:
        st.warning("No aging data available.")
        return

    temp = df.copy()
    bins = [0, 1, 3, 7, 15, 1000]
    labels = ["0-1 Day", "1-3 Days", "3-7 Days", "7-15 Days", "15+ Days"]

    temp["Aging"] = pd.cut(
        temp["Resolution_Hours"] / 24,
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    aging = (
        temp["Aging"]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    aging.columns = ["Aging", "Incidents"]

    fig = px.bar(
        aging,
        x="Aging",
        y="Incidents",
        color="Aging",
        text="Incidents",
        title="📅 Incident Aging Dashboard"
    )

    fig.update_traces(textposition="outside")
    fig.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Incident Age",
        yaxis_title="Incident Count"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 10. SLA CHART
# ----------------------------------------------------------
def sla_chart(df: pd.DataFrame):
    """SLA Compliance Donut Chart"""
    if df.empty or "SLA_Met" not in df.columns:
        st.warning("No SLA data available.")
        return

    summary = (
        df["SLA_Met"]
        .value_counts()
        .rename_axis("SLA Status")
        .reset_index(name="Count")
    )

    summary["SLA Status"] = summary["SLA Status"].replace({
        "Yes": "SLA Met",
        "No": "SLA Breached"
    })

    fig = px.pie(
        summary,
        names="SLA Status",
        values="Count",
        hole=0.55,
        title="🎯 SLA Compliance Dashboard",
        color="SLA Status",
        color_discrete_map={
            "SLA Met": "#2ECC71",
            "SLA Breached": "#E74C3C"
        }
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")
    fig.update_layout(height=450)

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------------------------------------
# 11. SLA GAUGE
# ----------------------------------------------------------
def sla_gauge(sla_percentage: float):
    """Gauge Chart for Overall SLA Percentage"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=sla_percentage,
        title={"text": "SLA Compliance %"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2ECC71"},
            "steps": [
                {"range": [0, 80], "color": "#FF4D4D"},
                {"range": [80, 95], "color": "#FFCC00"},
                {"range": [95, 100], "color": "#00CC66"},
            ],
        }
    ))

    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)