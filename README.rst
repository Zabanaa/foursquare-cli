Foursquare API Wrapper
=======================

The Foursquare API wrapper is a command line tool that allows users to interact with
Foursquare's API. It can be used to return information about venues or groups of venues,
namely categories, trending and recommended venues. It is also possible to perform a
search using keywords as a search query.

It is my first attempt at creating a python package so it is still under heavy
development. Revisions will be made continually to improve the tool and its efficiency.

If you come across this package and would like to contribute, please feel free to initiate
a PR, which I will happily accept as I want to learn more about the intricacies of
creating packages and modules.

----

General Usage
==

After installing the package you can call it like so:

fsq-wrapper <endpoint> <clientid> <client_secret> 

To get your client_id and client_secret keys you have to create an account on foursquare's
development platform. You will then be able to access your keys from the dashboard.

Endpoint: The nature of the request - As of present, you can fetch the categories, make a
search based on a search query, get trending venues or explore venues.

Categories => Will return all venue categories currently supported by the API
Search => Let's you make a search for venues based on keywords
Trending => Will return a list of trending venues based on the location you provide
Explore => Will return a list of recommended venues near the provided location
