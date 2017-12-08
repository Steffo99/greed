import os
import sys
import configparser
import telegram
import threading
import time
import strings

# Check if a configuration file exists, create one if it doesn't and get the template version number.
with open("config/template_config.ini") as template_file:
    # Check if the config file exists
    if not os.path.isfile("config/config.ini"):
        # Copy the template file to the config file
        with open("config/config.ini", "w") as config_file:
            config_file.write(template_file.read())
    # Find the template version number
    config = configparser.ConfigParser()
    config.read_file(template_file)
    template_version = int(config["Config"]["version"])

# Overwrite the template config with the values in the config
with open("config/config.ini") as config_file:
    config.read_file(config_file)

# Check if the file has been edited
if config["Config"]["is_template"] == "yes":
    print("A config file has been created in config/config.ini.\n"
          "Edit it with your configuration, set the is_template flag to false and restart this script.")
    sys.exit(1)

# Check if the version has changed from the template
if template_version > int(config["Config"]["version"]):
    # Reset the is_template flag
    config["Config"]["is_template"] = "yes"
    # Update the config version
    config["Config"]["version"] = str(template_version)
    # Save the file
    with open("config/config.ini", "w") as config_file:
        config.write(config_file)
    # Notify the user and quit
    print("The config file in config/config.ini has been updated.\n"
          "Edit it with the new required data, set the is_template flag to true and restart this script.")
    sys.exit(1)

# Create a bot instance
bot = telegram.Bot(config["Telegram"]["token"])

# Test the specified token
try:
    bot.get_me()
except telegram.error.Unauthorized:
    print("The token you have entered in the config file is invalid.\n"
          "Fix it, then restart this script.")
    sys.exit(1)

# Create a dictionary linking the chat ids to the ChatWorker objects
# {"1234": <ChatWorker>}
chat_workers = {}

# Current update offset; if None it will get the last 100 unparsed messages
next_update = None


# Main loop of the program
while True:
    # Get a new batch of 100 updates and mark the last 100 parsed as read
    updates = bot.get_updates(offset=next_update)
    # Parse all the updates
    for update in updates:
        # If the update is a message...
        if update.message is not None:
            # Ensure the message has been sent in a private chat
            if update.message.chat.type != "private":
                # Notify the chat
                bot.send_message(update.message.chat.id, strings.error_nonprivate_chat)
                # Skip the update
                continue
            # TODO: add stuff here
        # If the update is a inline keyboard press...
        if update.inline_query is not None:
            pass
        # Mark the update as read by increasing the update_offset
        next_update = update.update_id + 1
    # Temporarily prevent rate limits (remove this later)
    time.sleep(5)