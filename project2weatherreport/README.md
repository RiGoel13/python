#  Weather Fetcher with Voice Output

This Python script retrieves real-time weather information for a specified city from the **WeatherAPI** and speaks out the temperature in Celsius and Fahrenheit using text-to-speech functionality.

## Features

- Retrieves weather information from the **WeatherAPI**.
- Outputs the current temperature in **Celsius** and **Fahrenheit**.
- Speaks out the temperature using text-to-speech.

## Requirements

- Python 
- `requests` library to make API calls.
- `win32com.client` library to provide text-to-speech support.
- A **WeatherAPI** key (obtain one by signing up on [WeatherAPI](https://www.weatherapi.com/)).

### Install Dependencies

```bash
pip install requests pywin32
```


##  How to Run

```bash
python weather_fetcher.py
```

### Example Output

```bash
Enter city: London
temperature in celsius:
15

temperature in fahrenheit:
59
```

Also, the temperature will be read out by your system.

### Error Handling

In case the city name is invalid or the data cannot be retrieved, an error message will be shown, and the problem will be logged.

```bash
Error fetching weather data:
API error message here
```

## How It Works

1. The script asks for a city name.
2. It makes a request to the **WeatherAPI** to retrieve current weather data.
3. Both the temperature is printed in **Celsius** and **Fahrenheit**.
4. The temperature is subsequently read aloud by **text-to-speech**.

## Functions

- **requests.get(url)**: Retrieves the weather data from WeatherAPI.
- **win.Dispatch("SAPI.Spvoice")**: Uses text-to-speech to speak out the temperature.
  
