from fastapi import FastAPI, Query
from app.utils import generate_model
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/generate3d")
def generate_3d(prompt: str = Query(...)):
    output_path = generate_model(prompt)
    return FileResponse(output_path, media_type='model/gltf-binary', filename="model.glb")

@app.get("/status")
def status():
    return {"status": "running", "model": "Shap-E", "version": "v1"}
