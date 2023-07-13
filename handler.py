import io
import pandas as pd


def lambda_handler(event, context):
    # Create an in-memory buffer to store the Excel file
    excel_buffer = io.BytesIO()

    # Create a Pandas DataFrame with sample data
    data = {'Name': ['John', 'Jane', 'Alice'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']}
    df = pd.DataFrame(data)

    # Create an Excel writer using openpyxl
    writer = pd.ExcelWriter(excel_buffer, engine='openpyxl')

    # Convert the DataFrame to an Excel sheet
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Save the Excel file
    writer.close()

    # Reset the buffer position and retrieve the contents
    excel_buffer.seek(0)
    excel_data = excel_buffer.getvalue()

    # Set the appropriate headers for file download
    headers = {
        'Content-Disposition': 'attachment; filename=output.xlsx',
        'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    }

    # Return the Excel file as the HTTP response
    return {
        'statusCode': 200,
        'headers': headers,
        'body': excel_data,
        'isBase64Encoded': True
    }
