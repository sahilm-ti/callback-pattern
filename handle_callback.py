import json
import boto3
import json

def lambda_handler(event, context):
    # Extract the callback token from the incoming event
    print(f"Received {event=} and {context=}")
    body = event.get('body')
    body_json = json.loads(body)
    callback_token = body_json.get('token')
    data = body_json.get('data')
    
    if not callback_token:
        return {
            'statusCode': 400,
            'body': json.dumps('No callback token provided.')
        }
    
    sfn_client = boto3.client('stepfunctions')
    
    try:
        x = sfn_client.send_task_success(
            taskToken=callback_token,
            output=json.dumps({"result": "Task completed successfully", "data": data})
        )
        print(f"Triggered task success {x}")
        return {
            'statusCode': 200,
            'body': json.dumps('Callback successful.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Failed to send callback because of {e}')
        }
