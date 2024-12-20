#Importing the required modules for URL encoding and making HTTP requests
import urllib.parse #For encoding URL parameters
import requests #For sending HTTP requests and handling response

#Setting the origin and destination locations
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C." #Starting location
dest = "Baltimore, Md" #Ending location
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG" #API key for authenticating the MapQuest API request

#Constructing the complete URL with query parameters
#The "urllib.parse.urlencode" safely encodes parameters for a valid URL
url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
json_data = requests.get(url).json() #Sending a GET request to the constructed URL and parsing the JSON response

#Displaying the complete URL for debugging and verification
print("URL: " + (url))

#Extracting the status code from the JSON response
#The "info" field contains a "statuscode" that indicates the API call's success or failure
json_status = json_data["info"]["statuscode"]

#Checking if the API call was successful (status code 0 indicates success)
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    #Additional successful call details could be added here (e.g., route information)

 