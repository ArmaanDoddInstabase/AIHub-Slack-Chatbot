This is a simple integration for setting up a slack bolt app that interacts with an AIHub Chatbot. In this script, I've set it up to interact with one of two chatbots -- one for the Instabase platform, and one for AIHub. The below readme provides instructions for how to set up this slack bolt app for other chatbots, with a separate slack app.

Slack App Setup

**Step 1: Create a Slack App**


Visit Slack API Apps and create a new app.


-Enable Socket Mode under Settings > Socket Mode.

-Add an App-Level Token with the connections:write scope, and copy the token (starts with xapp-) to the *SLACK_APP_TOKEN* value in the script's config.cfg file.


**Step 2: Configure OAuth & Permissions**


Navigate to OAuth & Permissions.

Add the following bot token scopes:

*commands*, to handle slash commands

*chat:write*, to send messages


Install the app to your workspace and copy the Bot Token (starts with xoxb-) to the *SLACK_BOT_TOKEN* value in the script's config.cfg file.


**Step 3: Add Slash Commands**


Go to Slash Commands and create the following commands:


/request_doc: Use for Instabase platform queries.

/request_doc_aihub: Use for AIHub-specific queries.


These names can be adjusted, but would also need their respective command names adjusted in the attached slack bolt script.



**Step 4: Configuration File**


Create a config.cfg file in the same directory as your script:

```
[DEFAULT]
SLACK_BOT_TOKEN = [Attached in Step 1]

SLACK_APP_TOKEN = [Attached in Step 2]

AIHUB_API_KEY = [Include the AIHub API Key for the user querying the AIHub chatbot]

AIHUB_API_ROOT = [Include the URL of the AIHub instance you are reaching]

AIHUB_IB_CONTEXT = [Include your AIHub context here]

AIHUB_CHAT_ID_PLATFORM = [Include the chat ID for the query being made here. This value contains the chat ID for the Instabase Platform chatbot]

AIHUB_CHAT_ID_AIHUB = [Include the chat ID for the query being made here. This value contains the chat ID for the AIHub chatbot]
```


Replace each placeholder with your actual token, keys, and API details.
