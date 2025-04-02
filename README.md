# Weather Bot

This is a Discord bot that provides weather information for US locations by ZIP code and Canadian cities by name. The bot uses the [Weather.gov API](https://www.weather.gov/documentation/services-web-api) for US weather forecasts and the [OpenWeatherMap API](https://openweathermap.org/api) for Canadian weather forecasts.

## Features

- Get weather forecast for a US location by ZIP Code.
- Get weather forecast for a Canadian city by Postal Code.

## Prerequisites

- Python 3.7+
- Discord bot token
- OpenWeatherMap API key

## Installation

1. Download the repository by clicking Code and Download Zip.

2. Open a CMD prompt and install the required packages:
  ```py -m pip install requests discord.py geopy```

3. Go to the [Discord Development Portal, log on, and create a new application if needed](https://discord.com/developers/applications)

4. Once you have opened or created an application, click on the bot section, set up a bot if needed, and create a token.

5. Log onto the OpenWeatherMap website and [create an API key.](https://openweathermap.org/faq)
    
6. Replace the placeholder values with your actual Discord bot token and OpenWeatherMap API key in the code:
   ```
    bot.run('YOUR_DISCORD_BOT_TOKEN')
    API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
    ```

## Usage

Run the bot by running:
```
py Weather-API-for-Discord.py
``` 
in the directory of the script.

## Commands

### US Weather

Get the weather for a US location by ZIP code:
```
/us_weather ZIP_CODE
```

- **zip_code:** The ZIP code of the location to get weather for.

Example:
```
/us_weather 90210
```

### Canadian Weather

Get the weather forecast for a Canadian city (next 5 periods):
```
/ca_weather CITY_NAME
```

- **city:** The name of the Canadian city to get weather for.

Example:
```
/ca_weather Montreal
```

That is all, thank you for using this and thank you for reading down to the bottom!
