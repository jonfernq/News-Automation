## Basic Spacy NLP Tasks for English Language 

Easy tasks and code snippets to get started with using Spacy in Python:

1. Tokenization is the process of splitting a text into individual units such as words or punctuation marks. Spacy's tokenizer can be used as follows:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

text = "This is an example sentence."

doc = nlp(text)

for token in doc:
    print(token.text)
```

2. Part-of-Speech (POS) Tagging:

POS tagging is the process of labeling each word in a text with its corresponding part of speech such as noun, verb, adjective, etc. Spacy's POS tagger can be used as follows:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

text = "This is an example sentence."

doc = nlp(text)

for token in doc:
    print(token.text, token.pos_)
```

3. Named Entity Recognition (NER):

NER is the process of extracting entities such as names, organizations, and locations from a text. Spacy's NER can be used as follows:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple is looking at buying U.K. startup for $1 billion"

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
```

4. Dependency Parsing:

Dependency parsing is the process of analyzing the grammatical structure of a sentence to determine the relationships between words. Spacy's dependency parser can be used as follows:

```python
import spacy

nlp = spacy.load("en_core_web_sm")

text = "This is an example sentence."

doc = nlp(text)

for token in doc:
    print(token.text, token.dep_)
```

These are just a few examples of what Spacy can do. There are many more tasks and features available in Spacy, such as text classification, word vectors, and custom models.
