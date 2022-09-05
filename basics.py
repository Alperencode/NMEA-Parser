import pynmea2

file = open('nmea_sentences.log', encoding='utf-8')

for sentence in file.readlines():
    try:
        nmea_msg = pynmea2.parse(sentence)
        print(repr(nmea_msg))
    except pynmea2.ParseError as e:
        print(f"Couldn't parse {sentence}")
        continue