# Documentation 

> [!WARNING]
> 
> First of all, please note that this bot is a **proof-of-concept**!  
> No guarantees are provided if you use it, including guarantees of support, so use it in the real world at your own risk!

## History

Greed was developed as an [high school finals project](https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/edit) and then continued independently of the school thanks to the contributors of various developers, who you see credited on each individual commit.

The bot has since then ceased to be developed, but issues and pull request still are sometimes handled on the creator's free time.

## Features

Greed supports:

- for **users**:
	- creating an order
	- listing the status of all orders
	- adding more funds to the bot's wallet
		- via cash
		- via Telegram Payments
	- changing language
	- displaying information and help about the bot

- for **store managers**:
	- creating / editing / deleting products
	- receiving a live stream of orders to fulfill or refund as messages
	- manually adding funds to an user
	- displaying the list of performed transactions
	- exporting the list of performed transactions as a CSV file
	- adding other users as managers and specifying their permissions

## Installation via Docker Engine

This installation procedure assumes you are on a system with `docker` installed, with a supported CPU architecture.

### Requirements

* [Docker Engine](https://docs.docker.com/get-docker/)
* An Internet connection
* A Telegram bot token (obtainable at [@Botfather](https://t.me/Botfather))
* A payment provider token (obtainable by [connecting a provider with your bot](https://t.me/Botfather))

### Steps

1. Run a container using the project's Docker image:
   ```console
   # docker run --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
   ```

1. Edit the configuration file `config.toml` that was created in the `strings` directory, adding your bot and payment tokens to it:
   ```console
   # nano config/config.toml
   ```
   (Press **Ctrl+X** and then two times **Enter** to save and quit `nano`.)

1. _Optional:_ customize the files in the `strings` folder for custom messages.

1. Start the bot:
    ```console
    python -OO core.py
    ```

1. Open Telegram, and send a `/start` command to your bot to be automatically promoted to 💼 Manager.

1. Stop the bot by pressing **Ctrl+C**.

### Running the bot

After the installation, to run the bot, you'll need to:

1. Run its Docker container from the same directory you installed it from:
   ```console
   # docker run --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
   ```

### Keep the bot running

If you want to keep the bot open even after you closed your terminal window, you'll need to pass the appropriate arguments to the docker command:

1. Set the Docker container to always restart and to detach on successful start:
   ```console
   # docker run --detach --restart always --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
   ```

### Updating

To update the bot, run the following commands:

1. Find the ID of the Docker container of the bot:
   ```console
   # docker container ls
   CONTAINER ID   IMAGE                    COMMAND                CREATED         STATUS                  PORTS     NAMES
   abcdefabcdef   ghcr.io/steffo99/greed   "python -OO core.py"   6 seconds ago   Up Less than a second             relaxed_hypatia
   ```

1. Stop the Docker container of the bot:
   ```console
   # docker container stop abcdefabcdef
   ```

1. Remove the Docker container of the bot:
   ```console
   # docker container rm abcdefabcdef
   ```

1. Pull the latest Docker image of the bot:
   ```console
   # docker pull ghcr.io/steffo99/greed:latest
   ```

1. Restart the bot with the newly downloaded image:
   ```console
   # docker run --detach --restart always --volume "$(pwd)/config:/etc/greed" --volume "$(pwd)/strings:/usr/src/greed/strings" --volume "$(pwd)/data:/var/lib/greed" ghcr.io/steffo99/greed
   ```

## Installation via pip

This installation procedure assumes you are on a Linux system, using `bash`, and with `python` installed. 

### Requirements

* [Git](https://git-scm.com/)
* [Python 3.8 (or higher)](https://www.python.org/)
* An Internet connection
* A Telegram bot token (obtainable at [@Botfather](https://t.me/Botfather))
* A payment provider token (obtainable by [connecting a provider with your bot](https://t.me/Botfather))

Consider renting a virtual private server (VPS) to host the bot on; a cheap one should do, as greed is pretty lightweight! :)

### Steps

1. Download the project files by running:
   ```console
   $ git clone https://github.com/Steffo99/greed.git
   ```
   
1. Enter the newly created folder:
   ```console
   $ cd greed
   ```

1. Create a new venv:
   ```console
   $ python3 -m venv venv
   ```

1. Activate the venv:
   ```console
   $ source venv/bin/activate
   ```

1. Install the project requirements:
   ```console
   $ pip install -r requirements.txt
   ```
   
1. _Optional:_ For colored console output, install [coloredlogs](https://pypi.org/project/coloredlogs/):
   ```console
   $ pip install coloredlogs
   ```

1. Generate the configuration file:
   ```console
   $ python -OO core.py
   ```

1. Edit the configuration file `config.toml`, adding your bot and payment tokens to it:
   ```console
   $ nano config/config.toml
   ```
   (Press **Ctrl+X** and then two times **Enter** to save and quit `nano`.)

   > Beware to not enter your configuration in the `template_config.toml` file, as it will be ignored and may cause trouble when updating.

1. _Optional:_ customize the files in the `strings` folder for custom messages.

1. Start the bot:
   ```console
   $ python -OO core.py
   ```

1. Open Telegram, and send a `/start` command to your bot to be automatically promoted to 💼 Manager.

1. Stop the bot by pressing **Ctrl+C**.

### Running the bot

After the installation, to run the bot, you'll need to:

1. Activate the venv (if it has not already been activated in the current console session):
   ```console
   $ source venv/bin/activate
   ```

1. Start the bot:
   ```bash
   $ python -OO core.py
   ```

### Keep the bot running

If you want to keep the bot open even after you closed your terminal window, you'll need to use an external program, such as:

- `screen` (easier, but doesn't restart automatically)
- `systemd` (recommended, but more complex)

#### `screen`

1. Open a `screen` that will be running the bot with the following command:
    ```console
    $ screen venv/bin/python -OO core.py
    ```
    To safely detach the screen, press Ctrl+A and then Ctrl+D.

#### `systemd`

Assuming you downloaded `greed` in `/srv/greed`:

1. Create a new user named `greed`:
   ```console
   $ useradd greed --system
   ```
   
1. Give ownership of the greed folder you downloaded earlier to the `greed` user:
   ```console
   $ chown -R greed: /srv/greed
   ```

1. Create a new file in `/etc/systemd/system` named `bot-greed.service` with the following contents:
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

1. Start the `bot-greed` service:
   ```console
   $ systemctl start bot-greed
   ```
   
1. If everything goes well, enable the bot-greed service, so it will automatically start on a reboot:
   ```console
   $ systemctl enable bot-greed   
   ```

### Updating

To update the bot, run the following commands:

```console
$ git stash
$ git pull
$ git stash pop
```

> If you're using an older version of greed, you may need to recreate the configuration, as greed doesn't use `config.ini` anymore and but uses `config.toml` instead.

## Technical structure

The bot is composed of two parts:

- `core.py`, which handles communication with Telegram and dispatches updates to the workers
- `worker.py`, which handles the conversation flow for a single user, and runs on a separate thread for each conversation

Other resources used by the bot are:

- `utils.py`, containing utility methods
- `nuconfig.py`, containing the configuration loader
- `database.py`, handling interactions with a SQLite or PostgreSQL database
- `localization.py` and `strings/*`, managing the bot's languages
- `config/*`, initially containing the template to generate the configuration file, then also the configuration file itself after the bot has been run once
