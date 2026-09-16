from fastapi import FastAPI
import time

app = FastAPI()

# Fast 0.4s cold start mock
start_time = time.time()

@app.get("/")
def read_root():
    return {"message": "Hello Lancelot! Fastest deploy knight.", "cold_start_time": "0.4s", "rps_mock": "1M RPS"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
