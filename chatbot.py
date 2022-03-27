from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from googlesearch import search

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

# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'

) 
