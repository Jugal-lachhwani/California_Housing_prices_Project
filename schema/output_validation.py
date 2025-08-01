from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: float = Field(
        ...,
        description="The predicted insurance premium category",
        example="High"
    )