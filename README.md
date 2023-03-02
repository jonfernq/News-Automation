## News-Automation
Automate digital news production workflow using Python multimedia and AI packages.

I worked for 11 years for the Bangkok Post crafting the news for Thai English learners.

The reverse approach is taken here, namely crafting the Thai news for Thai language learners. 

### RSS Feeds (for VOA Thai News)

- [rss2json.py](https://github.com/jonfernq/News-Automation/blob/main/RSSFeed/rss2json.py): Retrieve an online RSS feed and convert to JSON format. 
- [voa_thai_feed.json](https://github.com/jonfernq/News-Automation/blob/main/RSSFeed/voa_thai_feed.json): VOA Thai News RSS feed converted to JSON format.  
- [json2articles.py](https://github.com/jonfernq/News-Automation/blob/main/RSSFeed/json2articles.py): Extracting news articles from JSON RSS feed file and writing to text files.  

### Text-to-Speech Audio for Thai News 

- [rss2mp3.py](https://github.com/jonfernq/News-Automation/blob/main/RSSFeed/rss2mp3.py): Choose an VOA news in Thai language RSS feed, then choose a story in the feed, then write text to .txt file, and make text-to-speech MP3 audio file. 

### News for Learning Thai

- [Thai Interlinear](https://github.com/jonfernq/News-Automation/tree/main/ThaiInterlinear): Inserting English definitions in parentheses after Thai words in a Thai text.  

![thaiinterlinear1](https://user-images.githubusercontent.com/68504324/221129655-a031570b-b623-48ff-913d-90fc30bff9fa.jpg)
  
### Research into News Issues

#### Extrajudicial Killing during the 2016 Philippine 'War on Drugs': 

- [Data Analysis](https://github.com/jonfernq/Extrajudicial-Killing-Philippines)

### Spacy NLP 

Spacy is an open-source software library for advanced Natural Language Processing (NLP) tasks in Python. 

- [Basic Spacy Tasks for English](https://github.com/jonfernq/News-Automation/tree/main/SpacyNLP/BasicSpacyEnglish) 

- [Basic Spacy Tasks for Thai](https://github.com/jonfernq/News-Automation/tree/main/SpacyNLP/BasicSpacyThai) 

### Paraphrasing & Similarity

A news story often has to paraphrase descriptions of events from other news stories.

Python has packages to both paraphrase and check for similarity of the paraphrase to other texts (an undesirable quality known as 'plagiarism').

- [TurnitinFree](https://github.com/SegYT/turnitinFree) - Reports a percentage similarity score for a text by searching for matching texts on the internet, 
much like the popular plagiarism checker [Turnitin](https://en.wikipedia.org/wiki/Turnitin).

In the example below I checked a near perfect paraphrase from ChatGPT (0% similarity) with text copied directly from Wikipedia (100% similarity):

![turnitin](https://user-images.githubusercontent.com/68504324/222352765-faf64a6c-8b54-4bf0-85fe-1492f060bed3.jpg)

