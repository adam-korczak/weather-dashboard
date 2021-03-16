import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods = ['POST'])
def render_results():
    zip_code = request.form['zipCode']
    return "Zip Code: " + zip_code

if __name__ == '__main__':
    app.run()

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(zip_code, api_key):
    api_url = "http://api.openweathermap.org" \
         " data/2.5/weather?zip={}&appid={}".format(zip_code, api_key)
    r = request.get(api_url)
    return r.json()

#print(get_weather_results("07009",get_api_key()))
