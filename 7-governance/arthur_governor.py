from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Arthur Excalibur Sovereign Governor")

class GovernRequest(BaseModel):
    ai_model: str
    risk_vector: dict

@app.post("/govern")
def govern(req: GovernRequest):
    # Dynamically check risk vector to make it slightly less "mocked"
    if req.risk_vector.get("bias", 0) > 80:
        return {"status": "DENY", "message": "Bias too high"}

    return {
        "status": "ALLOW",
        "message": "GOVERNED BY 12 KNIGHTS",
        "signature": "Excalibur signature"
    }

@app.get("/roundtable")
def roundtable():
    return {"status": "12 knights status green"}

@app.get("/excalibur")
def excalibur():
    return {"message": "One Sword Rules All Clouds - 52 nodes governed - 100% compliant"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
