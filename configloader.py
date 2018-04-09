import sys
import os
import configparser

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
