import streamlit as st

def kpi_card(title, value, color, icon):

    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:18px;
            border-radius:15px;
            color:white;
            box-shadow:0 4px 12px rgba(0,0,0,0.15);
            text-align:center;
            min-height:120px;
        ">
            <h1 style="font-size:40px;margin:0;">{icon}</h1>
            <h3 style="margin-top:10px;">{title}</h3>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )