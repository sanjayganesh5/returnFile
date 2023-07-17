import pandas as pd
import io
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

def lambda_handler(event, context):
    # Read the Excel file from S3 or local file system
    excel_data = pd.read_excel('template.xlsx')

    # Perform manipulations on the Excel data
    # Example: Add a new column with manipulated values
    excel_data['Name'] = 'sanjayganesh'

    # Save the manipulated Excel data to a buffer
    output_buffer = io.BytesIO()
    with pd.ExcelWriter(output_buffer, engine='openpyxl') as writer:
        writer.book = openpyxl.Workbook()
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        sheet_name = 'Sheet1'  # Replace with the desired sheet name
        for row in dataframe_to_rows(excel_data, index=False, header=True):
            writer.sheets[sheet_name].append(row)
        writer.save()

    # Provide the manipulated Excel file as the API response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "Content-Disposition": "attachment; filename=manipulated_excel.xlsx"
        },
        "body": output_buffer.getvalue()
    }
