import pytest
import responses
from api import app, db, WeatherData
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.session.remove()
        db.drop_all()
@responses.activate
def test_etl_route(client):
    responses.add(responses.GET, 'https://api.openweathermap.org/data/2.5/weather',
                 json={'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]},
                 status=200)
    response = client.get('/')
    assert response.status_code == 200
    assert 'Dados extraídos e armazenados no banco de dados' in response.data.decode()
    assert WeatherData.query.count() == 3
def test_all_weather_data_route(client):
    response = client.get('/all_weather_data')
    assert response.status_code == 200
    assert 'All Weather Data' in response.data.decode()