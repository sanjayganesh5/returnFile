import io
import base64
import pandas as pd

def lambda_handler(event, context):
    # Create a Pandas DataFrame with sample data
    data = {'Name': ['John', 'Jane', 'Alice'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']}
    df = pd.DataFrame(data)

    # Create an in-memory buffer to store the Excel file
    excel_buffer = io.BytesIO()

    # Create an Excel writer using pandas
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Reset the buffer position and retrieve the contents
    excel_buffer.seek(0)
    excel_data = excel_buffer.getvalue()

    # Encode the Excel data as base64
    excel_base64 = base64.b64encode(excel_data).decode('utf-8')

    # Set the appropriate headers for file download
    headers = {
        'Content-Disposition': 'attachment; filename=output.xlsx',
        'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    }

    # Return the Excel file as the HTTP response
    return {
        'statusCode': 200,
        'headers': headers,
        'body': excel_buffer.read().decode('latin1'),
        'isBase64Encoded': True
    }
