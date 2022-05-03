 Languages Involved
=====================
- CSS
- HTML
- Javascript
- Python
- YAML

 How To Use
=============
To use the ChatBot, you will be in the Command-Line Terminal of your computer. The first step will be to install the requirements.txt file included in the package. This will ensure all of the necessary modules are installed prior to use*. Change directory into the place where you have downloaded or stored the files and type python3.8 app.py into the CMD. Once it is finished initalizing, type localhost:5000/ into any browser window. The ChatBot will then be available for use.

Making Changes
===============
 -- HTML:
 	Look for the appropriate HTML file if you'd like to make changes to a certain page. home_index.html changes the main page, index_uni.html changes the University ChatBot page, and index_per.html changes the Personal ChatBot page. 
 -- Javascript:
 	Modify the shared-index.js file to change or add additional javascript functions present on the html documents.
 -- CSS:
 	Modify the style.css file to make changes to the overall style of the web pages.
 -- Python:
 	The only two files you will need to modify will be chatbot.py, to add trainers and additional dialogue, and app.py, to add functions and modules that the ChatBot can use. 

Creating a SubBot
==================
If you'd like to create a new ChatBot from the bottom up, you will want to modify the app.py file. To create a separate page for said ChatBot, you can add a new @app.route to this file and specify the link in the home_index.html file. This is also where the name of the new html file you make, if you so choose, is specified. The appropriate trainers can then be added to the chatbot.py file. An example of a trainer can be seen below.

Sample Questions
=================
 -- Hello
 -- Hi
 -- How are you doing?
 -- recipe
 -- search top coffee shops
 -- Where is Piedmont?
