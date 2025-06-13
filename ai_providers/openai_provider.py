from typing import Dict, Optional
from .base import BaseAIProvider
from decouple import config

class OpenAIProvider(BaseAIProvider):
    def __init__(self):
        self.api_key = config('OPENAI_API_KEY', default=None)
        self.model = config('OPENAI_MODEL', default='gpt-3.5-turbo')

    async def generate_response(self, prompt: str, context: Optional[Dict] = None) -> str:
        # Implementation will be added later
        pass

    async def process_message(self, message: str, user_id: str) -> str:
        # Implementation will be added later
        pass

    def validate_api_key(self) -> bool:
        return bool(self.api_key)