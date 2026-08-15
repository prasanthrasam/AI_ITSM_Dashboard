import streamlit as st
import pandas as pd


# ---------------------------------------------------------
# REQUIRED COLUMNS
# ---------------------------------------------------------

REQUIRED_COLUMNS = [
    "Incident_ID",
    "Opened_Date",
    "Resolved_Date",
    "Priority",
    "Assignment_Group",
    "Application",
    "Region",
    "Status",
    "SLA_Target_Hours",
    "Resolution_Hours",
    "SLA_Met",
    "Availability_%",
    "Category",
    "Short_Description",
    "CI",
    "Problem_ID",
    "Change_ID"
]


# ---------------------------------------------------------
# LOAD EXCEL
# ---------------------------------------------------------

@st.cache_data(show_spinner=True)
def load_excel(uploaded_file):

    try:

        df = pd.read_excel(uploaded_file)

        return df, None

    except Exception as e:

        return None, str(e)


# ---------------------------------------------------------
# VALIDATE DATASET
# ---------------------------------------------------------

def validate_dataset(df):

    missing = []

    for col in REQUIRED_COLUMNS:

        if col not in df.columns:
            missing.append(col)

    return missing


# ---------------------------------------------------------
# DATA QUALITY
# ---------------------------------------------------------

def dataset_summary(df):

    summary = {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing Values": int(df.isnull().sum().sum()),

        "Duplicate Rows": int(df.duplicated().sum())

    }

    return summary