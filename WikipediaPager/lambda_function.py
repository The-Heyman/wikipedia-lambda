import json
import wikipedia

# prints when function loads
print('Loading function')


def lambda_handler(event, context):
    ''' Wikipedia page summarizer.
        :param event: a request with a wikipedia "entity" that has page information
        :return: a response that contains the first sentence of a wikipedia page,
            the response is JSON formatted.'''
    
    if 'body' in event:
        
        event = json.loads(event["body"])
    
    entity = event["entity"]
    res = wikipedia.summary(entity, sentences=2) # first 2 sentences, result

    print(f"context: {context}, event: {event}")
    print(f"Response from wikipedia API: {res}")
    
    response = {
        "statusCode": "200",
        "headers": {"content-type": "application/json"},
        "body": json.dumps({"message": res})
    }
    
    return response