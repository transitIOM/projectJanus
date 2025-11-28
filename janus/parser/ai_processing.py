from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import os
from dotenv import load_dotenv

class AiProcessing:
    def __init__(self):
        load_dotenv()
        self.endpoint = os.getenv("ENDPOINT")
        self.key = os.getenv("KEY")

    def analyze_document(self, formUrl):
        document_intelligence_client = DocumentIntelligenceClient(
            endpoint=self.endpoint, credential=AzureKeyCredential(self.key)
        )

        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-layout", AnalyzeDocumentRequest(url_source=formUrl)
        )
        result = poller.result()

        output = {
            "pages": [],
            "tables": []
        }

        for page in result.pages:
            page_data = {
                "lines": []
            }
            for line in page.lines:
                page_data["lines"].append(line.content)
            output["pages"].append(page_data)

        def extract_table_with_days(table):
            # Assume first two rows are headers
            header_row_1 = [cell for cell in table.cells if cell.row_index == 0]

            # Sort headers by column_index
            header_row_1.sort(key=lambda cell: cell.column_index)

            # Build a list of day labels for each column
            days = []
            col = 0
            while col < table.column_count:
                cell = next((c for c in header_row_1 if c.column_index == col), None)
                if cell and cell.column_span and cell.column_span > 1:
                    for _ in range(cell.column_span):
                        days.append(cell.content)
                    col += cell.column_span
                else:
                    days.append(cell.content if cell else "")
                    col += 1

            # Build headers for each column
            headers = [{"day": days[i]} for i in range(table.column_count)]

            # Extract data rows (skip first two header rows)
            data_rows = []
            for r in range(1, table.row_count):
                row_cells = [cell for cell in table.cells if cell.row_index == r]
                row_cells.sort(key=lambda cell: cell.column_index)
                row_data = [cell.content for cell in row_cells]
                data_rows.append(row_data)

            return {
                "headers": headers,
                "rows": data_rows
            }

        output["tables"] = []
        for table in result.tables:
            output["tables"].append(extract_table_with_days(table))
        output.pop("pages")

        return output
        # print(json.dumps(output, indent=2, ensure_ascii=False))