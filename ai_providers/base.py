from abc import ABC, abstractmethod
from typing import Dict, Optional

class BaseAIProvider(ABC):
    """Base class for all AI providers."""
    
    @abstractmethod
    async def generate_response(self, prompt: str, context: Optional[Dict] = None) -> str:
        """Generate a response from the AI model."""
        pass

    @abstractmethod
    async def process_message(self, message: str, user_id: str) -> str:
        """Process a message and return a response."""
        pass

    @abstractmethod
    def validate_api_key(self) -> bool:
        """Validate the API key for the provider."""
        pass