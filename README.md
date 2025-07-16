
# **Slack Chat Deletion Bot**

This lightweight Python script uses a Slack bot to delete messages from direct messages (DMs) and channels. While its practical use is limited, it's a useful learning tool for understanding Slack's API, authentication scopes, and message handling through bots.




## **Slack Bot**

**Slack Bot:** A slack bot is required for this script. You can make one at slack's developer portal.

**Permissions:** The slack bot requires the following Permissions in order to be able to delete messages in chats it has access to.

- chat:delete

## **🔧 Script Inputs – .env**
This script requires a few environment variables to function correctly. You can set these up by either creating a .env file or renaming the provided .env.sample file and filling in the required values.

### slackToken
Your Slack bot user token, used for authentication. You can find this on your bot's OAuth & Permissions page in the Slack Developer Portal.

_Example:_
**xoxp-...**

### botToken
Your Slack bot bot token, also found under the OAuth & Permissions section, typically listed below the user token.

_Example:_
**xoxb-...**

### userID
The channel ID of the direct message or public/private channel from which you want to delete messages.

_Example:_
**D01ABC123XY** (for DMs) & **C01XYZ789LK** (for channels)

### timeRange
Specifies how far back (in weeks) the script should go when searching for messages to delete. You can adjust this behavior in the deleteMessage() function within the delChat.py script if needed.

_Example:_
**2** (deletes messages from the past 2 weeks)

### **⚠️ Usage Notes**
- Slack’s API limits how many messages can be processed per request. Messages sent by other users (which cannot be deleted) still count toward that limit.

- If you're trying to clean up DMs, it's most effective if both participants run deletion scripts to avoid hitting those limits.

- For best results, use the script frequently to prevent older messages from becoming unreachable due to API constraints.
## **Required Python Libraries**

- os
- time
- datetime
- schedule
- dotenv
- slack_sdk
- pystray
- PIL
## **🚀 Output & Execution**
This script can be executed in two main ways, depending on your preference:

### 1. Tray Icon Launcher (Recommended)
Running the iconTray.py script will launch a system tray icon (bottom-right of the taskbar on most systems) that allows you to trigger the deletion script with ease.

- 🖼 Icon: The default tray icon is skeleton.png. You can replace this file with any image of your choice to personalize the tray icon.

- ✅ Best for: Frequent or repeated use, as it allows easy access without reopening the script.

### 2. Direct Script Execution
If you prefer command-line or direct execution:

Run `delChat.py` directly.

Inside the script's `__main__` block, you can toggle between:

- A one-time deletion: `main()`

- A repeat deletion loop (ideal for clearing extended history): `agnition()`

⚙️ Adjust the function calls in the if `__name__ == "__main__"`: block to control behavior.
