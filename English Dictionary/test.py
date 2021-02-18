# This a library funtion to compare the extent of similarity between two patterns or sequences

# from difflib import SequenceMatcher

# print(SequenceMatcher(None, "rainn", "rain"))
# print(SequenceMatcher(None, "rainn", "rain").ratio())

# from difflib import get_close_matches

# print(get_close_matches("rainn", ["help", "pyramid", "rain"]))


import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        return "The word does not exist. Please double check it."


word = input("Enter word: ")

print(translate(word))

