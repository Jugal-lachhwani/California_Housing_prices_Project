import joblib # type: ignore
import pandas as pd # type: ignore
from custom_transformer import CombinedAttributesAdder

# import the ml model
with open('housing_pipeline.joblib', 'rb') as f:
    model = joblib.load(f)

# MLFlow
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):

    df = pd.DataFrame([user_input])

    # Predict the class
    predicted_class = model.predict(df)[0]

    return {
        "predicted_category": predicted_class
    }