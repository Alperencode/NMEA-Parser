# Data based parser
# Main plan for this parser is updating dataDict with new values if they are available
# In this way we don't need to parse for sentence type
# We are trying to get all data that we need and if its available we are updating dataDict
# If we are not able to get data we are using the last valid value

import pynmea2

dataDict = {}
unknown_sentences,valid_sentences, less_valid_sentences, data_gathered = [], [], [], []

null = ""

def parse(sentence):
    global dataDict
    valid_data = 0 
    
    temp = sentence
    try:
        value = temp.split(",")[-1].split("*")[-1][:2]
        dataDict["Checksum"] = value if value != null else dataDict["Checksum"]
        print("Checksum Updated: " + str(temp.split(",")[-1].split("*")[-1][:2]))
        valid_data += 1
    except: pass

    try: 
        sentence = pynmea2.parse(sentence)
    except: 
        unknown_sentences.append(sentence.split(",")[0][3:])
        return dataDict

    try: 
        value = sentence.sentence_type
        dataDict["Sentence Type"] = value if value != null else dataDict["Sentence Type"]
        data_gathered.append("Sentence Type")
        print("Sentence Type Updated: " + sentence.sentence_type)
        valid_data += 1
    except: pass
    try: 
        value = sentence.timestamp
        dataDict["UTC Time"] = value if value != null else dataDict["UTC Time"] 
        data_gathered.append("UTC Time")
        print("UTC Time Updated: " + str(sentence.timestamp))
        valid_data += 1
    except: pass
    try: 
        value = sentence.latitude
        dataDict["Latitude"] = value if value != null else dataDict["Latitude"] 
        data_gathered.append("Latitude")
        print("Latitude Updated: " + str(sentence.latitude))
        valid_data += 1
    except: pass
    try: 
        value = sentence.longitude
        dataDict["Longitude"] = value if value != null else dataDict["Longitude"] 
        data_gathered.append("Longitude")
        print("Longitude Updated: " + str(sentence.longitude))
        valid_data += 1
    except: pass
    try: 
        value = sentence.gps_qual
        data_gathered.append("GPS Quality")
        dataDict["GPS Quality"] = value if value != null else dataDict["GPS Quality"] 
        print("GPS Quality Updated: " + str(sentence.gps_qual))
        valid_data += 1
    except: pass
    try: 
        value = sentence.num_sats
        dataDict["Number of Satellites"] = value if value != null else dataDict["Number of Satellites"]
        data_gathered.append("Number of Satellites")
        print("Number of Satellites Updated: " + str(sentence.num_sats))
        valid_data += 1
    except: pass
    try: 
        value = sentence.horizontal_dil
        dataDict["Horizontal Dilution of Precision"] = value if value != null else dataDict["Horizontal Dilution of Precision"]
        data_gathered.append("Horizontal Dilution of Precision")
        print("Horizontal Dilution of Precision Updated: " + str(sentence.horizontal_dil))
        valid_data += 1
    except: pass
    try: 
        value = sentence.altitude
        dataDict["Altitude"] = value if value != null else dataDict["Altitude"]
        data_gathered.append("Altitude")
        print("Altitude Updated: " + str(sentence.altitude))
        valid_data += 1
    except: pass
    try: 
        value = sentence.geo_sep
        dataDict["Geoidal Separation"] = value if value != null else dataDict["Geoidal Separation"]
        data_gathered.append("Geoidal Separation")
        print("Geoidal Separation Updated: " + str(sentence.geo_sep))
        valid_data += 1
    except: pass
    try: 
        value = sentence.age_gps_data
        dataDict["Age of GPS Data"] = value if value != null else dataDict["Age of GPS Data"]
        data_gathered.append("Age of GPS Data")
        print("Age of Differential GPS Data Updated: " + str(sentence.age_gps_data))
        valid_data += 1
    except: pass
    try: 
        value = sentence.ref_station_id
        dataDict["Reference Station ID"] = value if value != null else dataDict["Reference Station ID"]
        data_gathered.append("Reference Station ID")
        print("Differential Reference Station ID Updated: " + str(sentence.ref_station_id))
        valid_data += 1
    except: pass
    try:
        value = sentence.true_course
        dataDict["True Course"] = value if value != null else dataDict["True Course"]
        data_gathered.append("True Course")
        print("True Course Updated: " + str(sentence.true_course))
        valid_data += 1
    except: pass

    if valid_data > 2:
        valid_sentences.append(sentence.sentence_type)
    else:
        less_valid_sentences.append(sentence.sentence_type)
    return dataDict