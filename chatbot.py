from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from googlesearch import search
from datetime import date

today = date.today()

# Creating ChatBot Instance
chatbot = ChatBot('PersonalBot')

 # Training with Personal Ques & Ans

 # Make a tutorial for slides example
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

conversation = [
    "Hello",
    "What's up?",
    "Not much, what about yourself?",
    "Getting ready to grab a byte to eat."
]

trainer.train(conversation)

look = [
    "Weather in Demorest",
    "search('Weather in Demorest')",
    "What is the best place to eat in Gainesville",
    "search('What is the best place to eat in Gainesville')"
]

trainer.train(look)

recipe = [
    "What is today's date",
    "Today's date is",
    "breakfast recipe",
    "Here is a recipe for crepes http://allrecipes.com/recipe/basic-crepes/",
    "dessert recipe",
    "Here is a recipe for a chocolate lava cake https://www.allrecipes.com/recipe/219964/chef-johns-chocolate-lava-cake/",
    "dinner recipe",
    "Here is a recipe for a french dip http://allrecipes.com/recipe/french-dip-sandwiches/",
    "soup recipe",
    "Here is a recipe for pho https://www.inspiredtaste.net/4307/vietnamese-soup-pho/",
    "recipe",
    "Here is a recipe for mexican cornbread http://www.bettycrocker.com/recipes/mexican-cornbread/40ba409f-95f8-42aa-b20b-54bf63dc046d",
]

trainer.train(recipe)

university = [
    "Where can I go to pay my deposit?",
    "You can go to https://www.piedmont.edu/admission-aid/ to pay your deposit.",
    "Where is Piedmont?",
    "Piedmont University has two campuses. One is located in Demorest, GA and the other is in Athens, GA.",
    "Where can I find information about transfer credit?",
    "You can go here https://www.piedmont.edu/registrar/transfer-credit/ for more information on transfer credit.",
    "transfer credit",
    "You can go here https://www.piedmont.edu/registrar/transfer-credit/ for more information on transfer credit.",
    "Where can I schedule a visit?",
    "You can go here https://www.piedmont.edu/admission-aid/visit/ to schedule a visit.",
    "visit",
    "You can go here https://www.piedmont.edu/admission-aid/visit/ to schedule a visit.",
    "apply",
    "You can go here https://www.piedmont.edu/admission-aid/apply/ to apply.",
    "Where can I apply?",
    "You can go here https://www.piedmont.edu/admission-aid/apply/ to apply.",
    "When was Piedmont founded?",
    "Piedmont University was founded in 1987.",
    "How many students are at Piedmont?",
    "Piedmont University has a pool of approximately 2500 students.",
    "How many majors are there?",
    "There are over 50 majors for students to choose from. You can find out more about them here https://www.piedmont.edu/academics/",

]

trainer.train(university)

propose = [
    "Will you marry me?",
    "For you Ana, I would love to. Our wedding with be in Venice.",

]

trainer.train(propose)

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'

) 
