import json
import random
import string
from urllib.parse import urlparse
from collections import Counter
        
# A function which return's the dictionary/hashmap within the file          
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data
    
# A function that generate's a random 11 ASCII characters            
def get_hash(url):
    ascii_chars = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(ascii_chars, k=11))
    return random_string

# A function that check if the URL is valid
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
            
def shorten_url(identifier):
    return "https://pem.com/" + str(identifier)

# calling the function which creates a file
create_file()

# making a sentinel value which we will use in our while loop
sentinel_value = "a";


#making a while loop to make the program keep on running until the user enter's q later on
while sentinel_value != "q":
    
    #asking the user what type of link they want to input
    url_input = input("What type of link are you going to input(Input l for Long Url | Input s for Short Url): ").upper()

    # if the user input's any other character except l or s, inform the user they made a mistake and press l or s.
    if url_input != "S" and url_input != "L":
        while url_input != "S" and url_input != "L":
            url_input = input("You did not input l or s. Please Input l for Long Url or s for Short Url: ").upper()
            
    

    #if the user enter's l, run the code for the long url
    if url_input == 'L':
        #ask the user input a long url
        original_url = input("Enter a long url: ")
        
        #loading all the data of the file in data variable    
        data = get_data()
        
        #checking if the url is valid or not, if it's not, ask the user input a valid url
        if not is_valid_url(original_url):
            while not is_valid_url(original_url):
                original_url = input("Please enter a valid url: ")
            
        #checking if the url is already in the file, if it is, inform the user that the Long URL has already been converted.        
        if original_url in data.values():
                print("This Long Url has already been converted into a short URL")
        #if the url is not in the file, give the url a unique identifier and store it in the file as well as print out the shortened url.
        else:
            with open('data.json', 'w') as file:
                identifier = get_hash(original_url)
                data[identifier] =  original_url
                json.dump(data, file)
                print("The shortened version is", shorten_url(identifier))
    
    
    #if there is 1 or 0 url provided up till now, print url instead of urls
    if len(get_data()) == 1 or len(get_data()) == 0:
        print("There have been", len(get_data()), "url shortened so far")
    #if there are more than 1 url, start writing it as urls    
    else:
        print("There have been", len(get_data()), "urls shortened so far")
            

    #printing everything inside the file right now
    print("Here is everything inside the file right now: ", get_data())
    #changing the sentinel value by asking the user if he want's to quit so that the while loop does not run forever
    sentinel_value = input("If you would like to quit press q, if you want to keep using the application press any other key: ")
#Thanking the user for using our application    
print("Thank you for using our application!")



            


