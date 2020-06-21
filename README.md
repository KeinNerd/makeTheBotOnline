
# makeTheBotOnline  !

Launch a minimal python script to take your Discord Bot always online. The idea came with the extension [Discord-Sync](https://hanashi.dev/filebase/file/1-discord-sync/) for the [Woltlab Suite](https://www.woltlab.com/) by [Hanashi](https://github.com/Hanashi). With this extension you can synchronize your Woltlab Suite user groups with the user groups of Discord. But it should also work with any other bot.

## ❗ Requirements

 - [Docker](https://docs.docker.com/get-docker/) installed
 - You need a Bot Token ([Create a Bot](https://discord.com/developers/applications))

## 📦 What's inside

 - Modified Script from [@TitusKirch](https://github.com/TitusKirch)

## 🚀 How to use

Create a Discord bot and obtain a BOT-TOKEN! Not the Client Secret!

Then create the Container with:

    docker create \
      --name=discordbotonline \
      --env 'GAMENAME=Visit KeinNerd.net' \
      --env 'DISCORDTOKEN=YOURDISCORDBOTTOKEN' \
      --restart unless-stopped \
    keinnerd/makethebotonline:latest

## 🔧 Envs

`GAMENAME` = It show what the Bot "plays" - e.g. your Website

`DISCORDTOKEN` = The Bot-Token for your Bot


## 🚨 Support

Create a Github Issue or visit our Website!

## 🙏 Contribution

This are my first steps with creating dockerimages so any contribution to expand my knowledge is welcome !


## 📖 License
This project is under the [MIT License](https://choosealicense.com/licenses/mit/).
