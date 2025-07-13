import google.generativeai as genai
from schema import WorkflowState
import requests
import os
from dotenv import load_dotenv

load_dotenv()

model = genai.GenerativeModel("gemini-2.5-pro")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_video_url(query: str) -> tuple[str, str]:
    #Uses YouTube Search API to return video ID and title for the given query.
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "type": "video",
        "maxResults": 1
    }

    res = requests.get(url, params=params)
    data = res.json()

    if "items" not in data or len(data["items"]) == 0:
        raise ValueError("No video found for the query.")

    video_id = data["items"][0]["id"]["videoId"]
    title = data["items"][0]["snippet"]["title"]
    return video_id, title


def fetcher_node(state: WorkflowState) -> dict:
    query = state.query

    prompt = f"""Turn the following user message into a precise YouTube search query. 
Only return the query, no explanation:

"{query}"
"""

    try:
        # Step 1: Get refined search query from Gemini
        print("Generated prompt: ", prompt)
        response = model.generate_content(prompt)
        refined_query = response.text.strip()
        print("Generated Search: ", refined_query)
        # Step 2: Use YouTube Search API to get the real video
        video_id, title = fetch_video_url(refined_query)
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print("🎥 Selected YouTube Video:")
        print(f"🔗 URL: {video_url}")
        print(f"📌 Title: {title}")

        return {"video_id": video_id}

    except Exception as e:
        print(f"❌ Fetcher error: {e}")
        return {"video_id": f"Error: {e}"}
