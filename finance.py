from phi.agent import Agent
from phi.model.groq import Groq
from api import api
from phi.tools.yfinance import YFinanceTools


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",api_key=api),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."]
    )
agent.print_response("Compare two stocks Nvda and tsla in 5lines")