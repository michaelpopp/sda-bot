The official Student Disciplinary Action Bot.  

-----Events for users-----  
Greetings and farewells for various phrases

-----Commands for users-----  
$ping : Will ping the bot and return the latency in milliseconds.  
$kickme : kicks oneself.

-----Developer Notes-----  
Token for the bot is accessed in a dot env file located in the root directory.  You  
may have to produce your own token for development purposes.    

If hosted on a headless server (eg. Raspberry pi) linux tools, like tmux or  screen, can be used to
prevent termination of the program when you exit SSH (assuming that is how you are accessing the server).  

Packages needed:  
Python 3  
Pip (for Python 3)  
discordy.py  
Python-dotenv 

References:  
https://discordpy.readthedocs.io/en/stable/index.html  
https://www.twilio.com/blog/environment-variables-python    
