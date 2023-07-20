from openpyxl import load_workbook
from io import BytesIO
import base64
import tempfile
import os
from flask import send_file


def lambda_handler(event, context):
    wb = load_workbook(filename='template.xlsx',
                       read_only=False)
    sheet = wb.active
    # Save the manipulated Excel data to a buffer
    sheet.cell(row=2, column=1, value='SanjayGanesh')
    # Create a temporary file to save the modified Excel data
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        modified_file_path = f'{temp_file.name}.xlsx'
        wb.save(modified_file_path)
    # Read the modified Excel data
    with open(modified_file_path, 'rb') as file:
        modified_excel_content = file.read()
    
    # Remove the temporary file
    # os.remove(modified_file_path)

    # Encode the modified Excel content as base64
    encoded_modified_excel_content = base64.b64encode(modified_excel_content)

    return send_file(modified_file_path, as_attachment=True, download_name='output.xlsx')
