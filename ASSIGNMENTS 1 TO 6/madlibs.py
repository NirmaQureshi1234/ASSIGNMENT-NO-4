print("Welcome to the Mad Libs Game!")


name = input("Enter your name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
food = input("Enter a type of food: ")


story = f"""
One bright morning, {name} decided to visit {place}.
While exploring, {name} stumbled upon a {adjective} {animal} that was {verb} around playfully.
It was such an unexpected sight that {name} couldn't stop laughing!
After a fun-filled day, {name} enjoyed a delicious feast of {food}, making the adventure even more memorable.
What an unforgettable day at {place}!
"""


print(story)
