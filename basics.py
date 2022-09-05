import pynmea2

file = open('simulator_sentences.log', encoding='utf-8')

for sentence in file.readlines():
    try:
        msg = pynmea2.parse(sentence,check=False)
        print(msg.lat)
    except:
        print(f"No attributes")