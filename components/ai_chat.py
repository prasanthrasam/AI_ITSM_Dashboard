import pandas as pd
import streamlit as st
import openai

# Replace with your LLM client configuration (e.g., OpenAI / Groq / Anthropic)
# st.secrets["OPENAI_API_KEY"] must be set in .streamlit/secrets.toml
def get_ai_response(prompt_text: str) -> str:
    client = openai.OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt_text}],
        temperature=0.0
    )
    return response.choices[0].message.content.strip()


def ai_chat(df: pd.DataFrame):
    st.subheader("💬 Ask OpsPilot AI")
    st.caption("Ask questions about incident types, SLA status, trends, and availability.")

    # Session state initialization
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render previous messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_query = st.chat_input("Ask a question about your incidents...")

    if user_query:
        # Display user question
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        # 1. Prepare Metadata Context for LLM
        columns_info = {col: str(dtype) for col, dtype in df.dtypes.items()}
        
        # Sample categorical values to prevent column value hallucination
        categorical_samples = {}
        for col in ["Priority", "Status", "Category", "SLA_Met", "Assignment_Group", "Region"]:
            if col in df.columns:
                categorical_samples[col] = df[col].dropna().unique().tolist()[:10]

        # 2. Build system prompt instructing LLM to generate single-line Pandas code
        system_prompt = f"""
You are OpsPilot AI, an expert IT Service Analytics Assistant.
You have access to a pandas DataFrame named `df` with the following properties:

Columns and Data Types:
{columns_info}

Sample Unique Categorical Values:
{categorical_samples}

User Question: "{user_query}"

INSTRUCTIONS:
1. If the user asks general conceptual questions (e.g., "What is SLA?"), provide a clear, professional ITIL explanation, and optionally add code to calculate overall SLA compliance on `df`.
2. If the user asks a question about counts, categories, dates, or metrics (e.g., "what type of incidents", "availability SLA for July"):
   - Write executable Python Pandas code using `df`.
   - Your code MUST return the answer directly (e.g., `df['Category'].value_counts()`, or `df[df['Opened_Date'].str.contains('07')]['Availability_%'].mean()`).
3. Output strictly valid JSON in this exact format:
{{
  "explanation": "Brief explanation of what is being calculated",
  "code": "Python pandas expression to evaluate"
}}
"""

        with st.chat_message("assistant"):
            with st.spinner("Analyzing incident dataset..."):
                try:
                    # Request code from LLM
                    raw_response = get_ai_response(system_prompt)
                    
                    # Clean response if wrapped in code block markers
                    cleaned = raw_response.replace("```json", "").replace("```", "").strip()
                    import json
                    parsed = json.loads(cleaned)

                    explanation = parsed.get("explanation", "")
                    code = parsed.get("code", "")

                    # Execute Pandas query safely
                    if code:
                        local_vars = {"df": df, "pd": pd}
                        result = eval(code, {"__builtins__": {}}, local_vars)
                        
                        # Format dataframe outputs nicely
                        if isinstance(result, (pd.DataFrame, pd.Series)):
                            result_display = result.to_frame() if isinstance(result, pd.Series) else result
                            formatted_answer = f"{explanation}\n\n"
                            st.markdown(formatted_answer)
                            st.dataframe(result_display, use_container_width=True)
                            st.caption(f"Executed: `{code}`")
                            
                            st.session_state.messages.append({
                                "role": "assistant", 
                                "content": f"{explanation}\n\n`{code}`\n\nResult:\n{result_display.to_string()}"
                            })
                        else:
                            # Scalar outputs (e.g., numbers, percentages)
                            formatted_answer = f"{explanation}\n\n**Result:** `{result}`\n\n*(Query: `{code}`)*"
                            st.markdown(formatted_answer)
                            st.session_state.messages.append({"role": "assistant", "content": formatted_answer})
                    else:
                        st.markdown(explanation)
                        st.session_state.messages.append({"role": "assistant", "content": explanation})

                except Exception as e:
                    error_msg = f"I encountered an error trying to process that query: `{str(e)}`"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})