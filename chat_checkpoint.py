from typing_extensions import TypedDict
from dotenv import load_dotenv
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()



llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return{"messages": [response]}


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

def compile_graph_with_checkpoint(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

DB_URI = "mongodb://admin:admin@localhost:27017"

config = {
    "configurable": {
        "thread_id": "Aryan"
    }
}

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:

    graph_with_checkpointer = graph_builder.compile(checkpointer=checkpointer)

    for chunk in graph_with_checkpointer.stream(
        {"messages": ["Hey what is my name?"]},
        config,
        stream_mode="values"
    ):
        print(chunk["messages"][-1])
