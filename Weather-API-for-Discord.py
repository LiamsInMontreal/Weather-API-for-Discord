## Hello, and thank you for using the Weather API for Discord!
import discord
from discord.ext import commands
from discord import app_commands
import requests
from geopy.geocoders import Nominatim

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

US_BASE_URL = "https://api.weather.gov/points/"


def get_lat_lon_from_zip(zip_code):
    geolocator = Nominatim(user_agent="weather_bot")
    location = geolocator.geocode(f"{zip_code}, USA")
    if location:
        return location.latitude, location.longitude
    return None, None


def get_us_weather(zip_code):
    lat, lon = get_lat_lon_from_zip(zip_code)
    if lat is None or lon is None:
        return "Could not find the location for the given ZIP code."
    
    url = f"{US_BASE_URL}{lat},{lon}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_url = data['properties']['forecast']
        forecast_response = requests.get(forecast_url)
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
            periods = forecast_data['properties']['periods']
            forecast_messages = []

            for period in periods[:5]:  # Get next 5 periods (you can change this)
                forecast_messages.append(f"{period['name']}: {period['detailedForecast']}")
            
            return "\n".join(forecast_messages)
        else:
            return "Could not retrieve forecast data."
    else:
        return "Invalid location for US weather."

def get_ca_weather(city):
    API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"The current temperature in {city} is {temperature}°C with {description}."
    else:
        return "Could not retrieve weather data for Canada."

@bot.tree.command(name="us_weather", description="Get the weather for a US location by ZIP code")
@app_commands.describe(zip_code="The ZIP code of the location to get weather for")
async def us_weather(interaction: discord.Interaction, zip_code: str):
    weather_info = get_us_weather(zip_code)
    await interaction.response.send_message(weather_info)

@bot.tree.command(name="ca_weather", description="Get the weather for a Canadian city")
@app_commands.describe(city="The name of the Canadian city to get weather for")
async def ca_weather(interaction: discord.Interaction, city: str):
    weather_info = get_ca_weather(city)
    await interaction.response.send_message(weather_info)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user}')

# Please put your bot token down here. Instructions are found in the [Github MD File]()
bot.run('YOUR_DISCORD_BOT_TOKEN')

