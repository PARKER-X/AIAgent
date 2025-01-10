import streamlit as st
from agent_teams import agent_team

st.set_page_config(page_icon="📰", layout="wide", page_title="Web & Finance Agent")

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

icon("📰")

st.subheader("Web & Finance Agent", divider="rainbow", anchor=False)

# Input for user to choose task
task_option = st.write("Get and Summarize Stock Information")

# Based on the task, show relevant input fields

Stock_content = st.text_area("Enter Stock name to summarize:", height=150)

if st.button("Summarizing..."):
        if not Stock_content.strip():
            st.error("Enter Stock name to summarize")
        
        try:
            with st.spinner("Processing your Stock..."):
                response = agent_team.run(Stock_content)
                # print(response.content[1])
                st.markdown(response.content)
        except Exception as e:
            st.error(f"An error occurred: {e}")