import os
from dotenv import load_dotenv
import google.generativeai as genai
from schema import WorkflowState

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def summarizer_node(state: WorkflowState) -> dict:
    transcript = state.transcript
    prompt = f"Summarize the following YouTube transcript in bullet points:\n\n{transcript}"
    try:
        response = model.generate_content(prompt)
        return {"summary": response.text}
    except Exception as e:
        return {"summary": f"Error: {e}"}
