from langgraph.graph import StateGraph, START

from graph.node import retrieve, generate
from graph.state import State


# build the graph
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")

# compile the graph
graph = graph_builder.compile()