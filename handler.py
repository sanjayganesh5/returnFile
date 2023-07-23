import json
import traceback
import boto3
from openpyxl import Workbook
import base64
from io import BytesIO


def lambda_handler(event, context):
    try:
        # Create an Excel workbook and add content to it
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "MySheet"

        # Sample content to add to the Excel sheet
        content = [
            ["Name", "Age", "Email"],
            ["John Doe", 30, "john.doe@example.com"],
            ["Jane Smith", 25, "jane.smith@example.com"]
        ]

        for row in content:
            sheet.append(row)

        # Save the workbook to a BytesIO object
        file_stream = BytesIO()
        workbook.save(file_stream)

        # Encode the file content in Base64
        file_content_base64 = base64.b64encode(file_stream.getvalue()).decode('utf-8')

        # Generate the response with appropriate headers
        response = {
            "statusCode": 200,
            "headers": {
                "Content-Disposition": "attachment; filename=my_excel_file.xlsx",
                "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            },
            "body": file_content_base64,
            "isBase64Encoded": True
        }

        return response
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    'StackTrace': f'{traceback.format_exc()}'
                }
            )
        }
