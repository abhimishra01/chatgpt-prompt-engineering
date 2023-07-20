import sys
sys.path.append('..')

from service.openai import get_completion

prompt=f"""
Tell me in detail about Grounding Glider version 2.0 by Jack and sons.
"""
# this is a made up procut, and the would still try to response an answer, which might be dangerous in various cases hence use the LLM principles and their tactics in order to prevent this outcome.
# Tactic to reduce hallucination :-
# Fist instruct to find relevant valid information, then answer the question based on relevant information.

response = get_completion(prompt)
print(response)

# Output :-
# Grounding Glider version 2.0 is an innovative product developed by Jack and Sons, a leading company in the field of outdoor recreational equipment. This glider is designed to provide a unique and thrilling experience to users while ensuring their safety and comfort.

# The Grounding Glider version 2.0 is an upgraded version of its predecessor, incorporating several new features and improvements. It is built with high-quality materials, ensuring durability and longevity. The glider is designed to be used in outdoor settings such as parks, playgrounds, and open fields.

# One of the key features of the Grounding Glider version 2.0 is its advanced grounding system. This system ensures that the glider remains stable and secure during use, minimizing the risk of accidents or injuries. The glider is equipped with strong and sturdy anchors that firmly hold it to the ground, providing a safe and enjoyable experience for users.

# The glider also features a comfortable seating arrangement. The seats are ergonomically designed, providing adequate support and cushioning for users. The seating area is spacious enough to accommodate multiple individuals, allowing friends and family to enjoy the glider together.

# To enhance the gliding experience, the Grounding Glider version 2.0 is equipped with a smooth and efficient gliding mechanism. This mechanism allows users to glide effortlessly and smoothly, providing a thrilling sensation while maintaining control and stability. The glider is designed to be easy to operate, making it suitable for users of all ages.

# In terms of safety, the Grounding Glider version 2.0 is equipped with various safety features. It has a secure harness system that ensures users are properly strapped in and protected during the gliding experience. The glider also has a braking system that allows users to control their speed and come to a safe stop when needed.

# Additionally, the Grounding Glider version 2.0 is designed with aesthetics in mind. It has a sleek and modern design, with attention to detail in its construction. The glider is available in a range of vibrant colors, allowing users to choose the one that best suits their preferences.

# Overall, the Grounding Glider version 2.0 by Jack and Sons is a top-of-the-line outdoor recreational equipment that offers a thrilling and safe gliding experience. With its advanced grounding system, comfortable seating, smooth gliding mechanism, and various safety features, this glider is sure to provide hours of fun and excitement for users of all ages.