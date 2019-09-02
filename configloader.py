import sys
import os
import configparser

# Check if the config file exists, and create one if it doesn't
if not os.path.isfile("config/config.ini"):
    # Open the template file and create the config file
    with open("config/template_config.ini") as template_file, open("config/config.ini", "w") as config_file:
        # Copy the template file to the config file
        config_file.write(template_file.read())

with open("config/template_config.ini") as template_file:
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
