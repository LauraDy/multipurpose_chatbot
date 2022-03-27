from chatbot import chatbot
from flask import Flask, render_template, request, url_for
from chatterbot.trainers import ChatterBotCorpusTrainer
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import emojis

### Chat initialize
##model = load_model("chatbot_model.h5")
##intents = json.loads(open("intents.json").read())
##words = pickle.load(open("words.pkl", "rb"))
##classes = pickle.load(open("classes.pkl", "rb"))


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
# emojis:
    sunny = emojis.encode(':sunny:')
    partlysun = emojis.encode(':partly_sunny:')
    cloudy = emojis.encode(':cloud:')
    storm = emojis.encode(':cloud_with_lightning:')
    rain = emojis.encode(':umbrella:')
    snow = emojis.encode(':snowflake:')
    if "Mostly sunny" in info:
        info = partlysun + info
    elif "sunny" in info:
        info = sunny + info
    elif "cloud" in info:
        info = cloudy + info
    elif "storm" in info:
        info = storm + info
    elif "rain" in info:
        info = rain + info
    elif "snow" in info:
        info = snow + info
    print(f"The weather in {location} is {info} at {weather}")

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    #return render_template("index_home.html")
    return render_template("home_index.html")

@app.route('/personal') 
def personal(): 
    return render_template("index_per.html")

@app.route('/uni') 
def uni(): 
    return render_template("index_uni.html")

# Teach people how to search/code to search google
# use emojis in weather searching

@app.route("/get")
def get_bot_response():
##    userText = request.args.get('msg')
##    return str(chatbot.get_response(userText))
    
##    msg = request.form["msg"]
##    if msg.startswith('my name is'):
##        name = msg[11:]
##        ints = predict_class(msg, model)
##        res1 = getResponse(ints, intents)
##        res =res1.replace("{n}",name)
##    elif msg.startswith('hi my name is'):
##        name = msg[14:]
##        ints = predict_class(msg, model)
##        res1 = getResponse(ints, intents)
##        res =res1.replace("{n}",name)
##    else:
##        ints = predict_class(msg, model)
##        res = getResponse(ints, intents)
##    return res
    userText = request.args.get('msg')
##    with open('conversations.yml') as file:
##        contents1 = file.read()
##    with open('assistant.yml') as file:
##        contents2 = file.read()
##    with open('university.yml') as file:
##        contents2 = file.read()
    ##    search_word = input("enter a word you want to search in file: ")
    ##    if search_word in contents:
    ##        print ('word found')
    ##    else:
    ##        print ('word not found')
    if "weather" in userText:
        city = 'Demorest'
        return weather(city)
    elif "search" in userText:
        return next(search(userText))
##    elif "weather in" in userText:
##        return next(search("weather"))
        #return str(chatbot.get_response(search("userText")))
##    elif "what" or "where" or "when" or "how" or "why" in userText:
##        return next(search(userText))
    else:
        return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run() 

# url = nex(x)
# print(f"<a ref='{url}'>{url}</a>")
