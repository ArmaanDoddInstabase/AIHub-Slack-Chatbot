import os
import time
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from aihub import AIHub
import requests
import time
import json
import configparser
from pathlib import Path

config_path = Path(__file__).parent / 'config.cfg'
config = configparser.ConfigParser()
config.read(config_path)

SLACK_BOT_TOKEN = str(config['DEFAULT']['SLACK_BOT_TOKEN'])
SLACK_APP_TOKEN = str(config['DEFAULT']['SLACK_APP_TOKEN'])
AIHUB_API_KEY = str(config['DEFAULT']['AIHUB_API_KEY'])
AIHUB_API_ROOT = str(config['DEFAULT']['AIHUB_API_ROOT'])
AIHUB_IB_CONTEXT = str(config['DEFAULT']['AIHUB_IB_CONTEXT'])
AIHUB_CHAT_ID_PLATFORM = str(config['DEFAULT']['AIHUB_CHAT_ID_PLATFORM'])
AIHUB_CHAT_ID_AIHUB = str(config['DEFAULT']['AIHUB_CHAT_ID_AIHUB'])


# Initializes the AIHub client
client = AIHub(api_root=AIHUB_API_ROOT, 
               api_key=AIHUB_API_KEY,
               ib_context=AIHUB_IB_CONTEXT)

# Initializes your Slack app
app = App(token=SLACK_BOT_TOKEN)

# Define the command handler for /request
@app.command("/request_doc")
def handle_request_command(ack, body, say):
    ack()
    text_value = body.get('text', '')
    print(text_value)
    authorization = "Bearer " + AIHUB_API_KEY
    input_url = AIHUB_API_ROOT + "/api/v2/queries/"
    response = requests.post(input_url, headers={ "Authorization": authorization, "IB-Context": AIHUB_IB_CONTEXT, "Content-Type": "application/json"},
        json={ "query": text_value, "source_app": { "type": "CHATBOT", "id": AIHUB_CHAT_ID_PLATFORM}},)
    data = response.json()
    print(data)
    query_id_new = data['query_id']
    print(query_id_new)
    say(f"*Processing Request:* " + "'" + text_value + "'")

    while True:
        time.sleep(1)
        given_url = AIHUB_API_ROOT + "/api/v2/queries/" + query_id_new
        response = requests.get(given_url, headers={ "Authorization": authorization, "IB-Context": AIHUB_IB_CONTEXT},)
        print(response.json())
        result = response.json()
        result_data = result['status']
        if result_data == "COMPLETE":
            response_text = result['results'][0]['response']
            say(response_text)
            break
        if result_data == "FAILED":
            say("query failed -- check script logs")
            break


# Define the command handler for /request
@app.command("/request_doc_aihub")
def handle_request_command(ack, body, say):
    ack()
    text_value = body.get('text', '')
    print(text_value)
    authorization = "Bearer " + AIHUB_API_KEY
    input_url = AIHUB_API_ROOT + "/api/v2/queries/"
    response = requests.post(input_url, headers={ "Authorization": authorization, "IB-Context": AIHUB_IB_CONTEXT, "Content-Type": "application/json"},
        json={ "query": text_value, "source_app": { "type": "CHATBOT", "id": AIHUB_CHAT_ID_AIHUB}},)
    data = response.json()
    print("data is:")
    print(data)
    query_id_new = data['query_id']
    print(query_id_new)
    say(f"*Processing Request:* " + "'" + text_value + "'")

    while True:
        time.sleep(1)
        given_url = AIHUB_API_ROOT + "/api/v2/queries/" + query_id_new
        response = requests.get(given_url, headers={ "Authorization": authorization, "IB-Context": AIHUB_IB_CONTEXT},)
        print(response.json())
        result = response.json()
        result_data = result['status']
        if result_data == "COMPLETE":
            response_text = result['results'][0]['response']
            say(response_text)
            break
        if result_data == "FAILED":
            say("query failed -- check script logs")
            break

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
