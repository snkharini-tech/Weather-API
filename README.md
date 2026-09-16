
# Weather Finder

Weather Finder is a simple and user-friendly weather forecasting web application built using Python and Streamlit. It allows users to search for a city and view its 5-day weather forecast with temperature information and a simple chart.

## Live Demo :

https://weather-api-hmrhxbfrgnofp4ecktwfbg.streamlit.app/

## Features

- Search weather by city name
- Find the selected city automatically
- Display today's maximum temperature
- Display today's minimum temperature
- Show 5-day weather forecast
- Display temperature trend using a line chart
- Display forecast data in a table
- Simple and clean user interface
- No API key required

## Technologies Used

- Python
- Streamlit
- Requests
- Pandas
- Open-Meteo API

## API Used

This project uses the Open-Meteo API to retrieve location and weather forecast information.

### Geocoding API

The Geocoding API is used to search for the entered city and obtain its latitude and longitude.

### Weather Forecast API

The Weather Forecast API uses the latitude and longitude to retrieve the 5-day weather forecast.

## How It Works

1. The user enters a city name.
2. The application sends the city name to the Geocoding API.
3. The city latitude and longitude are obtained.
4. The coordinates are sent to the Weather Forecast API.
5. Weather forecast data is retrieved.
6. Today's maximum and minimum temperatures are displayed.
7. The 5-day forecast is displayed in a table.
8. A temperature trend chart is displayed.

## Workflow

User
↓
Enter City Name
↓
Streamlit Application
↓
Open-Meteo Geocoding API
↓
Latitude and Longitude
↓
Open-Meteo Weather API
↓
Weather Forecast Data
↓
Weather Dashboard

## Weather Information

The application displays:

- City Name
- Country
- Maximum Temperature
- Minimum Temperature
- 5-Day Forecast
- Temperature Trend

## Project Structure

Weather-Finder/
│
├── app.py
├── requirements.txt
└── README.md

## Installation

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_LINK

Open the project folder:

    cd Weather-Finder

Install the required libraries:

    py -m pip install -r requirements.txt

## Requirements

    streamlit
    requests
    pandas

## Run the Application

Run the following command:

    py -m streamlit run app.py

The application will open in the browser.

## Example

Enter a city name such as:

    Chennai

The application will display the selected city's weather information and 5-day forecast.

## Error Handling

The application handles common errors such as:

- City not found
- Invalid city name
- API connection error
- Weather service error

An appropriate error message is displayed when weather data cannot be retrieved.

## User Interface

The application includes:

- City search input
- Weather information cards
- 5-day forecast table
- Temperature trend chart
- Simple and clean layout

## Advantages

- Easy to use
- Simple interface
- No API key required
- Provides a 5-day forecast
- Interactive temperature chart
- Fast weather data retrieval
- Beginner-friendly project

## Future Improvements

- Add hourly weather forecast
- Add humidity and wind speed
- Add rainfall probability
- Add weather condition icons
- Add sunrise and sunset information
- Add weather alerts
- Add multiple city comparison
- Add search history
- Improve dashboard design

## Learning Outcomes

Through this project, I learned:

- How to work with REST APIs
- How to send HTTP requests using Python
- How to process JSON data
- How to use Pandas for data handling
- How to build applications using Streamlit
- How to display data using tables
- How to create charts using Streamlit
- How to handle API errors

## Conclusion

Weather Finder is a simple weather forecasting application developed using Python and Streamlit. It uses the Open-Meteo API to retrieve weather information and provides users with a 5-day forecast and temperature trend. This project demonstrates the practical use of APIs, data processing, visualization, and Streamlit application development.

