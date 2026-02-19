from fastapi import FastAPI

app = FastAPI(title="RideFlow API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "RideFlow API is running! 🚗"}
