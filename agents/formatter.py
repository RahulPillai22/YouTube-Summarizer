import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from schema import WorkflowState
import textwrap
import re

def clean_text(text: str) -> str:
    # Remove markdown-style bullets and bolds
    text = re.sub(r"\*{1,2}", "", text)      # remove * and **
    text = re.sub(r"^\s*[-•]\s*", "", text, flags=re.MULTILINE)  # remove list bullets
    return text

def formatter_node(state: WorkflowState) -> dict:
    final_summary = state.final_summary or state.summary
    cleaned_text = clean_text(final_summary)

    output_path = "summary_output.pdf"

    # ❌ Remove existing file if it causes permission issues
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except Exception as e:
            print(f"⚠️ Could not delete existing PDF: {e}")

    # PDF setup
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    text_obj = c.beginText(40, height - 50)
    text_obj.setFont("Helvetica", 12)

    max_width = 90  # characters per line before wrapping

    for paragraph in cleaned_text.strip().split('\n'):
        lines = textwrap.wrap(paragraph.strip(), width=max_width)
        for line in lines:
            if text_obj.getY() < 50:
                c.drawText(text_obj)
                c.showPage()
                text_obj = c.beginText(40, height - 50)
                text_obj.setFont("Helvetica", 12)
            text_obj.textLine(line)
        text_obj.textLine("")  # spacing between paragraphs

    c.drawText(text_obj)
    c.save()

    return {"pdf_path": output_path}
