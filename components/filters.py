import streamlit as st


def create_filters(df):
    """
    Creates sidebar filters and returns filtered DataFrame.
    """

    st.sidebar.header("🔍 Filters")

    # Priority
    priority = st.sidebar.multiselect(
        "Priority",
        options=sorted(df["Priority"].dropna().unique()),
        default=sorted(df["Priority"].dropna().unique())
    )

    # Region
    region = st.sidebar.multiselect(
        "Region",
        options=sorted(df["Region"].dropna().unique()),
        default=sorted(df["Region"].dropna().unique())
    )

    # Assignment Group
    assignment = st.sidebar.multiselect(
        "Assignment Group",
        options=sorted(df["Assignment_Group"].dropna().unique()),
        default=sorted(df["Assignment_Group"].dropna().unique())
    )

    # Status
    status = st.sidebar.multiselect(
        "Status",
        options=sorted(df["Status"].dropna().unique()),
        default=sorted(df["Status"].dropna().unique())
    )

    # Filter Data
    filtered_df = df[
        (df["Priority"].isin(priority)) &
        (df["Region"].isin(region)) &
        (df["Assignment_Group"].isin(assignment)) &
        (df["Status"].isin(status))
    ]

    return filtered_df