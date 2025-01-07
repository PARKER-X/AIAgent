from phi.agent import Agent
from phi.model.groq import Groq
from api import api

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",api_key=api)
    
)

agent.print_response("Tell me about ironman in one line!")