import json
def lambda_handler(event, context):
    print(f"Received {event=} and {context=}")
    body = event.get('body')
    body_json = json.loads(body)
    callback_url = body_json.get('callback_url')
    callback_token = body_json.get('callback_token')
    print(f"Make a request to {callback_url=} with {callback_token=}")
    return {
            'statusCode': 200,
            'body': 'Callback successful'
        }