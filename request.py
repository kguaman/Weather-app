#request key is invalid. an account has to be made to obtain a new access key. 
# sign up to http://api.weatherstack.com to obtain the 
import requests
params = {
'access_key': 'c7136ca6c9cf56b61c94480ec83418fa',
'query': 'New York',
'units': 'f'

}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()
print(api_response)
print(api_response['current']['temperature'])
print(api_response['location']['name'])
print(api_response['current']['weather_descriptions'][0])
print(api_response['current']['feelslike'])
