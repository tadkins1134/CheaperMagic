import os
import requests

import discord
from discord.ext import commands
from dataclasses import dataclass
from dotenv import load_dotenv

API_KEY = os.getenv('JUSTTCG_API_KEY')
if not API_KEY:
    raise EnvironmentError("JUSTTCG_API_KEY environment variable not set.")
BASE_URL = "https://api.justtcg.com/v1"  
HEADERS = {"x-api-key": API_KEY} 

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

magicBot = commands.Bot(command_prefix='$', intents=intents)

user = {}

@dataclass
class Card:
    name: str
    price: float

@magicBot.event
async def on_ready():
    print(f'We have logged in as {magicBot.user}')

#This method is to allow the user to add cards to a list that will be scraped for on TCGPlayer
@magicBot.command(name='cards')
async def addCardsList(ctx,  price, *, card):
    if ctx.author not in user:
        user[ctx.author] = []
    usersCardList = user[ctx.author]
    usersCardList.append(Card(price=price, name=card))    
    await ctx.send(f'Added {card} with desired price of ${price}. Total cards in list now: {len(usersCardList)}')

#This method is so the user can see the card they have added to their list
@magicBot.command(name='myCards')
async def myCards(ctx):
    if ctx.author not in user:
        await ctx.send("You don't have any cards in your list.")
        return
    usersCardList = user[ctx.author]
    await ctx.send(f'Your cards: {", ".join([card.name for card in usersCardList])}')

#This method is used to clear a single card or all cards from the users card list
@magicBot.command(name='clearCards')
async def clearCards(ctx, card):
    if card == "all":
        if ctx.author in user:
            user[ctx.author] = []
            await ctx.send("Cleared all cards from your list.")
        else:
            await ctx.send("You don't have any cards in your list.")
    elif ctx.author in user and card in [c.name for c in user[ctx.author]]:
        usersCardList = user[ctx.author]
        usersCardList = [c for c in usersCardList if c.name != card]
        user[ctx.author] = usersCardList
        await ctx.send(f'Removed {card} from your list. Total cards in list now: {len(usersCardList)}')
    elif ctx.author in user:
        await ctx.send(f'{card} is not in your list. Total cards in list: {len(user[ctx.author])}')
    else:
        await ctx.send("You don't have any cards in your list.")


#This method is used by the user to scrape TCGPlayer for the cards in their list and return any that are at or below the price they set.
@magicBot.command(name='getCardsData')
async def cardsData(ctx):
    if ctx.author not in user:
        await ctx.send("You don't have any cards in your list. Please add cards before using this command.")
        return
    url = f"{BASE_URL}/cards"
    userCardList = user[ctx.author]
    for card in userCardList:
        params = {
            "q": card.name,
            "orderBy": "price",
            "order": "asc",
            "limit": 1,
            "game": "mtg"
        }
        try:
            response = requests.get(url, headers=HEADERS, params=params)
            response.raise_for_status()
            cards = response.json()["data"]
            if cards:
                lowest_priced_variant = min(cards[0]["variants"], key=lambda x: x["price"])
                market_price = lowest_priced_variant["price"]
                if market_price <= float(card.price):
                    await ctx.send(f'{card.name} is available for ${market_price}, which is at or below your desired price of ${card.price}.')
                else:
                    await ctx.send(f'{card.name} is available for ${market_price}, which is above your desired price of ${card.price}.')
            else:
                await ctx.send(f'No listings found for {card.name}.')
        except requests.exceptions.RequestException as e:
            await ctx.send(f"An error occurred while fetching data for {card.name}: {e}")


@magicBot.command(name='commandList')
async def commandList(ctx):
    commands = [
        "$cards <price> <card name> - Add a card to your list with a desired price.",
        "$myCards - View the cards in your list.",
        "$clearCards <card name>/all - Remove a specific card or all cards from your list.",
        "$getCardsData - Fetch current market data for the cards in your list and compare to your desired prices.",
    ]
    await ctx.send("Available commands:\n" + "\n".join(commands))

if __name__ == "__main__":
    magicBot.run(os.getenv('USER_TOKEN'))
