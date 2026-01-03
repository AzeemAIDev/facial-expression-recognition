import io
import uvicorn
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI , HTTPException , UploadFile , File

# Allowed frontend origins for CORS
origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

# Load trained FER model
model = load_model("F:\AI PROJECTS\FER MODEL\model\FER_model.h5")

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Face Recognization Expression",
    description="Face Expressions Detector",
    version="1.0.0.0"
)

# Enable CORS middleware for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Allowed client origins
    allow_credentials=True,
    allow_methods=["*"],               # Allow all HTTP methods
    allow_headers=["*"],               # Allow all headers
)

# Class labels used during model training
classes = ["Angry", "Contempt", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

def prepare_image(img_byte):
    # Load image from bytes and convert to grayscale
    img = Image.open(io.BytesIO(img_byte)).convert("L")
    
    # Resize image to model input size
    img = img.resize((48 , 48))
    
    # Convert image to numpy array
    img_array = image.img_to_array(img)
    
    # Add batch dimension
    img_array = np.expand_dims(img_array , axis=0)
    
    # Normalize pixel values
    img_array = img_array / 255.0

    return img_array

@app.get("/")
def home():
    # Health check endpoint
    return {"return" : "FER api is running"}

@app.post("/predict")
async def predict(file : UploadFile = File(...)):
    # Read uploaded image file
    content = await file.read()
    
    # Preprocess image for prediction
    prepared_image = prepare_image(content)

    # Run model inference
    prediction = model.predict(prepared_image)
    
    # Get index of highest probability
    max_index = np.argmax(prediction[0])

    # Extract predicted emotion and confidence
    result = classes[max_index]
    confidence = float(prediction[0][max_index])

    # Return prediction results
    return {
        "emotion" : result,
        "confidence" : f"{confidence * 100:.2f}%",
        "all_prediction" : {
            classes[i]: float(prediction[0][i]) for i in range(len(classes))
        }
    }

# Run FastAPI app using Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app" , host="127.0.0.1" , port=8000)
