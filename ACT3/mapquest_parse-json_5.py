#Importing necessary modules for URL handling and HTTP requests
import urllib.parse #For encoding URL query parameters
import requests #For making HTTP requests and handling API responses

#Base URL for the MapQuest Directions API
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "o55GazRbzQcs1OXr2yg2MsAbHiWAxWJG" #API key for authenticating requests to the MapQuest API

#Infinite loop to repeatedly prompt the user for inputs
while True:
    orig = input("Starting Location: ") #Prompt the user for the starting location
    #Allow the user to exit the program by typing 'quit' or 'q'
    if orig == "quit" or orig == "q": #Case-insensitive check
        break
    
    #Prompt the user for the destination location
    dest = input("Destination: ")
    if dest == "quit" or orig == "q": #Case-insensitive check
        break
    
    #Construct the complete API request URL with the origin, destination, and API key
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json() #Send a GET request to the MapQuest API and parse the response as JSON
    
    #Display the constructed URL for debugging and verification
    print("URL: " + url)
    
    #Extract the status code from the API response to determine if the request was successful
    json_status = json_data["info"]["statuscode"]
    
    #Handle a successful API response (status code 0)
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        #Display the route details
        print("=============================================")
        print("Directions from " + orig + " to " + dest)
        print("Trip Duration:   " + json_data["route"]["formattedTime"])  #Travel time in hh:mm:ss format
        print("Miles:           " + str(json_data["route"]["distance"])) #Distance in miles
        #Convert and display the distance in kilometers
        print("Kilometers:      " + str("{:.2f}".format(json_data["route"]["distance"] * 1.61)))

        # Check if 'fuelUsed' exists in the response
        if "fuelUsed" in json_data["route"]:
            print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
            #Convert and display the fuel usage in liters
            print("Fuel Used (Ltr): " + str("{:.2f}".format(json_data["route"]["fuelUsed"] * 3.78)))
        else:
            print("Fuel Used data not available.")  #Handle cases where fuel data is not provided

        print("=============================================")
    else:
        #Handle errors by displaying messages provided by the API
        print("Error: " + str(json_data["info"]["messages"]))

        

 