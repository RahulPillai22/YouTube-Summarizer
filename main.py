from schema import WorkflowState
from langgraph.graph import StateGraph
from agents.transcriber import transcriber_node
from agents.summarizer import summarizer_node
from agents.reviewer import reviewer_node
from agents.formatter import formatter_node
from agents.fetcher import fetcher_node

def build_graph():
    g = StateGraph(WorkflowState)

    g.add_node("Fetcher", fetcher_node)
    g.add_node("Transcriber", transcriber_node)
    g.add_node("Summarizer", summarizer_node)
    g.add_node("Reviewer", reviewer_node)
    g.add_node("Formatter", formatter_node)

    g.set_entry_point("Fetcher")  # Start with Fetcher

    g.add_edge("Fetcher", "Transcriber")
    g.add_edge("Transcriber", "Summarizer")
    g.add_edge("Summarizer", "Reviewer")
    g.add_edge("Reviewer", "Formatter")
    g.set_finish_point("Formatter")

    return g

def run_graph(query: str):
    g = build_graph()
    app = g.compile()

    state = WorkflowState(query=query)
    final_state = app.invoke(state)

    print("🔗 Video ID:", final_state["video_id"])
    print("📄 PDF path:", final_state["pdf_path"])
    print("📝 Review:\n", final_state["review"])
    
if __name__ == "__main__":
    user_query = input("🎤 What video would you like summarized? ")
    run_graph(user_query)
