import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Weather Finder",
    page_icon="☁️"
)

st.title("☁️ Weather Finder")
st.write("Check the 5-day weather forecast for any city.")

city = st.text_input("Enter City")

if st.button("Get Forecast"):

    try:
        location = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 10,
                "format": "json"
            }
        ).json()

        if not location.get("results"):
            st.error("City not found.")
            st.stop()

        place = location["results"][0]

        # Find exact city name
        for p in location["results"]:
            if p["name"].lower() == city.lower():
                place = p
                break

        result = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": place["latitude"],
                "longitude": place["longitude"],
                "daily": "temperature_2m_max,temperature_2m_min",
                "forecast_days": 5,
                "timezone": "auto"
            }
        ).json()

        daily = result["daily"]

        st.success(
            f"📍 {place['name']}, {place.get('country', '')}"
        )

        st.subheader("Today's Weather")

        c1, c2 = st.columns(2)

        c1.metric(
            "Maximum",
            f"{daily['temperature_2m_max'][0]} °C"
        )

        c2.metric(
            "Minimum",
            f"{daily['temperature_2m_min'][0]} °C"
        )

        st.subheader("5-Day Forecast")

        data = pd.DataFrame({
            "Date": daily["time"],
            "Max °C": daily["temperature_2m_max"],
            "Min °C": daily["temperature_2m_min"]
        })

        st.dataframe(
            data,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Temperature Trend")

        st.line_chart(
            data.set_index("Date")
        )

    except Exception:
        st.error("Unable to get weather data.")