import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# API Endpoint
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Default Models
MODELS = {
    "qwen": "qwen/qwen3-32b",
    "phi": "microsoft/phi-4",
    "llama": "meta-llama/llama-3.3-70b-instruct"
}