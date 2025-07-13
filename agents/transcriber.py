from youtube_transcript_api import YouTubeTranscriptApi
from schema import WorkflowState

def transcriber_node(state: WorkflowState) -> dict:
    video_id = state.video_id
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        lines = [line['text'].strip() for line in transcript if line['text'].strip()]
        return {"transcript": "\n".join(lines)}
    except Exception as e:
        return {"transcript": f"Error: {e}"}
