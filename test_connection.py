from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Du bist ein AI-Kommunikationsexperte für Ethik und Fairness."},
        {"role": "user", "content": "Schreibe einen kurzen, professionellen LinkedIn-Post über Bias in Trainingsdaten von LLMs."}
    ]
)

print(response.choices[0].message.content)