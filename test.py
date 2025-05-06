import requests

def get_weather_data(city_name, api_key):
    # API-endpoint
    url = (f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric")
 

get_weather_data("amsterdam", )

payload = {}
headers = {}    

response = requests.get(url)

print(response)
if response.status_code == 200:
    posts = response.json()
    print(posts[0])
else:
    print(f"Er is iet misgegaan. Status code: {response.status_code}")