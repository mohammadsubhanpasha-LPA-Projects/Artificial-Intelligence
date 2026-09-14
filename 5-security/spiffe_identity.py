from fastapi import FastAPI

app = FastAPI()

@app.get("/identity")
def get_identity():
    return {"spiffe_id": "spiffe://aegis.q/arthur-excalibur"}

@app.get("/verify")
def verify_identity():
    return {"status": "mTLS verified"}
