from fastapi import FastAPI

app = FastAPI(title="Indian Recipe API")

@app.get("/")
def home():
    return {"message": "Welcome to the Indian Recipe API!"}