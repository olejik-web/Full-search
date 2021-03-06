import sys
from pprint import pprint
from Need_Function import need_function
from io import BytesIO
import requests
from PIL import Image
toponym_to_find = input()
# object_width, object_height = int(input()), int(input())
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json",
    }
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass
json_response = response.json()
# pprint(json_response)
object_width, object_height = need_function(json_response)
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([str(object_width), str(object_height)]),
    "l": "map",
    'pt': '{},{},pmwtm1'.format(toponym_longitude, toponym_lattitude)
}
map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(
    response.content)).show()
# Москва, ул. Ак. Королева, 12
