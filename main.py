import parsers as parser

file = open("logs/simulator_sentences.log", "r")

for sentence in file.readlines():
    parser.parse(sentence)

file = open("logs/nmea_sentences.log", "r")
for sentence in file.readlines():
    parser.parse(sentence)

for key,item in parser.get_result().items():
    print(f"{key} : {item}")