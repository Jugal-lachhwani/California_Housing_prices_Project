from fastapi import FastAPI # type: ignore
import numpy as np # type: ignore
import joblib # type: ignore
import pandas as pd # type: ignore
import traceback
from schema.user_input import HousingInput
from schema.output_validation import PredictionResponse
from predict import predict_output

# Import custom transformer to avoid deserialization error
from custom_transformer import CombinedAttributesAdder

# # Load pipeline
# model = joblib.load("housing_pipeline.joblib")

app = FastAPI()





@app.post("/predict", response_model = PredictionResponse)
def predict(data: HousingInput):
    try:
        input_dict = {
            "longitude": data.longitude,
            "latitude": data.latitude,
            "housing_median_age": data.housing_median_age,
            "total_rooms": data.total_rooms,
            "total_bedrooms": data.total_bedrooms,
            "population": data.population,
            "households": data.households,
            "median_income": data.median_income,
            "ocean_proximity": data.ocean_proximity
        }

        # Wrap in a DataFrame to preserve column names
        input_df = pd.DataFrame([input_dict])

        # prediction = model.predict(input_df)
        prediction = predict_output(input_dict)
        return {"prediction": prediction.tolist()}

    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}
