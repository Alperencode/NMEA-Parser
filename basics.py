import pynmea2,parsers

unknown_sentences = []

for sentence in file.readlines():
    try:
        msg = pynmea2.parse(sentence)
        print(msg.sentence_type + " ", end='')
        print(f"{msg.data} - {len(msg.data)}")
    except:
        unknown_sentences.append(msg.sentence_type)
        