# CheaperMagic
This is a discord bot that will poll for magic cards of interest and update the user that the card is around a decent price

TODO:
1. COMPLETED: ~~Setup the bot to allow users to track their own list of cards with a given desired price~~
    -This list currently will be stored in memory and lost if the bot restarts. 
2. COMPLETED: ~~Obtain access to an API from TCGPlayer to gain access to the cards~~
3. REDACTED: ~~Add polling mechanism to retrieve new card data at the users desired time frame~~
4. COMPLETED: ~~Filter out art cards and any other occurences of cards being displayed that are NOT the card itself or one of its variants~~
5. Generate a URL link if the card queried for is below the user desired price.
6. Look into storing user List entries into a database so it can persist across bot restarts


Learned Lessons:
1. To keep libraries separate and not cause issues on system installs I am using a venv which is just a virtual enviornment so I can use the libraries needed but contain them here. This helps with avoiding conflicts on my overall system and contains things to just what I am working on.
2. Learned to work with APIs in python. Using the Just TCG API I have effectively been able to pass in specific parameters to filter to mtg, find the cards in the users list in a ascending order, find the first item in the asc order and compare it to the users desired price and the actual market price. 
