# Data based parser
# Main idea:
#   - Parse the upcoming sentence
#   - Update the dictionary with the new data
#   - Return the dictionary

import pynmea2

result_data = {}

def parse(sentence):
    """
    Parsing the sentence using pynmea2
    We are looping through the sentence fields (fields are the data in the sentences)
    and adding that data with its name to the result dictionary
    """
    try:
        msg = pynmea2.parse(sentence)
        for key in msg.fields:
            result_data[key[0]] = getattr(msg, str(key[1])) if getattr(msg, str(key[1])) != "" else result_data[key[0]]
    except:
        pass

def get_result():
    "Getter for the result dictionary"
    return result_data