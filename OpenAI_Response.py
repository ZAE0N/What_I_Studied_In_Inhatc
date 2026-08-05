from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_KEY = os.getenv('OPENAI_API_KEY')    # Get API key from .env file

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_KEY)

# First request
first_response = client.chat.completions.create(
    model="gpt-4o",     # GPT model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "최근 AI trend에 대해 알려줘"},
    ],  
    temperature=0.1,
    max_tokens=256
)

# Link to first response
first_response_text = first_response.choices[0].message.content

# Second request
second_respose = client.chat.completions.create(
    model="gpt-4o",     # GPT model
    messages=[
        {"role": "user", "content": "최근 AI trend에 대해 알려줘"},
        {"role": "user", "content": first_response_text},
        {"role": "user", "content": "이 기술 중 가장 주목받는 기술은?"},
    ],  
    temperature=0.1,
    max_tokens=256
)

print('\n====[ Response Content ]====')
print(second_respose.choices[0].message.content)  # GPT 답변 출력