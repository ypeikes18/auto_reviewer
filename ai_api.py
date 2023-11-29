import openai
import os

openai.api_key=os.getenv("OPEN_AI_API_KEY")

def get_response_to_prompt(prompt):
    completion = openai.ChatCompletion.create(model="gpt-4", messages = [{"role": "assistant", "content": prompt}])
    return completion.choices[0].message.content