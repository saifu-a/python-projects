import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):

    # Check for entry in dictiontary
    if word in data:
        return data[word]

    # Check for case-sensitivity
    elif word.lower() in data:
        return data[word.lower()]

    # Suggest word in case of typo in input
    elif get_close_matches(word, data.keys()):
        yn = input("Did you mean {} instead? Enter Y if yes, or N if no: ".format(
            get_close_matches(word, data.keys())[0]))

        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word does not exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word does not exist. Please double check it."


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)