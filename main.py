from parsers import sentence_based_parser
from parsers import data_based_parser

file = open("logs/nmea_sentences.log", "r")

result = []
for sentence in file.readlines():
    print(data_based_parser.parse(sentence))

for sentence in result:
    print(sentence)