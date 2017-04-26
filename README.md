## Command Line Item Sets: Bronze to Challenger in 30 days

The recent Leage of Legends client update removed a much beloved feature of the game, the Item Set. Now you can't create your Item Sets with the petty interface you use to be able to use. That sucks right?

##### WRONG

Now you can't make use of this feature unless you're willing to put in the work. It distinguishes the "good from the great", as the patch notes are so apt to say. If you put in the work, if you know your items, you can have an edge over the other Summoners. Take the opportunity they've given you by the horns. 

Take the Elo thats rightfully yours.

#Win

## But Forreal, how does it work?
There are actually a number of tools here. The primary one is the Item Set Creator, which makes use of much of the rest of the package. The Creator checks for your League of Legends Folder, and then prompts you for information on the item set, such as which champion it's for, what items,and how many of which item to add.
Item Set Reader is a way to read the raw .json flies and convert them from id numbers to human readable text.
Item Lookup is a way to find an item Name by its ID and vice versa.
The RiotCall and specifically league file provides a series of wrapper functions around every single up-to-date API endpoint offered. It returns a HTTP response object you can work with in your code

## Sounds good, what do I need to run it?
You'll only need two things to run this. The only dependencies for this are Python 3 and the [Requests Package](http://docs.python-requests.org/en/master/). You can install it by simply running $ pip install requests in your terminal. Once you have the dependencies, to run the tool all you need to do to run it is $ ./setcreator.py

Goodluck Summoners.
