# AIHub Slack Bolt App Integration

This script is a simple Slack Bolt app that interacts with AIHub chatbots. The provided script supports two chatbots: one for the Instabase Platform, and one for AIHub. The following steps will help you to configure this Slack Bolt app for additional chatbots using a separate Slack app.

---

## Slack App Setup

### Step 1: Create a Slack App

1. Visit [Slack API Apps](https://api.slack.com/apps) and create a new app.
2. Enable **Socket Mode** under **Settings** > **Socket Mode**.
3. Add an **App-Level Token** with the `connections:write` scope and copy it (starts with `xapp-`).
4. Paste the token into the `SLACK_APP_TOKEN` field in your `config.cfg` file.

### Step 2: Configure OAuth & Permissions

1. Navigate to **OAuth & Permissions**.
2. Add the following bot token scopes:
   - `commands`: for handling slash commands
   - `chat:write`: to send messages
3. Install the app to your workspace.
4. Copy the **Bot Token** (starts with `xoxb-`) and paste it into the `SLACK_BOT_TOKEN` field in `config.cfg`.

### Step 3: Add Slash Commands

1. Go to **Slash Commands**.
2. Create the following commands:
   - `/request_doc`: For Instabase platform queries
   - `/request_doc_aihub`: For AIHub-specific queries

> **Note**: If you modify the command names, ensure you update the corresponding references in the Slack Bolt script.

### Step 4: Configuration File

Create a `config.cfg` file in the same directory as your script with the following content:

```ini
[DEFAULT]
SLACK_BOT_TOKEN = [Attached in Step 1]
SLACK_APP_TOKEN = [Attached in Step 2]
AIHUB_API_KEY = [Include the AIHub API Key for the user querying the AIHub chatbot]
AIHUB_API_ROOT = [Include the URL of the AIHub instance you are reaching]
AIHUB_IB_CONTEXT = [Include your AIHub context here]
AIHUB_CHAT_ID_PLATFORM = [Include the chat ID for the query being made here. This value contains the chat ID for the Instabase Platform chatbot]
AIHUB_CHAT_ID_AIHUB = [Include the chat ID for the query being made here. This value contains the chat ID for the AIHub chatbot]
```

Replace each placeholder with your actual tokens, keys, and API details.
