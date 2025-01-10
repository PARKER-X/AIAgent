import streamlit as st
from agent_teams import agent_team  # Assuming you have agent_team already implemented

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
task_option = st.selectbox("Choose a task:", options=["Summarize News", "Get Stock Information"])

# Based on the task, show relevant input fields
if task_option == "Summarize News":
    news_content = st.text_area("Enter news article text or URL to summarize:", height=150)

    if st.button("Summarize News"):
        if news_content:
            with st.spinner("Summarizing..."):
                try:
                    # Summarize news using web agent
                    response = agent_team.ask(f"Summarize the news article: {news_content}")
                    st.session_state.summaries.append({"news": news_content, "summary": response})

                    # Show the summary
                    st.subheader("Summary:")
                    st.write(response)

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter some news content to summarize.")

elif task_option == "Get Stock Information":
    stock_symbol = st.text_input("Enter stock symbol (e.g., AAPL, NVDA):")

    if st.button("Get Stock Info"):
        if stock_symbol:
            with st.spinner("Fetching stock information..."):
                try:
                    # Get stock data using finance agent
                    response = agent_team.ask(f"Get the latest stock information for {stock_symbol}")
                    st.session_state.stocks.append({"stock_symbol": stock_symbol, "info": response})

                    # Show the stock information
                    st.subheader(f"Stock Info for {stock_symbol}:")
                    st.write(response)

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a stock symbol.")

# Show previous summaries or stock info if any
if "summaries" in st.session_state and st.session_state.summaries:
    st.subheader("Previous Summaries:")
    for idx, entry in enumerate(st.session_state.summaries):
        st.write(f"### News {idx+1}")
        st.write(f"**Original News:**\n{entry['news']}")
        st.write(f"**Summary:**\n{entry['summary']}")

if "stocks" in st.session_state and st.session_state.stocks:
    st.subheader("Previous Stock Information:")
    for idx, entry in enumerate(st.session_state.stocks):
        st.write(f"### Stock {idx+1}")
        st.write(f"**Stock Symbol:** {entry['stock_symbol']}")
        st.write(f"**Information:**\n{entry['info']}")