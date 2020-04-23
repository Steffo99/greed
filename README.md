# greed

A [customizable](/config/template_config.ini), [multilanguage](/strings) Telegram shop bot with [Telegram Payments support](https://core.telegram.org/bots/payments)!  

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

1. Download the project files through `git clone https://github.com/Steffo99/greed.git` (recommended) or [this link](https://github.com/Steffo99/greed/archive/master.zip).
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

## Documentation

`greed` currently does not have a documentation page, but you can try to read the [paper](https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/edit?usp=sharing) (in Italian) I wrote for my final Scuola Superiore exam about it.

## Help!

If you find a bug, have an idea for a new feature or just require help with `greed`, please [post an issue](https://github.com/Steffo99/greed/issues/new) on GitHub, or, if GitHub is blocked in your country, join [the Telegram group](https://t.me/greed_project) and send a message there.

## Forks

> Please note that @Steffo99, the developer of `greed`, does not endorse any of these forks.

### Bitcoin - Blockonomics

[DarrenWestwood](https://github.com/DarrenWestwood) is currently maintaining a [`greed`](https://github.com/DarrenWestwood/greed) fork with **Bitcoin support** through [Blockonomics](https://www.blockonomics.co/).
