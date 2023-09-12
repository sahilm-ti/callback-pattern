import json
import boto3
import json

def lambda_handler(event, context):
    # Extract the callback token from the incoming event
    print(f"Received {event=} and {context=}")
    body = event.get('body')
    body_json = json.loads(body)
    callback_token = body_json.get('token')
    status = body_json.get('status')
    data = body_json.get('data')
    print(f"status_code: {status}, data: {data}, token: {callback_token}")
    
    if not callback_token:
        print(f"Didn't receive any callback token")
        return {
            'statusCode': 400,
            'body': json.dumps('No callback token provided.')
        }
    
    sfn_client = boto3.client('stepfunctions')
    
    try:
        if status == 200:
            print(f"Going to send task success")
            sfn_client.send_task_success(
                taskToken=callback_token,
                output=json.dumps({"result": "Task completed successfully", "data": data})
            )
            print(f"Triggered task success")
        else:
            print(f"Going to send task failure")
            try:
                sfn_client.send_task_failure(
                    taskToken=callback_token,
                    error="Task Failed",
                    cause=json.dumps(body_json)
                )
            except Exception as e:
                print(f"Failed to send failure: {e}")
            print(f"Triggered task failure")
        return {
            'statusCode': 200,
            'body': json.dumps('Callback successful.')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Failed to send callback: {e}')
        }
