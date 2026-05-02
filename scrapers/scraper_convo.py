import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

auth = os.getenv('DISCORD_AUTH_TOKEN')
userId = os.getenv('MY_DISCORD_USER_ID')
channel_id = os.genenv('DISCORD_CHANNEL_ID')

def poll(lastMessageId=None):
    '''
    inputs:
        lastMessageId : track the last batch processed
    
    This function polls the discord chat to fetch the chat data
    '''
    time.sleep(2)

    if lastMessageId != None:
        requestUrl = ( "https://canary.discord.com/api/v9/channels/" 
        + channel_id + "/messages?before=" + lastMessageId + "&limit=100" )
    else:
        requestUrl = ( "https://canary.discord.com/api/v9/channels/" 
        + channel_id + "/messages?limit=100" )
    
    headers = {'Authorization': auth}
    response = requests.get(requestUrl, headers=headers, timeout=2)

    lastMessageId = process(response)
    poll(lastMessageId)


def process(response):
    '''
    inputs:
        response : response from the polling and return the lastMessageId
    
    This function will process the response of each batch
    '''
    for resp in response.json():
        lastMessageId = resp["id"]
        if resp["author"]["id"] == userId and "https" not in resp["content"]:
            print(resp["content"])
    
    return lastMessageId

def main():
    poll()

main()