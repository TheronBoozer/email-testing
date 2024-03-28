import json
import os
from openai import OpenAI
# from config import OPENAI_API_KEY


with open('keys.json') as key:
    keys = json.load(key)

    
client = OpenAI(
    api_key = keys["OPENAI_API_KEY"]
)

async def generate_email():
    print('hhmmmmm')
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)

async def call():
    print('huh')
    await generate_email()
