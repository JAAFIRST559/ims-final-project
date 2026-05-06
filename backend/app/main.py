from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "IMS running"}

@app.get("/hello")
def hello():
    return {"msg": "Hello from FastAPI 👋"}