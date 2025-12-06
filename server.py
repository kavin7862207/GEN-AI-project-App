from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from grok_client import GrokClient
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Grok Client (Mock mode by default if no key)
client = GrokClient(mock_mode=False)

class ChatRequest(BaseModel):
    message: str
    history: list

class ImageRequest(BaseModel):
    prompt: str

class VideoRequest(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    # Construct messages for Grok
    messages = request.history + [{"role": "user", "content": request.message}]
    response = client.chat_completion(messages)
    return {"response": response}

@app.post("/api/image")
async def generate_image(request: ImageRequest):
    url = client.generate_image(request.prompt)
    return {"url": url}

@app.post("/api/video")
async def generate_video(request: VideoRequest):
    url = client.generate_video(request.prompt)
    return {"url": url}

# Serve static files (Frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
