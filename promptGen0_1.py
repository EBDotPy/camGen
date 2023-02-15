import os
import json

# Define a function to load a list from a JSON file
def load_list(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Get the list of JSON files in the "lists" directory
json_files = [f for f in os.listdir("lists") if f.endswith(".json")]

# Create an empty dictionary to store the lists
lists = {}

# Load the lists from the JSON files and store them in the dictionary
for file_name in json_files:
    list_name = os.path.splitext(file_name)[0]
    list_data = load_list(os.path.join("lists", file_name))
    lists[list_name] = list_data


# Prompt the user for the prompt
prompt = input("Enter your prompt or type !help to list options: ")

# Process the prompt and choose random items from the lists
output = []
sections = prompt.split("_")
for i, section in enumerate(sections):
    if i % 2 == 0:
        output.append(section)
    elif section in lists:
        output.append(random.choice(lists[section]))
    else:
        output.append("_" + section + "_")

# Generate and print the specified number of random phrases
num_phrases = int(input("How many random entries would you like?"))
for i in range(num_phrases):
    current_phrase = []
    for word in output:
        if word in lists:
            current_word = random.choice(lists[word])
        else:
            current_word = word
        current_phrase.append(current_word)
    print("".join(current_phrase))
