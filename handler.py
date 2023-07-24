import json
import boto3
import xlsxwriter
import traceback


def lambda_handler(event, context):
    try:
        # Create an Excel workbook and add content to it
        workbook = xlsxwriter.Workbook('/tmp/my_excel_file.xlsx')
        sheet = workbook.add_worksheet("MySheet")

        # Sample content to add to the Excel sheet
        content = [
            ["Name", "Age", "Email"],
            ["John Doe", 30, "john.doe@example.com"],
            ["Jane Smith", 25, "jane.smith@example.com"]
        ]

        for row_num, row_data in enumerate(content):
            for col_num, col_data in enumerate(row_data):
                sheet.write(row_num, col_num, col_data)

        workbook.close()

        # Upload the file to S3
        s3_client = boto3.client('s3')
        s3_client.upload_file('/tmp/my_excel_file.xlsx', 'excel-file-download', 'my_excel_file.xlsx')

        # Generate the S3 URL for downloading the file
        s3_url = s3_client.generate_presigned_url('get_object',
                                                  Params={'Bucket': 'excel-file-download', 'Key': 'my_excel_file.xlsx'},
                                                  ExpiresIn=3600)

        return {
            'statusCode': 200,
            'body': json.dumps({'download_url': s3_url})
        }
    except Exception as ex:
        return {
            'statusCode': 500,
            'body': json.dumps(
                {
                    f'StackTrace: {ex}': f'{traceback.format_exc()}'
                }
            )
        }
