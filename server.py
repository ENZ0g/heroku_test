from bottle import Bottle, run, view, static_file, request
from truckpad.bottle.cors import CorsPlugin, enable_cors
import telebot
import horoscope
import os
from datetime import datetime as dt
import requests


app = Bottle()

TOKEN = os.environ.get('TOKEN')
CHAT_ID = int(os.environ.get('CHAT_ID'))
API_KEY = os.environ.get('API_KEY')

bot = telebot.TeleBot(TOKEN)


@enable_cors
@app.route('/activity')
def detect_client():
    ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    location = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}&fields=city, isp, organization')
    bot.send_message(CHAT_ID, 'New activity from:')
    bot.send_message(CHAT_ID, f"REFERER: {request.headers.get('Referer', 'direct_access')}")
    bot.send_message(CHAT_ID, f"ORIGIN: {request.headers.get('Origin', 'no_origin')}")
    bot.send_message(CHAT_ID, f"IP: {ip}")
    bot.send_message(CHAT_ID, f"CITY: {location['city']}")
    bot.send_message(CHAT_ID, f"ISP: {location['isp']}")
    bot.send_message(CHAT_ID, f"ORGANIZATION: {location['organization']}")
    bot.send_message(CHAT_ID, f"USER_AGENT: {request.headers.get('User-Agent')}")
    

@app.route('/api/forecasts')
def forecasts():
    return {
        'predictions': horoscope.generate_prophecies(6, 2)
    }


@app.route("/")
@view('index')
def index():
    month = ['*',
             'января',
             'февраля',
             'марта',
             'апреля',
             'мая',
             'июня',
             'июля',
             'августа',
             'сентября',
             'октября',
             'ноября',
             'декабря']
    return {'day': dt.now().day,
            'month': month[dt.now().month],
            'year': dt.now().year}


@app.route("/about")
@view('about')
def about():
    return {'test': 3}


@app.route('/static/<filename>')
def send_css(filename):
    return static_file(filename, root='static')

                                                  
app.install(CorsPlugin(origins=['https://enz0g.github.io']))                                                  

if os.environ.get('APP_LOCATION') == 'heroku':
    run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(app, host='localhost', port=8080)
