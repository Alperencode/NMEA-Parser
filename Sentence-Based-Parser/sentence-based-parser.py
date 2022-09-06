import pynmea2

file = open('simulator_sentences.log', encoding='utf-8')

unknown_sentences = []

for sentence in file.readlines():
    try:
        msg = pynmea2.parse(sentence)
        print(msg.sentence_type + " ", end='')
        print(f"{msg.data} - {len(msg.data)}")
    except:
        unknown_sentences.append(msg.sentence_type)
        
print(f"\nUnknown sentences: {unknown_sentences}")
