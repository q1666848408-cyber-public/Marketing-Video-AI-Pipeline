"""
Gemini 2.5 Pro multi-modal client.
"""

from typing import Optional, List


class GeminiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def generate_image(self, prompt: str, reference: Optional[bytes] = None) -> bytes:
        """Gemini Flash Image — generate ref image. [Not shown]"""
        pass

    async def analyze(self, prompt: str, images: List[bytes] = None) -> str:
        """Multi-modal analysis. [Not shown]"""
        pass
