import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-3.5-turbo'


def get_completion(prompt, model=MODEL):
    messages = [{"role":"user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness
    )
    return response.choices[0].message['content']