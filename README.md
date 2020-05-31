# greed

A customizable Telegram shop bot that accepts bitcoin payments. Demo at https://t.me/TgShopDemoBot

![](https://img.shields.io/badge/version-beta-blue.svg)

## Requirements

* [Python 3.6 (or higher)](https://www.python.org/)
* The packages specified in `requirements.txt` (install with `pip install -r requirements.txt`)
* An Internet connection
* A Telegram bot token (obtainable at [@Botfather](https://t.me/Botfather))
* A payment provider token (obtainable by [connecting a provider with your bot](https://t.me/Botfather))
* _Optional: a [git client](https://git-scm.com/)_
* _Optional: a [sentry.io](https://sentry.io) token_

## Installation

1. Download the project files through `git clone https://github.com/DarrenWestwood/greed.git` or [this link](https://github.com/DarrenWestwood/greed/archive/master.zip).
2. Install the project requirements with `pip install -r requirements.txt`
3. _Optional: run `pip install coloredlogs` to have colored logging output._
3. Run `python -OO core.py` to generate the configuration file.
4. Open the config folder and edit the `config.ini` file following the contained instructions.  
Ensure the `is_template` field is set to `no`.
5. Run `python -OO database.py` to generate the database tables. 
6. _Optional: customize the `strings.py` file_
7. Run `python -OO core.py` again to run the bot.
8. Open Telegram, and send a `/start` command to your bot to be promoted to administrator.

## Usage

All the bot features are available through Telegram.
As the administrator, you can add new products, check the placed orders, create new transactions and generate .csv log files.  
Users will be able to add credit to their wallet, place orders and contact you in case they require assistance.

## Updating

### Through `git`

If you downloaded `greed` through `git`, you can update it by running:

```
git stash
git pull
git stash pop
```

### By redownloading the zip file

If you downloaded `greed` through the zip archive, you can update it by redownloading [the latest version](https://github.com/Steffo99/greed/archive/master.zip) and by moving your `config.ini` and `database.sqlite` (if applicable) files to the new folder.

### Integrating Bitcoin

If you plan on accepting Bitcoin payments:

1. Complete merchant setup wizard by clicking on Get Started for Free on Blockonomics Merchants Page.
2. Depending on where you are deploying, you should set the callback URL on Blockonomics merchants page.
	* Testing: http://localhost/callback?secret=YOUR_SECRET (you can use any dummy host in place of localhost, important thing is secret should match the one in config.ini
	* Production: You need a publicly reachable URL like this https://greed.herokuapp.com/callback?secret=YOUR_SECRET
3. Configure settings in config.ini file
	* Set api_key seen on Blockonomics Merchants Page
	* Set secret as YOUR_SECRET
	* For testing, leave use_websockets = True. For production set use_websockets = False	

## Credits
This project is a fork of [greed project](https://github.com/Steffo99/greed) by @Steffo99. We would like to thank @Steffo99 for putting this in public domain. 
