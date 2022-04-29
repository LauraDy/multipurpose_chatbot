==================
 Chatbot Readme
==================
------------------------------------------------------------------------------------
 Chatbots made with Python that can respond to a variety of user queries
 By Laura Dyer
------------------------------------------------------------------------------------

 Languages Involved
=====================
- CSS
- HTML
- Javascript
- Python
- YAML

 About
===========
A ChatBot is an artificial intelligence program often used to simulate human conversation. As AI technology becomes more widespread, the need for ChatBots increases for both users and the companies employing said bots. They are often used to help customers due to their ability to be present online 24 hours a day 7 days a week. This also reduces the need for human employees in these situations. For personal ChatBots, the user prefers for the bot to seem more human than artificial. 

 How To Use
=============
:underline:`Getting Started`
To use the ChatBot, you will be in the Command-Line Terminal of your computer. The first step will be to install the requirements.txt file included in the package. This will ensure all of the necessary modules are installed prior to use*. Change directory into the place where you have downloaded or stored the files and type python3.8 app.py into the CMD. Once it is finished initalizing, type localhost:5000/ into any browser window. The ChatBot will then be available for use.

:underline:`Making Changes`
 -- HTML:
 	Look for the appropriate HTML file if you'd like to make changes to a certain page. home_index.html changes the main page, index_uni.html changes the University ChatBot page, and index_per.html changes the Personal ChatBot page. 
 -- Javascript:
 	Modify the shared-index.js file to change or add additional javascript functions present on the html documents.
 -- CSS:
 	Modify the style.css file to make changes to the overall style of the web pages.
 -- Python:
 	The only two files you will need to modify will be chatbot.py, to add trainers and additional dialogue, and app.py, to add functions and modules that the ChatBot can use. 

:underline:`Creating a SubBot`
If you'd like to create a new ChatBot from the bottom up, you will want to modify the app.py file. To create a separate page for said ChatBot, you can add a new @app.route to this file and specify the link in the home_index.html file. This is also where the name of the new html file you make, if you so choose, is specified. The appropriate trainers can then be added to the chatbot.py file. An example of a trainer can be seen below.

.. code-block:: python

	greeting = [
	    "Hello",
	    "Hi there!",
	    "How are you doing?",
	    "I'm doing great.",
	    "That is good to hear",
	    "Thank you.",
	    "You're welcome.",
	    "Can I help you with anything?",
	    "Could you get me a bag of chips?"
	]

	trainer = ListTrainer(chatbot)
	trainer.train(greeting)

:underline:`Sample Questions`
 -- Hello
 -- Hi
 -- How are you doing?
 -- recipe
 -- search top coffee shops
 -- Where is Piedmont?


