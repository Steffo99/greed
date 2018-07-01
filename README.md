# greed
A customizable Telegram shop bot, developed as a project for the final exam.  

![](https://img.shields.io/badge/version-beta-blue.svg)

## Requirements
* Python 3.6 (or higher)
* The packages specified in `requirements.txt` (install with `pip install -r requirements.txt`)
* An Internet connection
* A Telegram bot token (obtainable at [@Botfather](https://t.me/Botfather))
* A payment provider token (obtainable by [connecting a provider with your bot](https://t.me/Botfather))
* _Optional: a [sentry.io](https://sentry.io) token_

## Installation
1. Download the project files through `git clone https://github.com/Steffo99/greed.git` or [this link](https://github.com/Steffo99/greed/archive/master.zip).
2. Install the project requirements with `pip install -r requirements.txt`
3. Run `python -OO core.py` to generate the configuration file.
4. Open the config folder and edit the `config.ini` file following the contained instructions.  
Ensure the `is_template` field is set to `no`.
5. _Optional: customize the `strings.py` file_
6. Run `python -OO core.py` again to run the bot.
7. Open Telegram, and send a `/start` command to your bot to be promoted to administrator.

## Usage
All the bot features are available through Telegram.   
As the administrator, you can add new products, check the placed orders, create new transactions and generate .csv log files.  
Users will be able to add credit to their wallet, place orders and contact you in case they require assistance.
