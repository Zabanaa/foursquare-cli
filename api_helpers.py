import requests
import webbrowser

def make_request(endpoint, data):
    url = "https://api.foursquare.com/v2/venues/" + endpoint
    request = requests.get(url, params=data)
    return request

def show_results(request):
    url = request.url
    return webbrowser.open(url)

def display_results(request):
    # pretty print the json
    response = request.json()
    print(response)

