# Data based parser
# Main plan for this parser is updating dataDict with new values if they are available
# In this way we don't need to parse for sentence type
# We are trying to get all data that we need and if its available we are updating dataDict
# If we are not able to get data we are using the last valid value

import pynmea2

dataDict = {}

null = ""

def parse(sentence):
    global dataDict 
    
    temp = sentence
    try:
        value = temp.split(",")[-1].split("*")[-1][:2]
        dataDict["Checksum"] = value if value != null else dataDict["Checksum"]
        print("Checksum Updated: " + str(temp.split(",")[-1].split("*")[-1][:2]))
    except: pass

    try: sentence = pynmea2.parse(sentence)
    except: return dataDict

    try: 
        value = sentence.sentence_type
        dataDict["Sentence Type"] = value if value != null else dataDict["Sentence Type"]
        print("Sentence Type Updated: " + sentence.sentence_type)
    except: pass
    try: 
        value = sentence.timestamp
        dataDict["UTC Time"] = value if value != null else dataDict["UTC Time"] 
        print("UTC Time Updated: " + str(sentence.timestamp))
    except: pass
    try: 
        value = sentence.latitude
        dataDict["Latitude"] = value if value != null else dataDict["Latitude"] 
        print("Latitude Updated: " + str(sentence.latitude))
    except: pass
    try: 
        value = sentence.longitude
        dataDict["Longitude"] = value if value != null else dataDict["Longitude"] 
        print("Longitude Updated: " + str(sentence.longitude))
    except: pass
    try: 
        value = sentence.gps_qual
        dataDict["GPS Quality"] = value if value != null else dataDict["GPS Quality"] 
        print("GPS Quality Updated: " + str(sentence.gps_qual))
    except: pass
    try: 
        value = sentence.num_sats
        dataDict["Number of Satellites"] = value if value != null else dataDict["Number of Satellites"]
        print("Number of Satellites Updated: " + str(sentence.num_sats))
    except: pass
    try: 
        value = sentence.horizontal_dil
        dataDict["Horizontal Dilution of Precision"] = value if value != null else dataDict["Horizontal Dilution of Precision"]
        print("Horizontal Dilution of Precision Updated: " + str(sentence.horizontal_dil))
    except: pass
    try: 
        value = sentence.altitude
        dataDict["Altitude"] = value if value != null else dataDict["Altitude"]
        print("Altitude Updated: " + str(sentence.altitude))
    except: pass
    try: 
        value = sentence.geo_sep
        dataDict["Geoidal Separation"] = value if value != null else dataDict["Geoidal Separation"]
        print("Geoidal Separation Updated: " + str(sentence.geo_sep))
    except: pass
    try: 
        value = sentence.age_gps_data
        dataDict["Age of GPS Data"] = value if value != null else dataDict["Age of GPS Data"]
        print("Age of Differential GPS Data Updated: " + str(sentence.age_gps_data))
    except: pass
    try: 
        value = sentence.ref_station_id
        dataDict["Reference Station ID"] = value if value != null else dataDict["Reference Station ID"]
        print("Differential Reference Station ID Updated: " + str(sentence.ref_station_id))
    except: pass

    return dataDict