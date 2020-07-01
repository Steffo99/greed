# Greed

A [customizable](/config/template_config.ini), [multilanguage](/strings) Telegram shop bot with [Telegram Payments support](https://core.telegram.org/bots/payments)!  

## Demo

Send a message to [@greedtestbot](https://t.me/greedtestbot) on Telegram to view a demo of the bot in action!

Use the special credit card number `4242 4242 4242 4242` to add unlimited credit to your account. 

## Screenshots

![](https://i.imgur.com/FdT2tRV.png)

![](https://i.imgur.com/rDYWdUB.png)

![](https://i.imgur.com/9plMzO6.png)

## Requirements

* [Python 3.6 (or higher)](https://www.python.org/)
* The packages specified in `requirements.txt` (install with `pip install -r requirements.txt`)
* An Internet connection
* A Telegram bot token (obtainable at [@Botfather](https://t.me/Botfather))
* A payment provider token (obtainable by [connecting a provider with your bot](https://t.me/Botfather))
* _Optional: a [git client](https://git-scm.com/)_
* _Optional: a [sentry.io](https://sentry.io) token_

Consider renting a VPS to host the bot on; a cheap one should do, as greed is pretty lightweight! :)

## Installation

This installation procedure assumes you have `python3.8` installed on an Ubuntu server. If you have a different version installed, 

1. Download the project files by running:
   ```bash
   git clone https://github.com/Steffo99/greed.git
   ```

2. Create a new virtualenv:
   ```bash
   virtualenv -p python3.8 venv
   ```

3. Activate the virtualenv:
   ```bash
   source venv/bin/activate
   ```

4. Install the project requirements:
   ```bash
   pip install -r requirements.txt
   ```
   
5. _Optional:_ For colored output, install [coloredlogs](https://pypi.org/project/coloredlogs/):
   ```bash
   pip install coloredlogs
   ```

6. Generate the configuration file:
   ```bash
   python -OO core.py
   ```

7. Edit the configuration file to your preferences:
   ```bash
   nano config/config.ini
   ```
   Ensure the `is_template` field is set to `no`.  
   Press **Ctrl+X** and then two times **Enter** to save and quit.
   
8. Generate the database:
   ```bash
   python -OO database.py
   ```

9. _Optional:_ customize the files in the `strings` folder for custom messages.

10. Start the bot:
    ```bash
    python -OO core.py
    ```

11. Open Telegram, and send a `/start` command to your bot to be promoted to 💼 Manager.

12. _Optional:_ Stop the bot, and start it in a `screen` so it can keep running even after you close the console window:
    ```bash
    screen venv/bin/python -OO core.py
    ```
    To safely detach the screen, press Ctrl+A and then Ctrl+D.

## Usage

All features can be accessed through the Telegram bot chat.

As a 💼 Manager, you can add new products, check the placed orders, create new transactions and generate .csv log files.  
You can also add additional 💼 Managers.

Users will be able to add credit to their wallet, place orders and contact you in case they require assistance.

## Updating

To update the bot, run the following commands:

```bash
git stash
git pull
git stash pop
```

## Documentation and help

If you find a bug, have an idea for a new feature or just require help with `greed`, please [post an issue](https://github.com/Steffo99/greed/issues/new) on GitHub, or, if GitHub is blocked in your country, join [the Telegram group](https://t.me/greed_project) and send a message there.

If you can read Italian, you can try to read the [paper](https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/edit?usp=sharing) I wrote about greed for my final High School exam.

If you are proficient in Python, you can also try reading the code. Most of the bot interactions can be found in the [`worker.py`](worker.py) file, so try to have a look there.

## Forks

Some people made a copy of Greed and added or changed some things to it (they made a _fork_).  
These forks are listed below.

> Please note that @Steffo99, the main developer of `greed`, does not endorse any of these forks.

### Bitcoin - Blockonomics

[DarrenWestwood](https://github.com/DarrenWestwood) is currently maintaining a [`greed`](https://github.com/DarrenWestwood/greed) fork adding **Bitcoin support** through [Blockonomics](https://www.blockonomics.co/).
