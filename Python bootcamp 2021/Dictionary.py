import json
from difflib import get_close_matches

data = json.load(open("data.json"))

count = 0

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for 'yes' or n for 'no':")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return ("Word not found!")
        else:
            return ("Worng input!")
    else:
        print("Word not found!")

word = input("enter the word you want to search:")
output = translate(word)
if type(output) == list:
    for item in output:
        count += 1
        print(str(count)+":- "+item)
else:    
    print(output)