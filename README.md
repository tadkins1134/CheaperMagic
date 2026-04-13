# CheaperMagic
This is a discord bot that will poll for magic cards of interest and update the user that the card is around a decent price

TODO:
1. Setup the bot to allow users to track their own list of cards with a given desired price
    -This list currently will be stored in memory and lost if the bot restarts. 
    -Future stretch goal would be to add a database to hold this information the persist across restarts.
2. Obtain access to an API from TCGPlayer to gain access to the cards
3. Add polling mechanism to retrieve new card data at the users desired time frame


Learned Lessons:
1. To keep libraries separate and not cause issues on system installs I am using a venv which is just a virtual enviornment so I can use the libraries needed but contain them here.
