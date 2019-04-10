from bottle import run, route, view, static_file, response
import horoscope
import os
from datetime import datetime as dt


@route('/api/forecasts')
def forecasts():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return {
        'predictions': horoscope.generate_prophecies(6, 2)
    }


@route("/")
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


@route("/about")
@view('about')
def about():
    return {'test': 3}


@route('/static/<filename>')
def send_css(filename):
    return static_file(filename, root='static')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
