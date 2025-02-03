from fastapi import FastAPI, Header, HTTPException
from transformers import pipeline

app = FastAPI(
    title="Groq API Integration Demo",
    description="A simple API that translates English text to Spanish using Hugging Face."
)

# In a real-world scenario, store this token securely.
API_TOKEN = "MY-API-TOKEN"

# Set up the translation pipeline: English to Spanish.
translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")

@app.get("/translate", summary="Translate English text to Spanish")
async def translate(
    text: str,
    token: str = Header(..., description="API token for authentication")
):
    """
    Translates the given English text to Spanish.

    - **text**: The English text to be translated.
    - **token**: Your API token (passed as a header).
    """
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid API Token")
    
    translation_output = translator(text)
    translation_text = translation_output[0]["translation_text"]
    return {"translation": translation_text}