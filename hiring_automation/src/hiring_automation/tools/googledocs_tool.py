from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List
from google.oauth2 import service_account
import os 
from googleapiclient.discovery import build

class AppendCandidateInfoInput(BaseModel):
    """Input schema for AppendCandidateInfoTool."""
    name: str = Field(..., description="Name of the candidate.")
    email: str = Field(..., description="Email of the candidate.")
    skills: List[str] = Field(..., description="List of skills of the candidate.")
    education: List[str] = Field(..., description="List of education details of the candidate.")
    experience: List[str] = Field(..., description="List of experience details of the candidate.")

class AppendCandidateInfoTool(BaseTool):
    name: str = "Append Candidate Info Tool"
    description: str = "A tool that appends candidate information to a Google Doc."
    args_schema: Type[BaseModel] = AppendCandidateInfoInput

        
    def _run(self, name: str, email: str, skills: List[str], education: List[str], experience: List[str]) -> str:
        service_account_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        scopes = ['https://www.googleapis.com/auth/documents']

        credentials = service_account.Credentials.from_service_account_file(
            service_account_file, scopes=scopes)
        docs_service = build('docs', 'v1', credentials=credentials)
        doc_id = os.getenv("GOOGLE_DOC_ID")

        """Append candidate information to the Google Doc."""
        def format_list(title, items):
            return f"{title}:\n" + ''.join(f"- {item}\n" for item in items) + "\n"

        # Enhanced visual formatting for better observability
        text = (
            "📝 Candidate Information\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 Name: {name}\n"
            f"✉️  Email: {email}\n"
            "\n"
            "🔹 Skills:\n"
            + ''.join(f"   • {skill}\n" for skill in skills) +
            "\n"
            "🎓 Education:\n"
            + ''.join(f"   • {edu}\n" for edu in education) +
            "\n"
            "💼 Experience:\n"
            + ''.join(f"   • {exp}\n" for exp in experience) +
            "\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

        doc = docs_service.documents().get(documentId=doc_id).execute()
        end_index = doc['body']['content'][-1]['endIndex']

        requests = [
            {
                'insertText': {
                    'location': {'index': end_index - 1},
                    'text': text
                }
            }
        ]
        docs_service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()
        return "✅ Candidate information appended to the document."

