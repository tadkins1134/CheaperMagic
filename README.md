# CheaperMagic Discord Bot

CheaperMagic is a Discord bot built with Python and `discord.py` that allows Magic: The Gathering players to quickly search and monitor card prices directly from Discord using the JustTCG API.

Instead of opening a browser and manually searching card marketplaces, users can track desired prices and retrieve current market data directly through Discord commands.

---

## Why I Built This

I built CheaperMagic because my friends and I frequently discuss Magic: The Gathering cards in Discord and wanted a faster way to search pricing data without constantly opening external websites.

This project was also created to improve my experience with:
- Python development
- Discord bot development
- API integration
- Asynchronous command handling
- Parsing and filtering API data

---

## Features

- Search current market prices for Magic: The Gathering cards
- Track cards with user-defined target prices
- Compare market prices against desired purchase prices
- Retrieve highest and lowest market listings for individual cards
- Filter out undesirable card conditions
- Ignore Art Series cards when retrieving lowest market listings
- Maintain separate card lists per Discord user

---

## Tech Stack

- Python
- discord.py
- JustTCG API
- requests
- Virtual Environments (`venv`)

---

## Bot Invite

Add CheaperMagic to your Discord server using the link below:

https://discord.com/oauth2/authorize?client_id=1488002488224186470

Recommended permissions:
- Send Messages
- Read Message History
- Embed Links

---

## Installation

### Clone the repository

git clone https://github.com/tadkins1134/CheaperMagic
cd CHEAPERMAGIC

### Create a `.env` file in the project root:

DISCORD_TOKEN=your_discord_token
JUSTTCG_API_KEY=your_api_key

### Running the Bot

python bot.py

---

## Commands

| Command | Description |
|---|---|
| `$commandList` | Displays all available commands |
| `$cards <price> <card name>` | Adds a card to your tracking list with a desired price |
| `$myCards` | Displays your saved card list |
| `$clearCards <card name>/all` | Removes a single card or clears your entire list |
| `$getCardsData` | Retrieves market data for tracked cards and compares against desired prices |
| `$single <card name>` | Retrieves the highest and lowest market listings for a single card |

---

## Example Usage

$single sheoldred

Sheoldred Art Card:
Highest price - $27.05 (Foil, Near Mint), in set (Prerelease Cards)

Lowest price - $12.48 (Normal - Japanese, Near Mint), in set (March of the Machine)