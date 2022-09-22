from parsers import sentence_based_parser,data_based_parser

file = open("logs/nmea_sentences.log", "r")

for sentence in file.readlines():
    data_based_parser.parse(sentence)

file = open("logs/simulator_sentences.log", "r")

for sentence in file.readlines():
    data_based_parser.parse(sentence)

for item in data_based_parser.attrs:
    print(item)