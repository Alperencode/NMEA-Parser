import parsers

file = open("nmea_sentences.log", "r")

result = []
for sentence in file.readlines():
    result.append(parsers.parse(sentence))

for i in result:
    print(i)