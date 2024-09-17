# Mad Libs Story Generator

# Prompt the user for different words
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter the last adjective: ")
animal1 = input("Enter an animal: ")
animal2 = input("Enter another animal: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")

# Conditional variations
if animal1 == "monkey":
    special_sentence = f"I even tried to {verb} like the monkey, but I couldn't!"
else:
    special_sentence = f"The {animal1} was so curious, it came closer to me!"

# Constructing the Mad Libs story
story = f"""
On a beautiful {adjective1} day, I went to the {place}. 
I saw a funny {adjective2} {animal1} swinging from the trees. {special_sentence} 
Then, I spotted a majestic {adjective3} {animal2} lounging in the sun. 
What a wild and {adjective4} experience!
"""

# Display the final story
print(story)

