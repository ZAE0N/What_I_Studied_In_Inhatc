from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_KEY = os.getenv('OPENAI_API_KEY')    # Get API key from .env file

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_KEY)

# Create a chat completion
response = client.chat.completions.create(
    model="gpt-4o",     # GPT model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "머신러닝과 딥러닝의 차이점에 대하여 설명해줘"},
    ],  
    temperature=0.1,
    max_tokens=256
)

print(response)

print("\nㅡㅡㅡㅡㅡ")
print(response.choices[0])

print('\n====[ Response Content ]====')
print(response.choices[0].message.content)  # GPT 답변 출력