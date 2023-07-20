# principle :- Give the model time to think
# Tactic :- Instruct the model to work out its own solution before rushing to the conclusion
# 

import sys
sys.path.append('../../')

from service.openai import get_completion

text = f"""
Question: A person wants to set up a solar plant to power the school. The land for the plant costs $50,000, and the maintenance expenses are estimated at $10,000 annually. The average monthly electricity bill for the school is $2,000. Assuming a payback period of 5 years, calculate the total cost of setting up the solar plant and the yearly savings
Answer: 
Total cost of setting up the solar plant: $100,000.
Yearly savings: $120,000.
Payback period: 0.83 years
"""


prompt = f"""
Determine if the student's solution is correct or not from the following text provided delimited by <>
# Determine if the student's solution is correct or not from the following text provided delimited by <>
# To execute this task, you need to do the following:
# 1 - First work out your own solution to the problem.
# 2 - Compare it with the solution provided by the student and evaluate whether its correct or not.
# 3 - Do not decide the student's solution's verdict until you have validated it from your solution.
<{text}>

"""

response = get_completion(prompt)
print(response)
