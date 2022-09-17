# Data based parser
# Main plan for this parser is updating dataDict with new values if they are available
# In this way we don't need to parse for sentence type
# We are trying to get all data that we need and if its available we are updating dataDict
# If we are not able to get data we are using the last valid value

import pynmea2

dataDict = {}

def parse(sentence):
    global dataDict 
    
    temp = sentence
    try:
        dataDict["Checksum"] = temp.split(",")[-1].split("*")[-1][:2]
        print("Checksum Updated: " + str(temp.split(",")[-1].split("*")[-1][:2]))
    except: pass

    try: sentence = pynmea2.parse(sentence)
    except: return dataDict

    try: 
        dataDict["Sentence Type"] = sentence.sentence_type
        print("Sentence Type Updated: " + sentence.sentence_type)
    except: pass
    try: 
        dataDict["UTC Time"] = sentence.timestamp
        print("UTC Time Updated: " + str(sentence.timestamp))
    except: pass
    try: 
        dataDict["Latitude"] = sentence.latitude
        print("Latitude Updated: " + str(sentence.latitude))
    except: pass
    try: 
        dataDict["Longitude"] = sentence.longitude
        print("Longitude Updated: " + str(sentence.longitude))
    except: pass
    try: 
        dataDict["GPS Quality"] = sentence.gps_qual
        print("GPS Quality Updated: " + str(sentence.gps_qual))
    except: pass
    try: 
        dataDict["Number of Satellites"] = sentence.num_sats
        print("Number of Satellites Updated: " + str(sentence.num_sats))
    except: pass
    try: 
        dataDict["Horizontal Dilution of Precision"] = sentence.horizontal_dil
        print("Horizontal Dilution of Precision Updated: " + str(sentence.horizontal_dil))
    except: pass
    try: 
        dataDict["Altitude"] = sentence.altitude
        print("Altitude Updated: " + str(sentence.altitude))
    except: pass
    try: 
        dataDict["Geoidal Separation"] = sentence.geo_sep
        print("Geoidal Separation Updated: " + str(sentence.geo_sep))
    except: pass
    try: 
        dataDict["Age of Differential GPS Data"] = sentence.age_gps_data
        print("Age of Differential GPS Data Updated: " + str(sentence.age_gps_data))
    except: pass
    try: 
        dataDict["Differential Reference Station ID"] = sentence.ref_station_id
        print("Differential Reference Station ID Updated: " + str(sentence.ref_station_id))
    except: pass

    return dataDict