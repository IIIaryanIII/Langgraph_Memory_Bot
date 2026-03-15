from typing_extensions import TypedDict
from dotenv import load_dotenv
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

client = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]


def chatbot(state: State):
    print("chatbot node called:", state)

    response = client.invoke(state["user_query"])
    state["llm_output"] = response.content

    return state


def evaluate_response(state: State) -> Literal["chatbot_gemini", "end"]:
    print("evaluate_response node:", state)

    if True:
        return "end"
    else:
        return "chatbot_gemini"


def chatbot_gemini(state: State):
    print("chatbot_gemini node:", state)

    response = client.invoke(state["user_query"])
    state["llm_output"] = response.content

    return state


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)

graph_builder.add_edge(START, "chatbot")

graph_builder.add_conditional_edges(
    "chatbot",
    evaluate_response,
    {
        "chatbot_gemini": "chatbot_gemini",
        "end": END
    }
)

graph_builder.add_conditional_edges(
    "chatbot_gemini",
    evaluate_response,
    {
        "chatbot_gemini": "chatbot_gemini",
        "end": END
    }
)

graph = graph_builder.compile()


updated_state = graph.invoke({"user_query": "3*3"})
print(updated_state)
