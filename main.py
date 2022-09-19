from parsers import sentence_based_parser,data_based_parser

file = open("logs/nmea_sentences.log", "r")

for sentence in file.readlines():
    print("\n" +sentence)
    print(data_based_parser.parse(sentence))
    print()

for item,key in data_based_parser.dataDict.items():
    print(item + ": " + str(key))