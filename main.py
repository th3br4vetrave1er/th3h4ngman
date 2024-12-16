import random


word_list = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam",
    "zucchini", "ant", "bee", "cat", "dog", "elephant", "fox", "giraffe", "horse",
    "iguana", "jellyfish", "kangaroo", "lion", "monkey", "newt", "octopus", "penguin",
    "quail", "rabbit", "snake", "tiger", "urchin", "vulture", "wolf", "xenops",
    "yak", "zebra", "almond", "basil", "carrot", "dill", "endive", "fennel",
    "garlic", "hazelnut", "iris", "jasmine", "kale", "lavender", "mint", "nutmeg",
    "oregano", "parsley", "quinoa", "rosemary", "sage", "thyme", "umber", "violet",
    "walnut", "xylophone", "yucca", "zinnia", "atlas", "bison", "cactus", "desert",
    "everest", "fjord", "geyser", "horizon", "island", "jungle", "kettle",
    "lagoon", "mountain", "north", "oasis", "plateau", "quartz", "reef",
    "savanna", "tundra", "upland", "valley", "waterfall", "xenon", "yard", "zephyr"
]

random_word = random.choice(word_list)

print("Hello, brave traveler! Would you dare to play with me?")
print("This is a game called the HANGMAN! And you simply must guess a word by guessing letters!!")
print("So, let us begin!")
print(random_word)
running = True

while running:
    guess = input("Guess the letter: ").lower()
    if guess in random_word:
        print("Right!")
        running = False
    else:
        print("Wrong!")