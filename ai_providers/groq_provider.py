from typing import Dict, Optional
from .base import BaseAIProvider
from decouple import config
import httpx

class GroqProvider(BaseAIProvider):
    def __init__(self):
        self.api_key = config('GROQ_API_KEY', default=None)
        self.model = config('GROQ_MODEL', default='llama2-70b-4096')
        self.api_base = "https://api.groq.com/v1/completions"

    async def generate_response(self, prompt: str, context: Optional[Dict] = None) -> str:
        async with httpx.AsyncClient() as client:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": self.model,
                "prompt": prompt,
                "max_tokens": 1000,
                "temperature": 0.7,
            }
            response = await client.post(self.api_base, json=data, headers=headers)
            return response.json()['choices'][0]['text']

    async def process_message(self, message: str, user_id: str) -> str:
        return await self.generate_response(message)

    def validate_api_key(self) -> bool:
        return bool(self.api_key)