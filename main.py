import parsers

file = open("logs/nmea_sentences.log", "r")

result = []
for sentence in file.readlines():
    result.append(parsers.parse(sentence))

for sentence in result:
    print(sentence)