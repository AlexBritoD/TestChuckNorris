from flask import jsonify
import requests

def handle():
    url='https://api.chucknorris.io/jokes/random'
    id = set()
    while len(id) < 25:
        response = requests.get(url)
        id.add(response.json()['id'])
    return jsonify(list(id))

