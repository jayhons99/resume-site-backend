import json
import boto3
import os

# import requests
dynamodb = boto3.resource('dynamodb')
dynamodb_table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }
    dynamodb_table.update_item(
        Key={
            'metric': 'stats'
        },
        UpdateExpression= 'ADD numOfVisits :inc',
        ExpressionAttributeValues={
            ':inc': 1
        }
    )
    response = dynamodb_table.get_item(
        Key={
            'metric': 'stats'
        }
    )
    newCount = response['Item']['numOfVisits']
    serialize_count = int(newCount)
    return {
        "statusCode": statusCode,
        "headers": headers,
        "body": json.dumps({
            "message": "Count updated",
            "updatedCount": serialize_count
        }),
    }
