from graphs.email_agent import email_agent_graph
from example_email import EMAILS



message = {"messages": [("human", EMAILS[0])]}

for chunk in email_agent_graph.stream(message, stream_mode="values"):
    chunk["messages"][-1].pretty_print()

