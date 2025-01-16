from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

## latest news with duckduckgo
web_agent = Agent(
    name= "Web Agent",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources."]
)

finance_agent= Agent(
    name="Finance Agent",
    role="Get financial data",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data."]
)

## Team leader
agent_team = Agent(
    team=[web_agent,finance_agent],
    model= Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources","use tables to display data."],
    show_tool_calls=True,
    markdown=True
)
agent_team.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True)