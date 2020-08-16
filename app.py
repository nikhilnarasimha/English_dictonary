# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:23:43 2020

@author: malat
"""
import json

import os

import difflib 

from difflib import SequenceMatcher

from difflib import get_close_matches

data = json.load(open("data.json"))

keys = data.keys()

def Trans(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, keys, cutoff= 0.8)) > 0:
        sim = get_close_matches(w, keys, cutoff= 0.8)
        yn = input("Did you mean {} Instead of {w}? Enter y for yes, n for no. : ".format(sim[0], w = word))
        if yn == "y":
            return data[sim[0]]
        elif yn == "n" and len(get_close_matches(w, keys, cutoff= 0.8)) > 1:
            yn2 = input("Did you mean {} Instead of {w}? Enter y for yes, n for no. : ".format(sim[1], w = word))
            if yn2 == "y":
                return data[sim[1]]
            else:
                return "The Word don't exist"
        else:
            return "Try entering Another Word"
    else:
        return("Sorry, The Meaning of the word doesn't exists with us. Please try another word")


word = input("Enter the Words: ")

output = Trans(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
