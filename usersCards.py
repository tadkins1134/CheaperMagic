import discord
from discord.ext import commands
from dataclasses import dataclass

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

magicBot = commands.Bot(command_prefix='$', intents=intents)

user = {}

@dataclass
class Card:
    name: str
    price: float

#Main function to call and build out the users card list with all necessary information.
async def main():
   cardList = addCardsList()

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
@magicBot.command(name='getMyCards')
async def cardSiteScraper():