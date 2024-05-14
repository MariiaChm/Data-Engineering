import json
import os
import boto3
from botocore.exceptions import ClientError
from urllib import request, parse

s3 = boto3.client('s3')
BUCKET_NAME = os.environ['BUCKET_NAME']

AUTH_TOKEN = os.environ['AUTH_TOKEN']
URL = os.environ['URL']


def lambda_handler(event, context):
    dt: str = event.get('date')
    assert dt, "date is not set"

    # Prepare folder path
    year, month, day = dt.split('-')
    prefix = f'src1/sales/v1/{year}/{month}/{day}/'

    # Clean the folder
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)
    if 'Contents' in response:
        for obj in response['Contents']:
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])

    i = 0
    while True:
        i += 1
        # Prepare params
        params = {'date': dt, 'page': i}
        query_string = parse.urlencode(params)
        url = f"{URL}?{query_string}"
        new_file_key = prefix + f"page_{str(i)}.txt"

        try:
            req = request.Request(url, headers={'Authorization': AUTH_TOKEN})

            with request.urlopen(req) as response:
                response_data = response.read().decode('utf-8')
                # Save the file
                s3.put_object(Bucket=BUCKET_NAME, Key=new_file_key, Body=response_data)

        except Exception as e:
            if e.code == 404 and i > 1:
                print(i, 'is the last page')
                return {
                    'statusCode': 200,
                    'body': json.dumps('Data Fetched')
                }
            else:
                print('error', e)
                print('status', response.status)
                print('page', i)
                return {
                    'statusCode': 500,
                    'body': json.dumps('Something went wrong')
                }

    return {
        'statusCode': 200,
        'body': json.dumps('Interesting')
    }
