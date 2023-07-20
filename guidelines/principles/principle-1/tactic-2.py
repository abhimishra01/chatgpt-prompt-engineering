# principle  :- write clear and specific instructions
## Tactic 2 :- Ask for structured output

import sys
sys.path.append('../../')

from service.openai import get_completion

prompt = f"""
Generate a list of three made up book titles along with their authors and genre. Provide them in JSON format, with the following keys :- book_title, author, genre
"""

response = get_completion(prompt)
print(response)