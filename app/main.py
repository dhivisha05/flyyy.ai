from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from .api.routes import router

app = FastAPI(title="BOQ Excel Extractor", version="2.0")

# ─── CORS (allow local dev) ───
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── API routes ───
app.include_router(router)

# ─── Static files (React Build) ───
app.mount("/assets", StaticFiles(directory="boq-frontend/dist/assets"), name="assets")

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    # Only serve index.html for non-API routes
    if full_path.startswith("api"):
        return None
    return FileResponse("boq-frontend/dist/index.html")