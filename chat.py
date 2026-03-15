from typing_extensions import TypedDict
from dotenv import load_dotenv
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

class State(TypedDict):
    messages: list[Annotated[list, "message"]]

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return{"messages": [response]}

def samplenode(state: State):
    print("samplenode is called", state)
    return{"messages": ["\n\nHi,This is a mesaage from samplenode"]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi, My name is Aryan"]}))