import json

url_input = input("Enter what you want to do? (o for original, s for short)");


count = 0;


def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data
    # return {}

def get_hash(url):
    return str(int(hash(original_url)) % 10**11)

def shorten_url(url):
    return "https://pem.com/" + str(get_hash(url))


if url_input == 'o':
    original_url = input("Enter a long url")
    
    data = get_data()
    
    with open('data.json', 'w') as file:
        data[get_hash(original_url)] =  original_url
        json.dump(data, file)
    print("The shortened version is", shorten_url(original_url))

if url_input == 's':
    short_url = input("Enter a short url")
    
    hash_value = short_url.split("https://pem.com/")[1]
    
    data = get_data()
    
    print("the original link is: ",data[hash_value])

#print (shorten_url(url_input))
print(get_data())



    


