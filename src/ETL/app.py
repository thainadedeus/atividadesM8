import requests
import datetime
import pprint
from datetime import datetime
from pymongo import MongoClient

class WeatherETL:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["etl_db"]
        self.collection = self.db["weather_data"]

    def get_openweather_data(self, city):
        url = "http://api.openweathermap.org/data/2.5/weather"
        api_key = "ed69a7ed3a90d9d0190bd94758dd11af"
        params = {
            "q": city,
            "appid": api_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Falha ao obter dados para {city}. Código de status:", response.status_code)
            return None

    def etl_to_mongodb(self, data, city):
        uso = self.determine_usage(data)
        document = {
            "Data da Ingestão": datetime.now(),
            "Cidade": city,
            "Tipo": "Condições Meteorológicas",
            "Valores": data,
            "Uso": uso
        }
        result = self.collection.insert_one(document)
        print(f"Documento inserido com o ID: {result.inserted_id}")

    def determine_usage(self, data):
        if data['main']['temp'] > 25:
            return "Clima Quente"
        else:
            return "Clima Moderado"

if __name__ == "__main__":
    etl_processor = WeatherETL()
    cidades_brasileiras = ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza", "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre"]

    for cidade in cidades_brasileiras:
        data = etl_processor.get_openweather_data(cidade)
        if data:
            etl_processor.etl_to_mongodb(data, cidade)
