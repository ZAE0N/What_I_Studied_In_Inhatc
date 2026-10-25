from GPT_Date_Function import get_current_time, tools   # GPT_Date_Function.py
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

# Function to get AI response
def get_GPT_response(strMessages, tools=None):
    response = client.chat.completions.create(
        model="gpt-4o",   
        messages=strMessages,   
        tools=tools,        # Pass available tools
    )
    return response

messages = [                # Starting system message
    {"role": "system", "content": "너는 User를 도와주는 상담사야."},  
]

while True:
    user_input = input("User\t: ")  # User input
    if user_input == "exit":        # User wants to exit
        break
    
    # User message added to conversation history    
    messages.append({"role": "user", "content": user_input})  

    GPT_response = get_GPT_response(messages, tools=tools)
    GPT_message = GPT_response.choices[0].message
    print(GPT_message)                          # GPT response for debugging

    tool_calls = GPT_message.tool_calls         # AI Response tool_calls
    if tool_calls:                              # If tool_calls exist
        tool_name = tool_calls[0].function.name # Extract function name to execute
        tool_call_id = tool_calls[0].id         # Tool_call ID    
        
        if tool_name == "get_current_time":     # if tool_name is "get_current_time"
            messages.append({
                "role": "function",             # Set role to "function"
                "tool_call_id": tool_call_id,
                "name": tool_name,
                "content": get_current_time(),  # Set content to result of get_current_time()
            })

        GPT_response = get_GPT_response(messages, tools=tools) # Get GPT response again
        GPT_message = GPT_response.choices[0].message

    messages.append(GPT_message)  # Add GPT response to conversation history

    print("GPT\t: " + GPT_message.content)  # Print GPT response