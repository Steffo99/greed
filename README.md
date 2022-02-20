# Greed

A [customizable](/config/template_config.toml), [multilanguage](/strings) Telegram shop bot with [Telegram Payments support](https://core.telegram.org/bots/payments)!  

## Demo

Send a message to [@greedtestbot](https://t.me/greedtestbot) on Telegram to view a demo of the bot in action!

Use the special credit card number `4242 4242 4242 4242` to add unlimited credit to your account. 

## Screenshots

![](https://i.imgur.com/FdT2tRV.png)

![](https://i.imgur.com/rDYWdUB.png)

![](https://i.imgur.com/9plMzO6.png)

## Installation

This installation procedure assumes you are on a Linux system, using `bash` and have `python3.8` installed. 

### Requirements

* [Git](https://git-scm.com/)
* [Python 3.6 (or higher)](https://www.python.org/)
* An Internet connection
* A Telegram bot token (obtainable at [@Botfather](https://t.me/Botfather))
* A payment provider token (obtainable by [connecting a provider with your bot](https://t.me/Botfather))

Consider renting a VPS to host the bot on; a cheap one should do, as greed is pretty lightweight! :)

### Steps

1. Download the project files by running:
   ```bash
   git clone https://github.com/Steffo99/greed.git
   ```
   
2. Enter the newly created folder:
   ```bash
   cd greed
   ```

3. Create a new virtualenv:
   ```bash
   python3.8 -m venv venv
   ```

4. Activate the virtualenv:
   ```bash
   source venv/bin/activate
   ```

5. Install the project requirements:
   ```bash
   pip install -r requirements.txt
   ```
   
6. _Optional:_ For colored console output, install [coloredlogs](https://pypi.org/project/coloredlogs/):
   ```bash
   pip install coloredlogs
   ```

7. Generate the configuration file:
   ```bash
   python -OO core.py
   ```

8. Edit the configuration file, adding your bot and payment tokens to it:
   ```bash
   nano config/config.toml
   ```
   (Press **Ctrl+X** and then two times **Enter** to save and quit `nano`.)

9. _Optional:_ customize the files in the `strings` folder for custom messages.

10. Start the bot:
    ```bash
    python -OO core.py
    ```

11. Open Telegram, and send a `/start` command to your bot to be automatically promoted to 💼 Manager.

12. Stop the bot by pressing **Ctrl+C**.

### Running the bot

After the installation, to run the bot, you'll need to:

1. Activate the virtualenv (if it's not already activated in the current console session):
   ```bash
   source venv/bin/activate
   ```

2. Start the bot:
   ```bash
   python -OO core.py
   ```

### Keep the bot running

If you want to keep the bot open even after you closed your terminal window, you'll need to use some external program.  

Some of them are:

- `screen` (easier, but doesn't restart automatically)
- `systemd` (recommended, but more difficult)

#### `screen`

1. Open a `screen` that will be running the bot with the following command:
    ```bash
    screen venv/bin/python -OO core.py
    ```
    To safely detach the screen, press Ctrl+A and then Ctrl+D.

#### `systemd`

Assuming you downloaded `greed` in `/srv/greed`:

1. Create a new user named `greed`:
   ```bash
   useradd greed --system
   ```
   
2. Give ownership of the greed folder you downloaded earlier to the `greed` user:
   ```bash
   chown -R greed: /srv/greed
   ```

3. Create a new file in `/etc/systemd/system` named `bot-greed.service` with the following contents:
   ```ini
   [Unit]
   Name=bot-greed
   Description=Greed Bot
   Wants=network-online.target
   After=network-online.target nss-lookup.target
   
   [Service]
   Type=exec
   User=greed
   WorkingDirectory=/srv/greed
   ExecStart=/srv/greed/venv/bin/python -OO /srv/greed/core.py
   Environment=PYTHONUNBUFFERED=1
   
   [Install]
   WantedBy=multi-user.target
   ```

4. Start the bot-greed service:
   ```bash
   systemctl start bot-greed
   ```
   
5. If everything goes well, enable the bot-greed service, so it will automatically start on a reboot:
   ```bash
   systemctl enable bot-greed   
   ```
   
### Updating

To update the bot, run the following commands:

```bash
git stash
git pull
git stash pop
```

> If you're using an older version of greed, you may need to recreate the configuration, as greed won't use `config.ini` anymore and will use `config.toml` instead.

## Usage

All features can be accessed through the Telegram bot chat.

As a 💼 Manager, you can add new products, check the placed orders, create new transactions and generate .csv log files.  
You can also add additional 💼 Managers.

Users will be able to add credit to their wallet, place orders and contact you in case they require assistance.

## Documentation and help

If you find a bug, have an idea for a new feature or just require help with `greed`, please [post an issue](https://github.com/Steffo99/greed/issues/new) or [open a discussion](https://github.com/Steffo99/greed/discussions/new) on GitHub, or, if GitHub is blocked in your country, send me an email at [ste.pigozzi@gmail.com](mailto:ste.pigozzi@gmail.com)!

If you can read Italian, you can try to read the [paper](https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/edit?usp=sharing) I wrote about greed for my final High School exam.

If you are proficient in Python, you can also try reading the code. Most of the bot interactions can be found in the [`worker.py`](worker.py) file, so try to have a look there.

## Forks

Some people made a copy of Greed and added or changed some things to it (they made a _fork_).  
These forks are listed below.

> Please note that @Steffo99, the main developer of `greed`, does not endorse any of these forks.  
> **Do not file bug reports here for bugs in a fork!**

### Bitcoin - Blockonomics

[DarrenWestwood](https://github.com/DarrenWestwood) is currently maintaining a [`greed`](https://github.com/DarrenWestwood/greed) fork adding **Bitcoin support** through [Blockonomics](https://www.blockonomics.co/).
