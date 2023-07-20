# principle :- write clear and specific instructions
## Tactic 3 :- Check whether conditions are satisfied, if not stop the prompt execution

import sys
sys.path.append('../../')

from service.openai import get_completion

tea_instructions = f"""
Making a cup of tea is a delightful and soothing process. To begin, gather all the necessary ingredients and tools: a teapot or teacup, tea leaves or tea bags of your favorite blend, fresh water, a kettle or pot, and a tea infuser if using loose tea. First, boil the water in the kettle or pot until it reaches the ideal temperature for your tea type. While waiting, place the tea leaves or tea bag in the teapot or infuser. Once the water is ready, carefully pour it over the tea leaves, allowing them to steep for the appropriate time, depending on the tea's instructions. During this time, the room fills with the delightful aroma of the brewing tea. After steeping, remove the infuser or tea bag and set it aside. Finally, pour the aromatic tea into your cup and, if desired, add a touch of milk, honey, or lemon for extra flavor. Now, with your steaming cup of tea in hand, take a moment to savor the warmth and embrace the tranquility it brings, making it the perfect companion for relaxation and contemplation. Enjoy your tea!
"""

prompt = f"""
You will be provided with a text delimited by backticks. If it contains a sequence of steps / instructions, re-write those instructions in the following format :-

Step 1 - ...., 
Step 2 - .... 
...
Step N - .... 

First validate if the text contains the sequence of steps / instructions, if not then stop the entire execution and simply write \"No Steps provided!\"

```{tea_instructions}```

"""


response = get_completion(prompt)
print(response)