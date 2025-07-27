# Text-to-3D Asset Generator using Shap-E

This project uses OpenAI’s Shap-E to convert text prompts into 3D models (.glb format), ideal for game asset prototyping.

## 🚀 How It Works
- Input: Text like "a fantasy potion bottle"
- Output: 3D model + preview

## 🧪 API (FastAPI)
- `/generate3d?prompt=...`
- `/status`

## 📁 Sample Output
- Prompt: "a small fantasy potion bottle"
- Output: sample.glb + preview image

## 🛠 How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📎 Contents
- app/: API code
- examples/: sample .glb and preview
