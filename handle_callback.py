import json
import boto3

def lambda_handler(event, context):
    # Extract the callback token from the incoming event
    print(f"Received {event=} and {context=}")
    callback_token = event.get('token')
    
    if not callback_token:
        return {
            'statusCode': 400,
            'body': json.dumps('No callback token provided.')
        }
    
    sfn_client = boto3.client('stepfunctions')
    
    try:
        sfn_client.send_task_success(
            taskToken=callback_token,
            output=json.dumps({"result": "Task completed successfully"})
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Callback successful.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to send callback.')
        }
