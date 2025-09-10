#Goal

#Create a Python program that asks the user for different types of words (nouns, verbs, adjectives, etc.) and then generates a funny story using their inputs.

# Requirements

# Your program should:

# Greet the user.

# Ask the user to enter at least 5 different words (e.g., noun, adjective, verb, place, animal, food).

# Insert those words into a pre-written story.

# Print the completed story back to the user.

# Use string formatting (e.g., f-strings or .format()).

# Add at least one line break (\n) in your story to make it look nice.

print("Hello! Welcome to my Mad libs Game.")
print("Enter the following words")

noun=input("Enter a noun: ")
adjective=input("Enter an adjective: ")
verb=input("Enter a verb: ")
place=input("Enter the name of a place: ")
animal=input("Enter the name of an animal: ")
food=input("Enter the name of a type pf food: ")

story = f"""
    One {adjective} day, I went to the {place}\n
    I saw a {animal} that tried to {verb} my {noun}.
    Luckily, I had some {food}, and everything turned out fine!
    """
    
print(story)
