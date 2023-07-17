from openpyxl import load_workbook
from flask import send_file
from io import BytesIO


def lambda_handler(event, context):
    wb = load_workbook('template.xlsx')
    sheet = wb['Sheet1']
    # Save the manipulated Excel data to a buffer
    sheet['A2'] = 'SanjayGanesh'
    buffer = BytesIO
    wb.save(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='output.xlsx')
