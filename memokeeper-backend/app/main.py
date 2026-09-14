from pathlib import Path

from fastapi import FastAPI, File, UploadFile

# Storage location
STORAGE_DIR = Path("storage")

# Create storage directory if it doesn't exist
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

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

@app.post("/files/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = STORAGE_DIR / file.filename

    with file_path.open("wb") as buffer:
        while chunk := await file.read(1024 * 1024):
            buffer.write(chunk)

    await file.close()

    return {
        "filename": file.filename,
        "message": "File uploaded successfully"
    }