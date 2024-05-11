import os
import re
import json

LONGEST_KEY = 0  # Init at 0, but determine based on json file input
starter = "SKWR"

if os.name == "posix":  # Check if the current OS is Linux
    dictionary_file = (
        "/home/zach/.config/plover/dicts/aerick/lapwing-prefixed-proper-nouns.json"
    )
elif os.name == "nt":  # Check if the current OS is Windows
    dictionary_file = "C:\\Users\\aazach\\AppData\\Local\\plover\\plover\\dicts\\aerick\\lapwing-prefixed-proper-nouns.json"
else:
    # Handle other operating systems if needed
    print("Unsupported operating system")


def determine_longest_key_length():
    longest_key = 0
    with open(dictionary_file) as temp_dictionary:
        data = json.load(temp_dictionary)
        for key in data.keys():
            num_segments = len(key.split("/"))
            longest_key = max(longest_key, num_segments)
    return longest_key


LONGEST_KEY = determine_longest_key_length()
# print(LONGEST_KEY)


def change_starter(dictionary_file, starter):
    modified_dictionary = {}
    with open(dictionary_file) as temp_dictionary:
        temp_dictionary = json.load(temp_dictionary)
        for stroke in temp_dictionary:
            outline = temp_dictionary[stroke]
            new_stroke = starter + "/" + stroke[2:]  # Replace #/ with starter/
            modified_dictionary[new_stroke] = outline

    return modified_dictionary


modified_dictionary = change_starter(dictionary_file, starter)


def lookup(stroke):
    if isinstance(stroke, tuple):
        stroke = "/".join(stroke)  # Convert tuple to string
    if stroke in modified_dictionary:
        return modified_dictionary[stroke]
    else:
        raise KeyError("Translation not found for stroke: {}".format(stroke))


def reverse_lookup(outline):
    matches = []
    for key, val in modified_dictionary.items():
        if val == outline:
            matches.append(tuple(key.split("/")))  # Convert stroke string back to tuple
    return matches


# print(lookup(starter + '/' + 'SABG'))
# print(reverse_lookup("Zach"))
