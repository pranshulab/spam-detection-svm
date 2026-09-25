from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
import joblib


# --------------------------------------------------
# 1. Create FastAPI application
# --------------------------------------------------


app = FastAPI(
    title="Email Spam Detection API",
    description="Spam detection using TF-IDF and Support Vector Machine",
    version="1.0"
)

# --------------------------------------------------
# 2. Load trained ML model and TF-IDF vectorizer
# --------------------------------------------------

model = joblib.load("spam_svm_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")


# Frontend

app.mount("/static", StaticFiles(directory="static"), name="static")





# --------------------------------------------------
# 3. Request data format
# --------------------------------------------------

class MessageRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="The message to classify as Spam or Ham"
    )


# --------------------------------------------------
# 4. Home endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return  FileResponse("static/index.html")


# --------------------------------------------------
# 5. Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict(request: MessageRequest):

    try:

        # Convert message into TF-IDF features
        message_tfidf = tfidf.transform([request.message])

        # Make prediction
        prediction = model.predict(message_tfidf)[0]

        # SVM decision score
        score = model.decision_function(message_tfidf)[0]

        # Convert prediction to readable result
        if prediction == 1:
            result = "Spam"
        else:
            result = "Ham"

        return {
            "message": request.message,
            "prediction": result,
            "svm_score": round(float(score), 4)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )