import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv()

class GrokClient:
    def __init__(self, api_key=None, mock_mode=False):
        self.api_key = api_key or os.getenv("XAI_API_KEY")
        self.mock_mode = mock_mode
        self.base_url = "https://api.x.ai/v1"  # Standard xAI base URL
        
        if not self.api_key and not self.mock_mode:
            print("Warning: No API key found. Defaulting to MOCK MODE.")
            self.mock_mode = True

    def chat_completion(self, messages, model="grok-beta"):
        """
        Sends a chat completion request to Grok.
        """
        if self.mock_mode:
            return self._mock_chat_response(messages)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "messages": messages,
            "model": model,
            "stream": False,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error communicating with Grok: {e}"

    def generate_image(self, prompt, model="grok-2-image"):
        """
        Generates an image using Grok's image generation capabilities.
        """
        print(f"\n[System] Generating image for: '{prompt}'...")
        
        if self.mock_mode:
            time.sleep(2)
            return "[Mock Image URL: https://example.com/grok_image.png]"

        # Note: This is a hypothetical endpoint structure based on standard practices.
        # xAI's specific image endpoint might differ.
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "model": model,
            "n": 1,
            "size": "1024x1024"
        }

        try:
            # Hypothetical endpoint
            response = requests.post(f"{self.base_url}/images/generations", headers=headers, json=data)
            response.raise_for_status()
            # Assuming standard OpenAI-like response structure
            return response.json()['data'][0]['url']
        except Exception as e:
            return f"Error generating image: {e}"

    def generate_video(self, prompt, image_url=None):
        """
        Generates a video using Grok's video capabilities (Grok Imagine/Video).
        """
        print(f"\n[System] Generating video for: '{prompt}'...")
        
        if self.mock_mode:
            time.sleep(3)
            return "[Mock Video URL: https://example.com/grok_video.mp4]"

        # Note: Video generation endpoints are often distinct or beta.
        # This is a placeholder for the actual implementation.
        return "Video generation API integration requires specific beta access details."

    def _mock_chat_response(self, messages):
        last_user_message = messages[-1]['content']
        return f"[Mock Grok Response] You said: '{last_user_message}'. This is a simulated roleplay response. Imagine a vivid scene here!"
