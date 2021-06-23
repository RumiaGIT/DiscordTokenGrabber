# DiscordTokenGrabber
Small, Python-based script for fetching Discord user tokens on Windows-based machines\
This script purely serves for educational and self-studying purposes\
Additionally, the script has been sanitized, removing the webhook and IP-grabbing code\
I am in no way responsible for third-party modification and malicious usage of said code

# Features
* Scans for multiple versions of Discord on the same machine
* Works for Discord, Discord Canary, Discord PTB, Google Chrome, Opera, Brave, and Yandex 
* For detected Discord versions, scans .log and .ldb files for tokens using regex
* Sends results to a webhook on Discord
* Displays a fake and customizable error message

# How to use
1. Create a webhook on Discord and fill out the empty Webhook_URL variable with the webook url
2. Turn the script into a .exe using pyinstaller or similar means
3. Run the .exe on any Windows-based machine
4. View results of the script in the webhook's channel on Discord

23/06/2021
