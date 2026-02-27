"""Ejemplo CLI que consulta al SDK de Gemini (Google Generative AI)."""

# https://ai.google.dev/gemini-api/docs
# pip install -q -U google-genai

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)