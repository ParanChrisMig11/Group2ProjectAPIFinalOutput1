#Importing the required modules for URL encoding and making HTTP requests
import urllib.parse #For encoding URL parameters
import requests #For sending HTTP requests and handling response

#Define the base API endpoint for the MapQuest Directions API
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG" #API key for authenticating requests to the MapQuest API

#Starting an infinite loop to allow the user to make multiple API requests
while True:
    orig = input ("Starting Location: ") #Prompting the user to input the starting location
    #Checking if the user wants to quit the program
    if orig == "quit" or orig == "q":  #Case-insensitive quit command
        break
    #Prompting the user to input the destination location
    dest = input ("Destination: ")
    #Checking if the user wants to quit the program
    if dest == "quit" or dest == "q": #Case-insensitive quit command
        break
    #Constructing the full API request URL with the origin, destination, and API key
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    json_data = requests.get(url).json() #Sending a GET request to the API and parsing the JSON response
    
    #Displaying the constructed URL for debugging purposes
    print("URL:" + (url))
    
    #Extracting the status code from the JSON response to check the API call's result
    json_status = json_data["info"]["statuscode"]
    
    #Checking if the API call was successful
    if json_status == 0:
        #A status code of 0 indicates a successful API response
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        #Further processing of successful responses (e.g., display route details) could be added here

 