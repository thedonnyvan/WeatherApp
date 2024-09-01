# Weather App

This is a simple command-line weather application written in Python. The app allows users to retrieve real-time weather information for any city in the world by leveraging the OpenWeatherMap API. The weather data includes temperature, weather descriptions, and more.

## Features

- Retrieve current weather information for any city worldwide.
- Displays temperature in both Celsius and Fahrenheit.
- Includes a "feels like" temperature.
- Weather description (e.g., clear sky, light rain).
- Colored text output using the `colorama` library for better readability.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/thedonnyvan/weather-app.git

2. **Navigate to weather-app**

   
3. **Install required dependencies**
   Type these commands into the terminal.
   ```bash
   pip install requests
   pip install colorama

5. **Get an OpenWeatherMap API key**
  Sign up for an account on OpenWeatherMap and generate an API key.
  Insert your API key in the get_weather() function in place of the placeholder.

## To Run the Program
  ```bash
  python weather_app.py
```
**EXAMPLE OUTPUT** 

Hello, this is the weather app. This Python program is a command-line weather
application that allows users to retrieve real-time weather information for any
city in the world. By leveraging the OpenWeatherMap API, the app fetches current weather
data, including temperature, weather descriptions, and more.

Enter City Name: London

Weather in London, GB:
Temperature: 15.00 °C, 59.00 °F
Feels Like: 14.00 °C, 57.20 °F
Description: clear sky

Type 'exit' if you would like to leave the program.
Enter City Name: exit

Thank you for using the Weather App.
****
