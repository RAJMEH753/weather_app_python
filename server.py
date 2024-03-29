from flask import Flask, render_template, request, abort

# import json to load json data to python dictionary
import json

# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)
def tocelcius(temp):
    return str(round(float(temp) - 273.16,2))

@app.route('/', methods=['POST','GET'])
def weather():
    api_key = 'f327a81a2a120fd158a88e9528340ec5'
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name mathura
        city = 'Delhi'

    # source contain json data from api
    try:
        weather_api = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api_key).read()
    except:
        return abort(404)
    
    # converting json data to dictionary
    list_of_data = json.loads(weather_api)
    # wallpaper = urllib.request.urlopen('https://source.unsplash.com/1600x900/?' + city ).read()

    # data for variable list_of_data
    data = {
        "temp_cel": str(list_of_data['main']['temp']) + '°C',
        "humidity": str(list_of_data['main']['humidity']),
        "wind": str(list_of_data['wind']['speed']),
        "cityname":str(city).capitalize(),
        "status": str(list_of_data["weather"][0]["description"]).capitalize(),
        "icon": str('https://openweathermap.org/img/wn/' + list_of_data["weather"][0]["icon"] + '.png'),
        "wall": str('https://source.unsplash.com/1600x900/?' + city),
    }
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
