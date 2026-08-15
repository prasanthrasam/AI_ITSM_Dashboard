import streamlit as st

def sidebar():

    with st.sidebar:

        st.image("assets/logo.png", width=120)

        st.markdown("# AI ITSM")

        st.caption("Enterprise Analytics")

        st.markdown("---")

        page = st.radio(
            "",
            [
                "🏠 Dashboard",
                "📊 Incident Analytics",
                "🎯 SLA Dashboard",
                "⚡ Availability",
                "🤖 AI Assistant",
                "📄 Reports"
            ]
        )

        st.markdown("---")

        st.info(
            """
Version 1.0

Powered by

• Streamlit

• Plotly

• OpenAI
"""
        )

    return page