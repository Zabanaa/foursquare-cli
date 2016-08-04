Foursquare API Wrapper
=======================

The Foursquare API wrapper is a command line tool that allows users to interact with
Foursquare's API.
It can be used to return information about venues or groups of venues,
(namely categories, trending and recommended venues.)
It is also possible to perform a search using keywords.

This is my first attempt at creating a python package so it is still under heavy
development. Revisions will be made continually to improve the tool and its efficiency.

If you come across this package and would like to contribute, please feel free to initiate
a PR, which I will happily accept as it will help me to learn more about the intricacies of package/module creation.

----

General Usage
=============

To use the Foursquare API Wrapper, you first have to register an application on
Foursquare's developers site. You will be given two keys: a client_id and a client_secret.
You will need those to be able to make calls to the API.

After installing the package you can use it like so:

fsq-wrapper <endpoint> <clientid> <client_secret> 

Endpoint (Positional Argument) 

The nature of the request. As of present date, 4 types of endpoints are accepted:
categories, search, trending and explore

Client Id (Positional Argument)
The client id given to you by foursquare's development platform (can be found in the
dashboard)

Client Secret (Positional Argument) 
Same as above


Endpoints
=========
Categories => Will return all venue categories currently supported by the API
Search => Lets you make a search for venues on the basis of keywords and location
Trending => Will return a list of trending venues based on the location you provide
Explore => Will return a list of recommended venues near the provided location

