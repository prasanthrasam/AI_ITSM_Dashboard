import streamlit as st

from components.filters import create_filters
from components.kpi_cards import kpi_card
from components.ai_summary import generate_dashboard_summary
from services.data_loader import dataset_summary

from components.charts import (
    assignment_group_chart,
    category_chart,
    incident_aging_chart,
    monthly_trend_chart,
    priority_chart,
    region_chart,
    resolution_time_chart,
    sla_chart,
    sla_gauge,
    status_chart,
    top_applications_chart,
)


def render_dashboard(df):

    # ==========================================
    # Filters
    # ==========================================

    filtered = create_filters(df)

    # ==========================================
    # KPI Calculations
    # ==========================================

    total = len(filtered)

    open_inc = len(
        filtered[filtered["Status"] == "Open"]
    )

    closed = len(
        filtered[filtered["Status"] == "Closed"]
    )

    p1 = len(
        filtered[filtered["Priority"] == "P1"]
    )

    sla = filtered["SLA_Met"].eq("Yes").mean() * 100

    availability = filtered["Availability_%"].mean()

    # ==========================================
    # Executive KPI Dashboard
    # ==========================================

    st.subheader("📊 Executive KPI Dashboard")

    row1 = st.columns(3)

    with row1[0]:
        kpi_card(
            "Total Incidents",
            total,
            "#2563EB",
            "📊",
        )

    with row1[1]:
        kpi_card(
            "Open Incidents",
            open_inc,
            "#F59E0B",
            "📂",
        )

    with row1[2]:
        kpi_card(
            "Closed Incidents",
            closed,
            "#10B981",
            "✅",
        )

    st.write("")

    row2 = st.columns(3)

    with row2[0]:
        kpi_card(
            "P1 Incidents",
            p1,
            "#EF4444",
            "🚨",
        )

    with row2[1]:
        kpi_card(
            "SLA Compliance",
            f"{sla:.2f}%",
            "#7C3AED",
            "🎯",
        )

    with row2[2]:
        kpi_card(
            "Availability",
            f"{availability:.2f}%",
            "#06B6D4",
            "⚡",
        )

    st.markdown("---")

    # ==========================================
    # SLA Dashboard
    # ==========================================

    st.subheader("🎯 SLA Performance Dashboard")

    sla_met = filtered[
        filtered["SLA_Met"] == "Yes"
    ].shape[0]

    sla_breached = filtered[
        filtered["SLA_Met"] == "No"
    ].shape[0]

    total_sla = sla_met + sla_breached

    if total_sla > 0:
        sla_compliance = (
            sla_met / total_sla
        ) * 100
    else:
        sla_compliance = 0

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "✅ SLA Compliance",
            f"{sla_compliance:.2f}%"
        )

    with c2:
        st.metric(
            "🟢 SLA Met",
            sla_met
        )

    with c3:
        st.metric(
            "🔴 SLA Breached",
            sla_breached
        )

    st.markdown("---")

    # ==========================================
    # Charts
    # ==========================================

    left, right = st.columns(2)

    with left:
        priority_chart(filtered)

    with right:
        assignment_group_chart(filtered)

    left, right = st.columns(2)

    with left:
        region_chart(filtered)

    with right:
        status_chart(filtered)

    st.markdown("---")

    st.subheader("📈 Advanced Analytics")

    left, right = st.columns(2)

    with left:
        monthly_trend_chart(filtered)

    with right:
        top_applications_chart(filtered)

    st.write("")

    category_chart(filtered)

    st.write("")

    resolution_time_chart(filtered)

    st.write("")

    incident_aging_chart(filtered)

    st.write("")

    left, right = st.columns(2)

    with left:
        sla_chart(filtered)

    with right:
        sla_gauge(sla_compliance)

    st.markdown("---")

    # ==========================================
    # AI Executive Summary
    # ==========================================

    st.header("🤖 AI Executive Summary")

    generate_dashboard_summary(filtered)

    st.markdown("---")

    # ==========================================
    # Incident Details
    # ==========================================

    st.subheader("📄 Incident Details")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("---")

    # ==========================================
    # Dataset Summary
    # ==========================================

    st.subheader("📈 Dataset Summary")

    summary = dataset_summary(filtered)

    s1, s2, s3, s4 = st.columns(4)

    s1.metric("Rows", summary["Rows"])
    s2.metric("Columns", summary["Columns"])
    s3.metric(
        "Missing",
        summary["Missing Values"]
    )
    s4.metric(
        "Duplicates",
        summary["Duplicate Rows"]
    )

    return filtered