# Data based parser
# Main plan for this parser is updating dataDict with new values if they are available
# In this way we don't need to parse for sentence type
# We are trying to get all data that we need and if its available we are updating dataDict
# If we are not able to get data we are using the last valid value
import pynmea2

attrs = []

def parse(sentence):
    try:
        msg = pynmea2.parse(sentence)
        for key in msg.fields:
            if key[1] not in attrs:
                attrs.append(key[1])
    except:
        pass