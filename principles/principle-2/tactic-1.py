# principle :- Give the model time to think
# Tactic :- specify the steps required to complete the task
# 

import sys
sys.path.append('../../')

from service.openai import get_completion

text = f"""
In a quaint countryside village, adventurous friends Jack and Jill set out to explore the enchanted forest. Excitedly, they packed a picnic basket and ventured into the magical woods, where glistening streams and ancient trees beckoned.

As they roamed deeper, the forest's charm enchanted them further. Sipping water from a sparkling spring, they found themselves weightless, floating like feathers. Amidst laughter and joy, they soared through the woods.

But the sky turned dark, and rain poured down, leaving them lost and frightened. Luckily, Granny Rose, the wise village woman, came to their rescue. With her guidance, they found their way home, drenched but grateful.

The adventure taught Jack and Jill valuable lessons. They treasured each moment, knowing that with Granny Rose's wisdom, they could overcome any challenge. And so, their bond deepened, and they continued exploring life's wonders, grateful for the magical memories they shared.
"""

prompt = f"""
Perform the following actions:
1 - Summarize the following text delimited by <>.
2 - Translate the summary into french.
3 - List the names mentioned in the french summary.
4 - Output a json object with following keys: french_summary, num_names

Then answer back in the following format and separate the answers by line breaks:
1 - answer
2 - answer
3 - answer
4 - answer

<{text}>
"""

response = get_completion(prompt)
print(response)