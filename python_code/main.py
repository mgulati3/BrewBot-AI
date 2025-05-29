from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("RUNPOD_TOKEN"),
    base_url=os.getenv("RUNPOD_CHATBOT_URL"),
)
model_name = os.getenv("MODEL_NAME", "gpt-3.5-turbo")

response = client.chat.completions.create(
    model=model_name,
    messages=[{"role": "user", "content": "What's the capital of Germany?"}],
    temperature=0.0,
    top_p=0.8,
    max_tokens=2000,
)

print(response.choices[0].message.content.strip())
