import pythainlp, sys 
from pythainlp.corpus import wordnet

text = "วันนี้เราไปเที่ยวที่สวนสนุก"
words = pythainlp.word_tokenize(text)

sys.stdout = open('interlinear.txt', 'w', encoding='utf-8') 

for word in words:
    synsets = wordnet.synsets(word)
    if synsets:
        definition = synsets[0].definition()
        print(f"{word} ({definition})")
    else:
        print(word)
