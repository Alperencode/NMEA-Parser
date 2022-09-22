from parsers import sentence_based_parser,data_based_parser

file = open("logs/simulator_sentences.log", "r")

for sentence in file.readlines():
    print("\n" +sentence)
    print(data_based_parser.parse(sentence))
    print()

for item,key in data_based_parser.dataDict.items():
    print(item + ": " + str(key))

file = open("logs/nmea_sentences.log", "r")

for sentence in file.readlines():
    print("\n" +sentence)
    print(data_based_parser.parse(sentence))
    print()

for item,key in data_based_parser.dataDict.items():
    print(item + ": " + str(key))

print(f"\nValid Sentences: {set(data_based_parser.valid_sentences)}\n")
print(f"Less Valid Sentences: {set(data_based_parser.less_valid_sentences)}\n")
print(f"Unknown Sentences: {set(data_based_parser.unknown_sentences)}\n")
print(f"Data Gathered: {set(data_based_parser.data_gathered)}\n")