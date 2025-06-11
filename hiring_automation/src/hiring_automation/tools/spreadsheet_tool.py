from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import gspread
import os

class AppendRowInput(BaseModel):
    """Input schema for AppendRowTool."""
    name: str = Field(..., description="Name to append to the sheet.")
    reason: str = Field(..., description="Reason to append to the sheet.")

class AppendRowTool(BaseTool):
    name: str = "Append Row Tool"
    description: str = "A tool that appends a row to a Google Sheet."
    args_schema: Type[BaseModel] = AppendRowInput

    def _run(self, name: str, reason: str) -> str:
        print(name, reason)
        """Append a row to the Google Sheet."""
        service_account_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        spreadsheet_id = os.getenv("SPREADSHEET_ID")
        gc = gspread.service_account(filename=service_account_file)
        spreadsheet = gc.open_by_key(spreadsheet_id)
        sheet = spreadsheet.sheet1
        sheet.append_row([name, reason])
        return f"✅ Appended: {name}, {reason}"


