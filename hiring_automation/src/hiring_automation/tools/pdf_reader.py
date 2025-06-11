from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import PyPDF2

class PDFReaderInput(BaseModel):
    """Input schema for PDFReaderTool."""
    file_path: str = Field(..., description="Path to the PDF file.")

class PDFReaderTool(BaseTool):
    name: str = "PDF Reader Tool"
    description: str = "A tool that reads a PDF file and returns its text content."
    args_schema: Type[BaseModel] = PDFReaderInput

    def _run(self, file_path: str) -> str:
        """Read a PDF file and return its text content."""
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text