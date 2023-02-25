## Thai Interlinear Translation 

An 'interlinear translation' or 'gloss' is a word-by-word translation of a text. 

More precisely, it is defined as the insertion after (or below) the words of a foreign language text,
of equivalent words (or definitions of words) in one's native language.

It allows the reader to read a word, see the translation, read the next word, see the translation, and so on. 

It provides an aid for reading foreign language texts, saving time by automating the look-up of words in the dictionary. 

As Wikipedia observes: 

"...glosses help the reader follow the relationship between 
the source text and its translation, and the structure of the original language. 
In its simplest form, an interlinear gloss is simply a literal, word-for-word translation of the source text." 
(Source: [Wikipedia](https://en.wikipedia.org/wiki/Interlinear_gloss))

### Simple Gloss

The code for simple glossing from Thai to English is provided below.

This code uses the first definition or [synset](https://en.wikipedia.org/wiki/Synset) from [WordNet](https://en.wikipedia.org/wiki/WordNet). 

To get more accurate glossing more involved [word sense disambiguation (WSD)](https://en.wikipedia.org/wiki/Word-sense_disambiguation)  must be done as well, identifying which exact sense of a word is meant by each word in a sentence. 

- [thai_interlinear_snippet.py](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/thai_interlinear_snippet.py): Inserting English definition in parentheses after the Thai word in the text, after first word segmentation on Thai language text, then English gloss/translation lookup on the segmented words.
- [make_interlinear_function.py](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/make_interlinear_function.py): Glossing (in the above) made into a function.  
-[make_interlinear_directory.py](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/make_interlinear_directory.py): Creates Thai glossed to English files for all files in a directory, by using a function: apply_function_to_files_in_directory.
- [thai_news_summary.txt](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/thai_news_summary.txt): A sample whole directory of Thai language files glossed to English copied into one text file. 
