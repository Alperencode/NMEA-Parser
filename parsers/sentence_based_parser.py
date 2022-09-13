# Sentence type based parser

def parseGGA(sentence):
    datadict = {}
    sentence = sentence.split(',')
    datadict['sentence_type'] = sentence[0][3:] if sentence[0] != "" else None
    datadict['utc_time'] = sentence[1][:2] + ":" + sentence[1][2:4] + ":" + sentence[1][4:] if sentence[1] != "" else None
    datadict['latitude'] = sentence[2] if sentence[2] != "" else None
    datadict['lat_direction'] = sentence[3] if sentence[3] != "" else None
    datadict['longitude'] = sentence[4] if sentence[4] != "" else None
    datadict['lon_direction'] = sentence[5] if sentence[5] != "" else None
    datadict['gps_quality'] = sentence[6] if sentence[6] != "" else None
    datadict['num_sats'] = sentence[7] if sentence[7] != "" else None
    datadict['horizontal_dil'] = sentence[8] if sentence[8] != "" else None
    datadict['antenna_alt'] = sentence[9] if sentence[9] != "" else None
    datadict['antenna_alt_units'] = sentence[10] if sentence[10] != "" else None
    datadict['geoidal_sep'] = sentence[11] if sentence[11] != "" else None
    datadict['geoidal_sep_units'] = sentence[12] if sentence[12] != "" else None
    datadict['age_gps_data'] = sentence[13] if sentence[13] != "" else None
    datadict['ref_station_id'] = sentence[14].split("*")[0] if sentence[14] != "" else None
    datadict['checksum'] = sentence[14].split("*")[1][:2] if sentence[14] != "" else None
    return datadict

def parseGLL(sentence):
    datadict = {}
    sentence = sentence.split(',')
    datadict['sentence_type'] = sentence[0][3:] if sentence[0] != "" else None
    datadict['latitude'] = sentence[1] if sentence[1] != "" else None
    datadict['lat_direction'] = sentence[2] if sentence[2] != "" else None
    datadict['longitude'] = sentence[3] if sentence[3] != "" else None
    datadict['lon_direction'] = sentence[4] if sentence[4] != "" else None
    datadict['utc_time'] = sentence[5][:2] + ":" + sentence[5][2:4] + ":" + sentence[5][4:] if sentence[5] != "" else None
    datadict['status'] = sentence[6].split("*")[0] if sentence[6] != "" else None
    datadict['checksum'] = sentence[6].split("*")[1][:2] if sentence[6] != "" else None
    return datadict

def parseRMC(sentence):
    datadict = {}
    sentence = sentence.split(',')
    datadict['sentence_type'] = sentence[0][3:] if sentence[0] != "" else None
    datadict['utc_time'] = sentence[1][:2] + ":" + sentence[1][2:4] + ":" + sentence[1][4:] if sentence[1] != "" else None
    datadict['status'] = sentence[2] if sentence[2] != "" else None
    datadict['latitude'] = sentence[3] if sentence[3] != "" else None
    datadict['lat_direction'] = sentence[4] if sentence[4] != "" else None
    datadict['longitude'] = sentence[5] if sentence[5] != "" else None
    datadict['lon_direction'] = sentence[6] if sentence[6] != "" else None
    datadict['speed_over_ground'] = sentence[7] if sentence[7] != "" else None
    datadict['course_over_ground'] = sentence[8] if sentence[8] != "" else None
    datadict['date'] = sentence[9][:2] + "/" + sentence[9][2:4] + "/" + sentence[9][4:] if sentence[9] != "" else None
    datadict['mag_variation'] = sentence[10] if sentence[10] != "" else None
    datadict['mag_var_direction'] = sentence[11] if sentence[11] != "" else None
    datadict['checksum'] = sentence[12].split("*")[1][:2] if sentence[12] != "" else None
    return datadict

def parseHDM(sentence):
    datadict = {}
    sentence = sentence.split(',')
    datadict['sentence_type'] = sentence[0][3:] if sentence[0] != "" else None
    datadict['heading'] = sentence[1] if sentence[1] != "" else None
    datadict['checksum'] = sentence[2].split("*")[1][:2] if sentence[2] != "" else None
    return datadict

def parseHDT(sentence):
    datadict = {}
    sentence = sentence.split(',')
    datadict['sentence_type'] = sentence[0][3:] if sentence[0] != "" else None
    datadict['heading'] = sentence[1] if sentence[1] != "" else None
    datadict['checksum'] = sentence[2].split("*")[1][:2] if sentence[2] != "" else None
    return datadict

def parse(sentence):
    sentence_type = sentence.split(',')[0][3:]
    if sentence_type == 'GGA':
        return parseGGA(sentence)
    elif sentence_type == 'GLL':
        return parseGLL(sentence)
    elif sentence_type == 'RMC':
        return parseRMC(sentence)
    elif sentence_type == 'HDM':
        return parseHDM(sentence)
    elif sentence_type == 'HDT':
        return parseHDT(sentence)
    else:
        return "Unknown sentence type"