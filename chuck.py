from flask import jsonify
import requests
import concurrent.futures


def handle():
    id = set()
    id = set_data(id)
    
    for x in id:
        count = list(id).count(x)
        if count < 1:
            id.remove(x)   
            
    if len(id) < 25:
        id = set_data(id, len(id))    

    return jsonify(list(id))

def fetch_joke(url):
    response = requests.get(url)
    return response.json()['id']

def get_data(times):
    url = 'https://api.chucknorris.io/jokes/random'
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_joke, url) for _ in range(times)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        return results
    
def set_data(id, long = 0):
    
    while len(id) < 25:
        times = 25 - long
        results = get_data(times)
        id.update(results)
    
    return id