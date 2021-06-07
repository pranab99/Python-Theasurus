import json
import difflib
from difflib import get_close_matches
file=json.load(open("data.json"))

word=input("Enter the word you want to search :")
def dictionary(word):
    word=word.lower()
    if word in file:
        return file[word]
    elif word.title() in file: #if user entered "texas" this will check for "Texas" as well.
        return file[word.title()]
    elif word.upper() in file: #in case user enters words like USA or NATO
        return file[word.upper()]
    elif len(get_close_matches(word,file.keys()))>0:
        yn=input("Hey phrasal noobie! You meant '%s' instead? Enter 'Y' if yes or 'N' if no: "%get_close_matches(word,file.keys())[0])
        if yn=='Y':
            return file[get_close_matches(word,file.keys())[0]]
        elif yn=="N":
            return "So sorry, you cant flex as the word doesn't exist"
        else :
            return "We didn't understand your entry as you dont understand yours. "
    else:
        return "So sorry, you cant flex as the word doesn't exist"

output=dictionary(word)#output is basically a list so we can iterate over it 

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
