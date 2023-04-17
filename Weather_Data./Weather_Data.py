from flask import Flask, request, redirect, session
import requests, json, datetime


import os
my_secret = os.environ['API_KEY']


app = Flask(__name__)

@app.route('/')
def index():
    page = """  

    <h1>Weather Around the World</h1>
    <form method = "post" action = "/getWeather">
        <p>Zipcode: <input type = "text" name = "zipcode" required></p>
        <p><button type = "submit">Go</button></p>
      </form>

    """
    return page

  
@app.route('/getWeather', methods=["POST"])
def getWeather():

  form = request.form
  zip = form["zipcode"]

  url = f"""https://api.openweathermap.org/data/2.5/weather?zip={zip},us&appid={my_secret}"""

  result = requests.get(url)
  weather = result.json()
  print(json.dumps(weather, indent = 5))

  page = ""
  response_code = weather["cod"]
  if response_code != 200:
   page += "Error: Could not get to the API. :( "
  else: 
    desc = weather["weather"][0]["description"].title()
    city_name = weather["name"]
    temp = weather["main"]["temp"]
  
    page += f"""City Name: {city_name}\nWeather: {desc}\nCurrent Temperature: {temp}F"""
    
  return page
  
app.run(host='0.0.0.0', port=81)

