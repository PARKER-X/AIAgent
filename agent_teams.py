from phi.agent import Agent
from phi.model.groq import Groq
from api import api
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.playground import Playground, serve_playground_app


web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile",api_key=api),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",api_key=api),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    description="You are an investment analyst that researches stock prices.",
    instructions=["Format your response using markdown and use tables to display data."]
    )

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile",api_key=api),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)

app = Playground(agents=[finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)