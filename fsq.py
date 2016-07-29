import argparse
import requests
import webbrowser
from helpers import get_valid_string, get_int_input, check_alnum

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

    location = input("Please provide a location\n")
    while not all(c.isalpha() or c.isspace() or c == ',' for c in location) or not location:
        print("This is a required field, please provide a correct location \n")
        location = input("Please provide a location \n")

    section = input("What section do you want us to explore ? (Food, Drinks, Coffee, Shops, Arts, Outdoors \
Sights, Trending, or Specials) \n")
    section_list = ['food', 'drinks', 'coffee', 'shops', 'arts', 'outdoors', 'sights','trending', 'specials']
    while section and section.lower() not in section_list:
        print("Incorrect section. Please select one from the list above\n")
        section = input("What section do you want us to explore ? Leave blank to skip\n")

    query = input("What do you want to explore ? Please provide a search query or leave blank to skip\n")
    while query and not all(c.isalpha() or c.isspace() for c in query):
        print("Incorrect query, please provide a valid one\n")
        query = input("What do you want to explore ?\n")

    limit = input("How many results do you wish to have returned (max 50 - default 10) leave blank to skip\n")
    while limit and int(limit) not in range(1, 51):
        print("The maximum number of results is 50. Please provide a number within that range\n")
        limit = print("How many results do you wish to have returned ? Leave blank to skip\n")

    price = input("Do you want to filter by price range ? Choose between 1 and 4 (1 being the least expensive\
and 4 being the most expensive. Leave blank to skip\n)")
    while price and int(price) not in range(1,5):
        print("Invalid price range\n")
        price = input("Choose a valid price range\n")

    payload['near'] = location
    if section: payload['section'] = section
    if query: payload['query'] = query
    if limit: payload['limit'] = int(limit)
    if price: payload['price'] = int(price)

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










