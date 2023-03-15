import re
import time

def get_story(filename: str):
    """
    Read the story from a file and return a dictionary with each section as a key and the section content as a list of strings
    """
    story_dict = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        section = None
        for line in lines:
            if re.match("\[.*\]", line):
                section = line.strip()[1:-1]
                story_dict[section] = []
            else:
                story_dict[section].append(line.strip())
    return story_dict


def get_options_from_sentence(sentence: str):
    # extract the option name (between "@" and "[" characters)
    option_name = sentence[1:sentence.find("[")]

    # extract the option text (between "[" and "]" characters)
    option_text = sentence[sentence.find("[") + 1:sentence.find("]")]

    # extract the option value (between "(" and ")" characters)
    option_value = sentence[sentence.find("(") + 1:sentence.find(")")]
    option_value = option_value.split()  # split the value into a list of strings

    return {
        "name": option_name,
        "text": option_text,
        "value": option_value
    }

def extract_options(story_dict: dict):
    """
    Extract the options from the story dictionary and return a new dictionary with the options as a dictionary    
    """
    for key, value in story_dict.items():
        if isinstance(value, list):
            new_value = []
            options = []
            for i in range(len(value)):
                sentence = value[i]

                # Check if the sentence is an option
                isOption = False
                if(sentence.startswith('@')):
                    if (i != len(value)-1 and value[i+1].startswith('@')):
                        isOption = True
                    if (i != 0 and value[i-1].startswith('@')):
                        isOption = True

                if isOption:
                    options.append(get_options_from_sentence(sentence))
                    
                else:
                    if options:
                        new_value.append(options)
                        options = {}
                    new_value.append(sentence)
            if options:
                new_value.append(options)
            story_dict[key] = new_value
    return story_dict


def print_sentence(string: str, variables: dict):
    # If string contains {variable} replace it with the value of the variable
    for key, value in variables.items():
        string = string.replace(f"{{{key}}}", value)

    time.sleep(1)
    wordlist = string.split(" ")
    for word in wordlist:
        print(word, end=' ', flush=True)
        time.sleep(0.1)
    print()
    


def read_user_option(sentence: list):
    for option in sentence:
        print(f"{option['text']} {option['value']}" )            
        validOptionSelected = False
    while not validOptionSelected:
        choice = input("Enter your choice: ")
        
        for option in sentence:
            if choice in option["value"]:
                return option["name"]
        if not validOptionSelected:
            print("Invalid option")

def read_user_input(text):
    return input(f"{text}: ")


def run_story(story_dict: dict):
    storyblock = 'start'
    variables = {}
    while storyblock != 'end':
        for sentence in story_dict[storyblock]:
            
            if isinstance(sentence, list):
                # User has to select an option
                storyblock = read_user_option(sentence)

            elif isinstance(sentence, str):
                if sentence.startswith('@'):
                    # Go to another story block
                    storyblock = sentence[1:]
                elif sentence.startswith("+"):
                    # The user must enter a value for a variable
                    variable = sentence[1:sentence.find("[")]
                    text = sentence[sentence.find("[") + 1:sentence.find("]")]
                    value = read_user_input(text)
                    variables[variable] = value
                else:
                    # It is a normal string, print it
                    print_sentence(string=sentence, variables=variables)