import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.responses import Response
from fastapi.staticfiles import StaticFiles
from Cogniezer.pipeline.prediction import PredictionPipeline
from Cogniezer.pipeline.transcribe import TranscribePipeline
from Cogniezer.logging import logger

load_dotenv()

prediction_pipeline = PredictionPipeline()
transcribe_pipeline = TranscribePipeline()
app = FastAPI()

host = os.getenv("HOST")
port = os.getenv("PORT")

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

logger.info(f"Starting server on {host}:{port}")

@app.get("/",tags=["Pages"])
async def index():
    return HTMLResponse(content=templates.get_template("index.html").render(), status_code=200)


@app.post("/api/predict",tags=["API"])
async def predict(text):
    try:
        summary = prediction_pipeline.predict(text)
        return summary
    except Exception as e:
        return Response(e)

@app.post("/api/uploadfile/",tags=["API"])
async def upload_file(wav_file: UploadFile):
    file_path = os.path.join("audio-uploads", wav_file.filename)

    with open(file_path, "wb") as f:
        f.write(wav_file.file.read())
    
    try:
        text = transcribe_pipeline.transcribe(file_path)
        summary = prediction_pipeline.predict(text)
        os.remove(file_path)
        return summary
    except Exception as e:
        os.remove(file_path)
        return Response(e)
        

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
