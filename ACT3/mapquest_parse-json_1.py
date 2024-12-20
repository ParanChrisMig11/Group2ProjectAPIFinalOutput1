#Importing the required modules for URL encoding and making HTTP requests
import urllib.parse  #For encoding URL parameters
import requests #For sending HTTP requests and handling responses

#Define the base API endpoint for the MapQuest Directions API
main_api = "https://www.mapquestapi.com/directions/v2/route?"

#Setting the origin and destination locations
orig = "Washington, D.C." #Origin city
dest = "Baltimore, Md" #Destination city

#API key for authenticating the MapQuest API request
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG"

#Constructing the complete URL with query parameters
#The "urllib.parse.urlencode" safely encodes parameters for a valid URL
url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data = requests.get(url).json() #Sending a GET request to the constructed URL and parsing the JSON response

#Printing the JSON response (this contains the route information and other data)
print(json_data)
