import requests # To retrieve data from OpenWeatherMap API
from colorama import Fore, Style, init # Colorama will add color to the ouputed text

init(autoreset=True) #Resets the color to default after prints

def get_weather(city):
    city = city.title()
    api_key = '805f4916c9513cba2459b53436b91995' #Insert your own OpenWeatherMap API

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url) # Sends a GET request to the OpenWeatherMap API

    if response.status_code == 200: # Checks if request was successful
        data = response.json() # Parse the JSON data returned by the API
        
        country = data['sys']['country']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15 # Kelvin to celcius conversion
        temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32 # Kelvin to fahrenheit conversion
        temp_feels_like = data['main']['feels_like']
        temp_feels_like_f = (temp_feels_like - 273.15) * 9/5 + 32 # Kelvin to fahrenheit conversion
        temp_feels_like_c = temp_feels_like - 273.15 # Kelvin to celcius conversion
        desc = data['weather'][0]['description']
        
        return city, country, temp_celsius, temp_fahrenheit, temp_feels_like_c, temp_feels_like_f, desc
    else:
        print(Fore.RED + '\nError: Cannot Fetch Weather Data or City Name Was Spelled Incorrectly')
        return None
    
def main():
    print(Fore.YELLOW + "Hello, this is the weather app. This Python program is a command-line weather \napplication that allows users to retrieve real-time weather information for any \ncity in the world. By leveraging the OpenWeatherMap API, the app fetches current weather \ndata, including temperature, weather descriptions, and more.\n")
    city = input("Enter City Name: ")

    while city.lower() != "exit":
        weather_info = get_weather(city) #Retreives weather information
        
        if weather_info:
            city, country, temp_celsius, temp_fahrenheit, temp_feels_like_c, temp_feels_like_f, desc = weather_info
            print(Fore.LIGHTCYAN_EX + f'\nWeather in {city}, {country}:')
            print(Fore.LIGHTCYAN_EX + f'Temperature: {temp_celsius:.2f} °C, {temp_fahrenheit:.2f} °F')
            print(Fore.LIGHTCYAN_EX + f'Feels Like: {temp_feels_like_f:.2f} °C, {temp_feels_like_f:.2f} °F')
            print(Fore.LIGHTCYAN_EX + f'Description: {desc}') 
            
        print("\nType 'exit' if you would like to leave the program.\n")
        city = input("Enter City Name: ")
        
    print(Fore.GREEN + "Thank you for using the Weather App.")

if __name__ == "__main__":
    main()