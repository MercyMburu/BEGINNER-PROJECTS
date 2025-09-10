import random

def madlib():
    print("Hello! Welcome to my Mad libs Game.")
    print("Enter the following words")

    noun=input("Enter a noun: ")
    adjective=input("Enter an adjective: ")
    verb=input("Enter a verb: ")
    place=input("Enter the name of a place: ")
    animal=input("Enter the name of an animal: ")
    food=input("Enter the name of a type pf food: ")

    stories = [
    "One day, a {adjective} {animal} decided to {verb} at the {place}. Everyone laughed when it grabbed a {noun} and ran away with some {food}.",

    "In the middle of {place}, a {adjective} {animal} tried to {verb} a {noun}. Luckily, someone distracted it with {food}.",

    "Yesterday, I saw a {adjective} {animal} that wanted to {verb} inside the {place}. Instead, it found a {noun} and ate {food}.",

    "A {adjective} {animal} once lived in the {place}. It loved to {verb} all day while keeping a {noun} in its pocket and munching on {food}.",

    "During my trip to {place}, I met a {adjective} {animal}. It tried to {verb} my {noun}, but I saved it by offering some {food}."
]
    # Pick a random template

    story_template=random.choice(stories)
    
    
    #Format it with user inputs
    story=story_template.format(
        adjective=adjective,
        animal=animal,
        verb=verb,
        place=place,
        noun=noun,
        food=food
    )
    
    
    print(story)

if __name__=="__main__":
    madlib()
