from pydantic import BaseModel

class WorkflowState(BaseModel):
    query: str = None
    video_id: str = None
    transcript: str = None
    summary: str = None
    review: str = None
    final_summary: str = None  
    pdf_path: str = None
