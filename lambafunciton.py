import os
import io
import json
import boto3
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))

    data = json.dumps(event)
    payload = data
    print(payload)

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT_NAME,
        ContentType='application/json',
        Body=bytes(payload, 'utf-8')
    )

    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)

    return result
