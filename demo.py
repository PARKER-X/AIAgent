from typing import Iterator
from phi.agent import Agent, RunResponse
from phi.utils.pprint import pprint_run_response
from agent_teams import agent_team
agent = agent_team

# Run agent and return the response as a variable
response: RunResponse = agent.run("Simulation theory in 2line")
print((response))
print("*"*20)

# Print the response in markdown format
# pprint_run_response(response, markdown=True)

# # Run agent and return the response as a stream
response_stream: Iterator[RunResponse] = agent.run("Simulation theory in 2 line", stream=True)
print((response_stream))
# # Print the response stream in markdown format
# pprint_run_response(response_stream, markdown=True, show_time=True)
