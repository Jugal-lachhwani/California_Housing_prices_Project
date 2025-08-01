from pydantic import BaseModel,Field # type: ignore
class HousingInput(BaseModel):
    longitude: float = Field(..., description="Longitude of the house location")
    latitude: float = Field(..., description="Latitude of the house location")
    housing_median_age: float = Field(..., description="Median age of the houses in the area")
    total_rooms: float = Field(..., description="Total number of rooms in the house")
    total_bedrooms: float = Field(..., description="Total number of bedrooms in the house")
    population: float = Field(..., description="Population in the area")
    households: float = Field(..., description="Number of households in the area")
    median_income: float = Field(..., description="Median income of the area")
    ocean_proximity: str = Field(..., description="Proximity to ocean (e.g., NEAR BAY, INLAND)")