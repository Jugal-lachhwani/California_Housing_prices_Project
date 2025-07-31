from pydantic import BaseModel, Field
from typing import List, Optional
from custom_transformers import CombinedAttributesAdder
import joblib
import pandas as pd

class PredictHousePrice(BaseModel):
    longitude: float = Field(..., description="Longitude of the house location")
    latitude: float = Field(..., description="Latitude of the house location")
    housing_median_age: float = Field(..., description="Median age of the houses in the area")
    total_rooms: float = Field(..., description="Total number of rooms in the house")
    total_bedrooms: float = Field(..., description="Total number of bedrooms in the house")
    population: float = Field(..., description="Population in the area")
    households: float = Field(..., description="Number of households in the area")
    median_income: float = Field(..., description="Median income of the area")
    ocean_proximity: str = Field(..., description="Proximity to ocean (e.g., NEAR BAY, INLAND)")

@app.post("/predict")
def predict(input1 : PredictHousePrice):
    model = joblib.load(open('Housing_prices.joblib', 'rb'))
    User_input_df = pd.DataFrame([{
        'longitude': input1.longitude,
        'latitude': input1.latitude,
        'housing_median_age': input1.housing_median_age,
        'total_rooms': input1.total_rooms,
        'total_bedrooms': input1.total_bedrooms,
        'population' : input1.population,
        'households': input1.households,
        'median_income': input1.median_income,
        'ocean_proximity': input1.ocean_proximity
    }])
    some_data = pd.DataFrame(User_input_df)
    print(model.predict(some_data)[0])