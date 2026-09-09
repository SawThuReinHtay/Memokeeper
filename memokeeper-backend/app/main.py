from fastapi import FastAPI

app = FastAPI(
    title="Memokeeper API",
    description="Backend API for the Memokeeper hardware",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Memokeeper API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/strh")
def authorname():
    return{
        "Author": "Saw Thu Rein Htay"
    }