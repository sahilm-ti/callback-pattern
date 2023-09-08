import requests
import threading

def request_task(url, json):
    requests.post(url, json=json)


def fire_and_forget(url, json):
    threading.Thread(target=request_task, args=(url, json)).start()

def lambda_handler(event, context):
    # Extract the callback token from the incoming event
    print(f"Received {event=} and {context=}")
    callback_token = event.get('token')
    
    # Define the callback URL (API Gateway endpoint)
    callback_url = "https://fxmcaazn53.execute-api.us-east-1.amazonaws.com/Prod/callback"
    
    fire_and_forget('https://fxmcaazn53.execute-api.us-east-1.amazonaws.com/Prod/external-api', json={
        'callback_url': callback_url,
        'callback_token': callback_token
    })
    return {
            'statusCode': 200,
            'body': 'Request sent to external API'
        }
