from typing import Dict, Optional
from .base import BaseAIProvider
from decouple import config
import google.generativeai as genai

class GeminiProvider(BaseAIProvider):
    def __init__(self):
        self.api_key = config('GEMINI_API_KEY', default=None)
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    async def generate_response(self, prompt: str, context: Optional[Dict] = None) -> str:
        response = self.model.generate_content(prompt)
        return response.text

    async def process_message(self, message: str, user_id: str) -> str:
        return await self.generate_response(message)

    def validate_api_key(self) -> bool:
        return bool(self.api_key)