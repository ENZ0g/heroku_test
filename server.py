from bottle import run, route, view, static_file
import horoscope
import os
from datetime import datetime as dt


@route('/api/forecasts')
def forecasts():
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    return {
        'predictions': horoscope.generate_prophecies(6, 2)
    }


@route("/")
@view('index')
def index():
    return {'date': dt.now()}


@route("/about")
@view('about')
def index():
    pass


@route('/static/<filename>')
def send_css(filename):
    return static_file(filename, root='static')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
