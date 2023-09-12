import requests
import os
import boto3
import json

def lambda_handler(event, context):
    # Extract the callback token from the incoming event
    print(f"Received {event=} and {context=}")
    callback_token = event.get('token')
    
    # Define the callback URL (API Gateway endpoint)
    callback_url = "https://fxmcaazn53.execute-api.us-east-1.amazonaws.com/Prod/callback"
    secrets_client = boto3.client('secretsmanager')
    secrets_value = secrets_client.get_secret_value(SecretId='sahil-test-4-process-bp-project-secrets')
    secrets_json = json.loads(secrets_value["SecretString"])
    print(f"Found secrets {secrets_json}")
    openai_api_key = secrets_json.get('OPENAI_API_KEY')
    print(f"Using api key {openai_api_key}")
    response = requests.post('https://haunmzwtsq.us-east-1.awsapprunner.com/chat/completions', json={
     "model": "gpt-4",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 1
    }, headers={
        'callback-url': callback_url,
        'callback-token': callback_token,
        'Authorization': f'Bearer {openai_api_key}'
    })
    print(f"Sent request {response.request.body} with headers {response.request.headers}")
    print(f"Received response({response.status_code}) {response.text}")
    return {
            'statusCode': 200,
            'body': 'Request sent to external API'
        }
