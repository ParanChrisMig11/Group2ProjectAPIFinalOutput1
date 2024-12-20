#Importing the required modules for URL encoding and making HTTP requests
import urllib.parse #For encoding URL parameters
import requests #For sending HTTP requests and handling response

#Setting the origin and destination locations
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG" #API key for authenticating the MapQuest API request

#Loop to repeatedly prompt the user for starting and destination locations
while True:
    orig = input ("Starting Location: ") #User inputs the origin
    dest = input ("Destination: ") #User inputs the destination

    #Constructing the complete URL with query parameters
    #The "urllib.parse.urlencode" safely encodes parameters for a valid URL
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    json_data = requests.get(url).json() #Sending a GET request to the API and parsing the response into JSON format
    
    #Displaying the constructed URL for debugging or verification purposes
    print("URL: " + (url))
    #The "info" section contains the "statuscode" that indicates the result of the API call
    json_status = json_data["info"]["statuscode"]
    
    #Handling successful API responses
    if json_status == 0:
        # Status code 0 indicates a successful API call
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        # Additional logic to display route details could be added here (e.g., distance, time, etc.)

 