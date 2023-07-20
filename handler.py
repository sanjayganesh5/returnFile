from openpyxl import load_workbook
from io import BytesIO
import base64


def lambda_handler(event, context):
    wb = load_workbook(filename='template.xlsx',
                       read_only=False)
    sheet = wb.active
    # Save the manipulated Excel data to a buffer
    sheet.cell(row=2, column=1, value='SanjayGanesh')
    buffer = BytesIO
    wb.save(buffer)
    buffer.seek(0)
    updated_excel = buffer.getvalue()
    encoded_excel = base64.b64encode(updated_excel).decode('utf-8')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            # Set the content type to Excel
            'Content-Disposition': 'attachment; filename="example.xlsx"',  # Suggest a filename for the user
        },
        'body': encoded_excel,
        'isBase64Encoded': True,  # Indicate that the body is base64 encoded
    }
