from openpyxl import load_workbook
from flask import send_file


def lambda_handler(event, context):
    wb = load_workbook('template.xlsx')
    sheet = wb['Sheet1']
    # Save the manipulated Excel data to a buffer
    sheet['A2'] = 'SanjayGanesh'
    wb.save('output.xlsx')
    return send_file('output.xlsx', as_attachment=True, download_name='output.xlsx')
