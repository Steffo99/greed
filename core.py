import os
import sys
import configparser

# Check if a configuration file exists and create one if it doesn't
if not os.path.isfile("config/config.ini"):
    # Copy the template file to the config file
    with open("config/template_config.ini") as template_file, open("config/config.ini", "w") as config_file:
        config_file.write(template_file.read())

# Create a configparser
config = configparser.ConfigParser()
# Read the config file into the configparser
with open("config/config.ini") as config_file:
    config.read_file(config_file)

# Check if the file has been edited correctly
if config["Config"]["is_template"] == "yes":
    print("A config file has been created in config/config.ini.")
    print("Edit it with your configuration, set the is_template flag to false and restart this script.")
    sys.exit(1)

print("Program goes here")