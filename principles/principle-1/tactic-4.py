# principle  :- write clear and specific instructions
## Tactic 4 :- Few shot prompting. Give successful examples of completing tasks then ask model to perform the task


import sys
sys.path.append('../../')

from service.openai import get_completion

text = f"""
You should express what you want a model to do by providing instructions that are as clear and specific as you can possibly make then. This will guide the model towards the desired output, and reduce the chances of receiving irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt. In many cases longer prompts provide more clarity and more context to the model.
"""
prompt = f"""
Your task is to answer in a consistent style.

<child>: Teach me about solar system.

<teacher>: The solar system is the home where the planet Earth resides. We are the residents of the planet Earth .... 

<child>: Wow I didn't knew we lived on the planet which is part of solar system.

<child>: Tell me more !
"""

response = get_completion(prompt)
print(response)