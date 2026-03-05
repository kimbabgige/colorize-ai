from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def root():
    return {"message": "Colorizer API ready"}

@app.get("/ping")
def ping():
    return {"status": "alive"}

@app.post("/api/colorize")
async def colorize_video(file: UploadFile = File(...)):
    contents = await file.read()
    return StreamingResponse(io.BytesIO(contents), media_type="video/mp4")