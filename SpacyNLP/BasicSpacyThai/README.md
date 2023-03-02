## Basic Spacy NLP Tasks for Thai Language

First, install: 

```bash
pip install spacy-thai
```

Then run [example code](https://pypi.org/project/spacy-thai/): 

```python 
import spacy_thai
nlp=spacy_thai.load()
doc=nlp("แผนกนี้กำลังเผชิญกับความท้าทายใหม่")
for t in doc:
    print("\t".join([str(t.i+1),t.orth_,t.lemma_,t.pos_,t.tag_,"_",str(0 if t.head==t else t.head.i+1),t.dep_,"_","_" if t.whitespace_ else "SpaceAfter=No"]))

import deplacy
deplacy.render(doc,WordRight=True)
```

Output: 

![spacy_thai](https://user-images.githubusercontent.com/68504324/222329273-d696c6f3-f732-4736-b015-b5b8a85f8ac1.jpg)


### Basic Tasks

Here are Basic NLP Spacy using Thai language in Spacy:

1. Tokenization

```python
import spacy_thai
nlp=spacy_thai.load()
doc = nlp("สวัสดีครับ ยินดีต้อนรับสู่โลกของ NLP")
for token in doc:
    print(token.text)
```

Output:

```
สวัสดีครับ 
ยินดีต้อนรับ
สู่
โลก
ของ
NLP
```

2. POS tagging

```python
import spacy_thai
nlp=spacy_thai.load()
doc = nlp("สวัสดีครับ ยินดีต้อนรับสู่โลกของ NLP พระองค์ทรงเดินทางไปเมืองเชียงใหม่")
	
for token in doc:
    print(token.text, token.pos_)
```

Output:

```
สวัสดี NOUN
ครับ NOUN
ยินดีต้อนรับ VERB
สู่ ADP
โลก NOUN
ของ ADP
NLP NOUN
พระองค์ NOUN
ทรง NOUN
เดินทาง VERB
ไป AUX
เมือง VERB
เชียงใหม่ ADV
```


3. Named Entity Recognition

```python
import spacy_thai
nlp=spacy_thai.load()
doc = nlp("สวัสดีครับ ยินดีต้อนรับสู่โลกของ NLP พระองค์ทรงเดินทางไปเมืองเชียงใหม่")
	
doc = nlp("มหาวิทยาลัยมหิดลตั้งอยู่ที่เขตบางเขน กรุงเทพมหานคร")
for token in doc.ents:
    print(token.text, token.label_)
```

Output:

```
มหาวิทยาลัยมหิดล ORG
เขตบางเขน LOC
กรุงเทพมหานคร LOC
```

4. Dependency Parsing

```python
import spacy_thai
nlp=spacy_thai.load()

doc = nlp("ต้นไม้ในสวนเราเป็นต้นไม้ที่โตช้า")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
```

Output:

```css
ต้นไม้ nsubj โตช้า VERB []
ใน case สวน NOUN []
สวน obl เป็น AUX [ต้นไม้, ใน]
เรา nsubj เป็น AUX []
เป็น ROOT เป็น AUX [สวน, ที่, โตช้า]
ต้นไม้ dobj เป็น AUX []
ที่ det โตช้า VERB []
โตช้า advcl เป็น AUX [ที่]
```

