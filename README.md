# Weather App

A simple desktop weather application built with **PyQt5** and the **OpenWeatherMap API**. Enter a city name and instantly get the current temperature, a weather description, and a matching emoji.

## Features

- Clean, minimal GUI built with PyQt5
- Real-time weather data from the OpenWeatherMap API
- Temperature displayed in Celsius
- Weather condition shown as text + emoji (☀ 🌧 ⛈ ❄ 🌫 and more)
- Sound cue (beep) when fetching weather
- Handles common errors gracefully (invalid city, bad connection, timeout, server errors, etc.)

## Tech Stack

- Python 3
- [PyQt5](https://pypi.org/project/PyQt5/) — GUI framework
- [requests](https://pypi.org/project/requests/) — HTTP requests to the API
- [python-dotenv](https://pypi.org/project/python-dotenv/) — loads API key from a `.env` file
- [OpenWeatherMap API](https://openweathermap.org/api) — weather data source

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ajaoobafemi/Weather-App.git
cd Weather-App
```

### 2. Install dependencies

```bash
pip install PyQt5 requests python-dotenv
```

### 3. Get an OpenWeatherMap API key

Sign up for a free account at [openweathermap.org](https://home.openweathermap.org/users/sign_up) and generate an API key from your account dashboard.

### 4. Create a `.env` file

In the project root, create a file named `.env` and add your key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

> **Note:** New OpenWeatherMap keys can take a few minutes to activate.

The `.env` file is already excluded from version control via `.gitignore`, so your key stays private.

### 5. Run the app

```bash
python weather.py
```

## Usage

1. Launch the app
2. Type a city name into the input field
3. Click **Get Weather**
4. View the current temperature, condition, and emoji for that city

## Project Structure

```
Weather-App/
├── weather.py       # Main application code
├── .env             # Your API key (not tracked by git)
├── .gitignore       # Excludes .env from version control
└── README.md
```

## Error Handling

The app displays a clear message for common issues, including:

| Status Code | Meaning |
|---|---|
| 400 | Bad request — check your input |
| 401 | Unauthorized — invalid API key |
| 403 | Forbidden — access denied |
| 404 | City not found |
| 500 | Internal server error |
| 502 | Bad gateway |
| 503 | Service unavailable |
| 504 | Gateway timeout |

Connection errors, timeouts, and too-many-redirects are also handled separately.

## License

This project is open source and available for personal or educational use.

OBAFEMI.
