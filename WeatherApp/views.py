from django.shortcuts import render
import urllib.request
# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    

    if request.method == 'POST':
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=6e2194ce069a1eb9c7ec6f5ef566c239'

        city_weather = requests.get(url.format(city)).json() #we are requesting the API data and converting the JSON to Python data types
        print(city_weather) #checking the output
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'wind' : city_weather['wind']['speed'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        # return render(request, 'index.html', {'weather' : weather}) #returns the index.html template
    else:
        weather={}

    return render(request,'index.html',weather)