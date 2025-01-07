import streamlit as st
from agent_teams import agent_team  # Make sure this is the correct import for accessing your AI team

# Ask the user to input a stock symbol (e.g., TSLA for Tesla)
stocks = st.text_input('Enter a stock symbol to compare and gather market research:')


ans = agent_team.run(stocks,stream=False)  # Assuming the 'run' function processes the stock symbol and returns info
st.json(ans)

    
