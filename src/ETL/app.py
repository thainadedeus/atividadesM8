from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
import requests
import datetime

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'etl_db',  
    'host': 'localhost',  
    'port': 27017,  
}

db = MongoEngine(app)

class WeatherData(db.Document):
    ingestion_date = db.DateTimeField(default=datetime.datetime.utcnow)
    weather_type = db.StringField(max_length=255)
    values = db.StringField(max_length=255)
    usage = db.StringField(max_length=255)


@app.route('/etl')
def etl():
    weather_data = get_openweather_data()
    transformed_data = transform_data(weather_data)
    load_data(transformed_data)
    
    return jsonify({'message': 'ETL completa'})

def get_openweather_data():
    api_key = '16fc3a8a132ce0a1419aa5a3a6c9b66d'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q=CITY&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def transform_data(data):
    weather_type = data['weather'][0]['main']
    values = data['main']['temp']
    usage = 'exemplo'
    
    return {
        'weather_type': weather_type,
        'values': values,
        'usage': usage
    }

def load_data(data):
    new_data = WeatherData(
        ingestion_date=data['ingestion_date'],
        weather_type=data['weather_type'],
        values=data['values'],
        usage=data['usage']
    )
    new_data.save()


if __name__ == '__main__':
    app.run(debug=True)
