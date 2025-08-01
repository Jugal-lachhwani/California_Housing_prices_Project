import streamlit as st
import requests

st.title("California Housing Price Predictor")

# Input fields
longitude = st.number_input("Longitude", value=-122.0)
latitude = st.number_input("Latitude", value=37.0)
housing_median_age = st.number_input("Housing Median Age", value=20)
total_rooms = st.number_input("Total Rooms", value=1000)
total_bedrooms = st.number_input("Total Bedrooms", value=200)
population = st.number_input("Population", value=850)
households = st.number_input("Households", value=300)
median_income = st.number_input("Median Income", value=3.5)

ocean_proximity = st.selectbox("Ocean Proximity", [
    "INLAND", "NEAR OCEAN", "NEAR BAY", "<1H OCEAN", "ISLAND"
])

# Prediction button
if st.button("Predict"):
    payload = {
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()

        if response.status_code == 200 and "prediction" in result:
            st.success(f"Predicted Median House Value: {result['prediction'][0]:,.2f}")
        else:
            st.error(f"Error: {result.get('error', 'Unknown error')}")
            st.text(result.get('trace', 'No traceback'))

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
