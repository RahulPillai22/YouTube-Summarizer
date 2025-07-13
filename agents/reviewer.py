import os
from dotenv import load_dotenv
import google.generativeai as genai
from schema import WorkflowState

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def reviewer_node(state: WorkflowState) -> dict:
    summary = state.summary
    prompt = f"""Review and improve the following summary. 
If it's good, return the same text. If it needs improvement, return only the improved version. 
Do not include explanations or introductions. Just give the cleaned-up summary:\n\n{summary}"""


    try:
        response = model.generate_content(prompt)
        reviewed = response.text.strip()
        
        print("\n🔹 Original Summary:\n", summary)
        print("\n🔸 Reviewed/Edited Summary:\n", reviewed)

        return {
            "review": "Edited summary generated",
            "final_summary": reviewed
        }
    except Exception as e:
        print("❌ Gemini error during review:", e)
        return {
            "review": f"Error: {e}",
            "final_summary": summary
        }