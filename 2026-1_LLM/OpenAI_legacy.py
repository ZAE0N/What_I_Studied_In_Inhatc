from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_KEY = os.getenv('OPENAI_API_KEY')    # Get API key from .env file

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_KEY)

# Create a chat completion
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",     # GPT model
    prompt="AI 기술의 미래에 대하여 알려줘.",       # Text 기반 모델이어서 message가 없음
    temperature=0.7,
    max_tokens=150,
)

print(response)

print("\nㅡㅡㅡㅡㅡ")
print(response.choices[0])

print('\n====[ Response Content ]====')
print(response.choices[0].text)  # GPT 답변 출력