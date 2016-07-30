import argparse
import requests
import webbrowser
from helpers import get_valid_string, get_int_input, check_alnum, check_in_list

ROOT_URL = "https://api.foursquare.com/v2/venues/"

parser = argparse.ArgumentParser(description="Wrapper around the foursquare API. Use it to retrieve information about\
                                 specific venues or groups of venues.")
parser.add_argument("endpoint", help="Name of the resource you want to access", choices=["categories", "trending",\
                                                                                         "explore", "search"])
parser.add_argument("client_id", help="Your Foursquare Client ID")
parser.add_argument("client_secret", help="Your Foursquare Client Secret")
args = parser.parse_args()

payload = {
    "v": 20160612,
    "m": "foursquare",
    "client_id": args.client_id,
    "client_secret": args.client_secret
}

def get_categories(payload):
    print("Fetching all categories ...")
    req  = requests.get(ROOT_URL + "categories", params=payload)
    response = req.json()
    print(response)

def search_venues(payload):

    payload['query'] = get_valid_string("1 - Please provide a search query:")
    payload['near']  = get_valid_string("2 - Please provide a location for the venues")

    radius = get_int_input("3 - Please provide a search radius in meters (up to 2000, default is 100 - Leave blank to\
 continue):", 1, 2000, 100)
    limit  = get_int_input("4 - How many results do you wish to get back ? (up to 50, default it 10 - Leave blank to\
 continue):", 1, 50, 10)
    category_id = check_alnum("5 - Please provide a category id if you have one (Leave blank to continue) \n")

    if radius: payload['radius'] = radius
    if limit: payload['limit'] = limit
    if category_id: payload['category_id'] = category_id

    venues_request = requests.get(ROOT_URL + "search", params=payload)
    print("Fetching results for %s in %s" % (payload['query'], payload['near']))
    response = venues_request.json()
    webbrowser.open(venues_request.url)

def get_trending_venues(payload):
    payload['near'] = get_valid_string('Please Provide a location')
    radius = get_int_input('Please provide a search radius (in meters - up to 2000 - default 100) Leave blank to \
 skip:', 1, 2000, 100)
    limit = get_int_input('How many search results do you wish to have returned ? (Max is 50 - Default is 10) Leave blank\
to skip', 1, 50, 10)

    if radius: payload['radius'] = radius
    if limit: payload['limit'] = limit

    trending_request = requests.get(ROOT_URL + 'trending', params=payload)
    print("Getting trending venues for %s" % (location))
    trending_venues = trending_request.json()
    webbrowser.open(trending_request.url)

def explore_venues(payload):

    payload['near'] = get_valid_string("Please provide a location")
    section = check_in_list("What section do you want us to explore ? (Food, Drinks, Coffee, Shops, Arts, Outdoors \
Sights, Trending, or Specials) - Leave blank skip", ['food', 'drinks', 'coffee', 'shops', 'arts', 'outdoors', 'sights','trending', 'specials'])
    query = get_valid_string("What do you want to explore ? Please provide a search query or leave blank to skip")
    limit = get_int_input("How many results do you wish to have returned (max 50 - default 10) leave blank to skip",\
 1, 50, 10)
    price = check_in_list("Do you want to filter by price range ? Choose between 1 and 4 (1 being the least expensive\
and 4 being the most expensive. Leave blank to skip)", [1,2,3,4])

    if section: payload['section'] = section
    if query: payload['query'] = query
    if limit: payload['limit'] = limit
    if price: payload['price'] = price

    explore_request = requests.get(ROOT_URL + 'explore', params=payload)
    print("Exploring places ...")
    explore_venues = explore_request.json()
    webbrowser.open(explore_request.url)

if __name__ == "__main__":

    if args.endpoint == "categories":
        get_categories(payload)
    elif args.endpoint == "search":
        search_venues(payload)
    elif args.endpoint == "trending":
        get_trending_venues(payload)
    elif args.endpoint == "explore":
        explore_venues(payload)










