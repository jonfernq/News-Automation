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
