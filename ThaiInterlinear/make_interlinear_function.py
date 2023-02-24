import pythainlp, sys 
from pythainlp.corpus import wordnet

def make_interlinear(txt):
    words = pythainlp.word_tokenize(txt)

    iltxt = ""
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            definition = synsets[0].definition()
            iltxt = iltxt + f"{word} ({definition}) "
        else:
            iltxt = iltxt + word + ' ' 
    return iltxt 
		
txt = "วันนี้เราไปเที่ยวที่สวนสนุก"
iltxt = make_interlinear(txt)

sys.stdout = open('iltxt.txt', 'w', encoding='utf-8')
print(iltxt)  
		
