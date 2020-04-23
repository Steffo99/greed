import sys
import os
import configparser
import logging


# Logs won't show up for this file as it is imported before logging is configured
log = logging.getLogger(__name__)


# Check if the config file exists, and create one if it doesn't
if not os.path.isfile("config/config.ini"):
    log.debug("Creating config.ini from template_config.ini")
    # Open the template file and create the config file
    with open("config/template_config.ini", encoding="utf8") as template_file, \
         open("config/config.ini", "w", encoding="utf8") as config_file:
        # Copy the template file to the config file
        config_file.write(template_file.read())

with open("config/template_config.ini", encoding="utf8") as template_file:
    # Find the template version number
    config = configparser.ConfigParser()
    config.read_file(template_file)
    template_version = int(config["Config"]["version"])
    log.debug(f"Template is version {template_version}")

# Overwrite the template config with the values in the config
with open("config/config.ini", encoding="utf8") as config_file:
    config.read_file(config_file)
    config_version = int(config["Config"]["version"])
    log.debug(f"Config is version {template_version}")

# Check if the file has been edited
if config["Config"]["is_template"] == "yes":
    log.debug("Config is a template, aborting...")
    log.fatal("A config file has been created in config/config.ini.\n"
              "Edit it with your configuration, set the is_template flag to 'no' and restart this script.")
    sys.exit(1)

# Check if the version has changed from the template
if template_version > config_version:
    log.debug("Config is older than Template, trying to merge...")
    # Reset the is_template flag
    config["Config"]["is_template"] = "yes"
    # Update the config version
    config["Config"]["version"] = str(template_version)
    # Save the file
    with open("config/config.ini", "w", encoding="utf8") as config_file:
        log.debug("Writing merged config file...")
        config.write(config_file)
    # Notify the user and quit
    log.debug("Config is now a template, aborting...")
    log.fatal("The config file in config/config.ini has been updated.\n"
              "Edit it with the new required data, set the is_template flag to true and restart this script.")
    sys.exit(1)
