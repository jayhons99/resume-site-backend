import json
import boto3
import os
# import requests

dynamodb = boto3.resource('dynamodb')
dynamo_table = dynamodb.Table(os.environ['TABLE_NAME'])


def lambda_handler(event, context):
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }
    response = dynamo_table.get_item(
        Key={
            'metric': 'stats'
        }
    )
    getCount = response['Item']['numOfVisits']
    serialize_count = int(getCount)
    return {
        "statusCode": statusCode,
        "headers": headers,
        "body": json.dumps({
            "message":  "GET request success",
            "numOfVisits": serialize_count
        }),
    }
