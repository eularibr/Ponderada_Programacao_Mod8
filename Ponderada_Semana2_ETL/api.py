from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import requests
import pytz
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
brasil_timezone = pytz.timezone('America/Sao_Paulo')
def get_brasil_datetime():
    return datetime.now(brasil_timezone)
class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_ingestao = db.Column(db.DateTime, default=get_brasil_datetime)
    data_tipo = db.Column(db.String(50))
    valores = db.Column(db.String(100))
    uso = db.Column(db.String(100))
def funcao_etl():
    api_key = '7e15951f31a6f5146a44725003d8dd61'
    cidades = ['São Paulo', 'Rio de Janeiro', 'Bahia', 'Amazonas', 'Santa Catarina', 'Sergipe']
    lista_dados_climaticos = []
    for city in cidades:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            logging.error(f"Request error: {err}")
            continue
        logging.debug(f'Response status code: {response.status_code}')
        logging.debug(f'Response content: {response.json()}')
        if response.status_code == 200:
            weather_data = response.json()
            weather_data_json = json.dumps(weather_data)
            weather_entry = WeatherData(
                data_tipo='openweather',
                valores=weather_data_json,
                uso='previsao_climatica'
            )
            lista_dados_climaticos.append(weather_entry)
        else:
            return f'Erro na extração dos dados da API OpenWeather para {city}', 500
    db.session.add_all(lista_dados_climaticos)
    db.session.commit()
    return lista_dados_climaticos
from flask import render_template
@app.route('/all_weather_data', methods=['GET'])
def display_all_weather_data():
    weather_data = WeatherData.query.all()
    return render_template('all_weather_data.html', weather_data=weather_data)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)