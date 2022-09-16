# Data based parser
# Main plan for this parser is updating dataDict with new values if they are available
# In this way we don't need to parse for sentence type
# We are trying to get all data that we need and if its available we are updating dataDict
# If we are not able to get data we are using the last valid value

import pynmea2

dataDict = {}

def parse(sentence):
    global dataDict 
    
    try: sentence = pynmea2.parse(sentence)
    except: return dataDict

    try: dataDict["Sentence Type"] = sentence.sentence_type 
    except: pass
    try: dataDict["UTC Time"] = sentence.timestamp 
    except: pass
    try: dataDict["Latitude"] = sentence.latitude
    except: pass
    try: dataDict["Longitude"] = sentence.longitude
    except: pass
    try: dataDict["GPS Quality"] = sentence.gps_qual
    except: pass
    try: dataDict["Number of Satellites"] = sentence.num_sats
    except: pass
    try: dataDict["Horizontal Dilution of Precision"] = sentence.horizontal_dil
    except: pass
    try: dataDict["Altitude"] = sentence.altitude
    except: pass
    try: dataDict["Geoidal Separation"] = sentence.geo_sep
    except: pass
    try: dataDict["Age of Differential GPS Data"] = sentence.age_gps_data
    except: pass
    try: dataDict["Differential Reference Station ID"] = sentence.ref_station_id
    except: pass
    try: dataDict["Checksum"] = sentence.checksum
    except: pass
    try: dataDict["Checksum Valid"] = sentence.is_checksum_valid()
    except: pass
    try: dataDict["Checksum Calculated"] = sentence.calculate_checksum()
    except: pass

    return dataDict