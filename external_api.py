import requests
import time

def lambda_handler(event, context):
    print(f"Received {event=} and {context=}")
    # Extract the callback URL and token from the incoming event
    callback_url = event.get('callback_url')
    callback_token = event.get('callback_token')
    
    # Simulate some processing
    time.sleep(3)

    # Make a request to the callback URL
    response = requests.post(callback_url, json={
        'token': callback_token,
        'status': 'completed'
    })
    
    if response.status_code == 200:
        return {
            'statusCode': 200,
            'body': 'Callback successful'
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Callback failed'
        }
