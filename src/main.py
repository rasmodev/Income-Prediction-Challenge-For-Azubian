from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Load the saved model
with open("model_and_key_components.pkl", "rb") as f:
    components = pickle.load(f)
dt_model = components['model']

app = FastAPI()

class IncomePredictionRequest(BaseModel):
    age: int
    gender: str
    education: str
    worker_class: str
    marital_status: str
    race: str
    is_hispanic: str
    employment_commitment: str
    employment_stat: int
    wage_per_hour: int
    working_week_per_year: int
    industry_code: int
    industry_code_main: str
    occupation_code: int
    occupation_code_main: str
    total_employed: int
    household_stat: str
    household_summary: str
    vet_benefit: int
    tax_status: str
    gains: int
    losses: int
    stocks_status: int
    citizenship: str
    mig_year: int
    country_of_birth_own: str
    importance_of_record: float

   
class IncomePredictionResponse(BaseModel):
    income_prediction: str
    prediction_probability: float

@app.get("/")
async def root():
    # Endpoint at the root URL ("/") returns a welcome message with a clickable link
    message = "Welcome to the Income Classification API! This API Provides predictions for Income based on several inputs. To use this API, please access the API documentation here: https://rasmodev-income-prediction-fastapi.hf.space/docs/"
    return message


@app.post("/predict/")
async def predict_income(data: IncomePredictionRequest):
    try:
        input_data = data.dict()
        input_df = pd.DataFrame([input_data])
        prediction = dt_model.predict(input_df)
        prediction_proba = dt_model.predict_proba(input_df)
        prediction_result = "Income over $50K" if prediction[0] == 1 else "Income under $50K"
        return {"income_prediction": prediction_result, "prediction_probability": prediction_proba[0][1]}

    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        raise

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)