from parsers import sentence_based_parser,data_based_parser

file = open("logs/nmea_sentences.log", "r")

result = []
for sentence in file.readlines():
    print("\n" +sentence)
    print(data_based_parser.parse(sentence))
    print()

for sentence in result:
    print(sentence)