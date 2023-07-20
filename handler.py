import json
import io
import openpyxl

def generate_excel_file():
    # Create a new workbook and worksheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Add some data to the worksheet (example)
    sheet['A1'] = 'Name'
    sheet['B1'] = 'Age'
    sheet['A2'] = 'John Doe'
    sheet['B2'] = 30
    sheet['A3'] = 'Jane Smith'
    sheet['B3'] = 25

    return workbook

def lambda_handler(event, context):
    try:
        # Generate the Excel file
        workbook = generate_excel_file()

        # Save the workbook to a buffer
        excel_buffer = io.BytesIO()
        workbook.save(excel_buffer)
        excel_buffer.seek(0)

        # Generate the API Gateway response
        response = {
            "statusCode": 200,
            "body": excel_buffer.read(),
            "headers": {
                "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "Content-Disposition": "attachment; filename=my_excel_file.xlsx"
            }
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
        }

    return response
