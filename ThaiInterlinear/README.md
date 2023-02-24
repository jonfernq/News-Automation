## Thai Interlinear Translation 

Glossing or inserting the English definitions after the Thai words of a Thai text is one form of interlinear translation.
This sort of translation helps language learners read texts in the language they are learning.
It saves them the time of looking up words in the dictionary. 

An interlinear translation or gloss is defined more precisely as follows: 

"In linguistics and pedagogy, an interlinear gloss is a gloss 
(series of brief explanations, such as definitions or pronunciations) placed between lines, 
such as between a line of original text and its translation into another language. 
When glossed, each line of the original text acquires one or more corresponding lines 
of transcription known as an interlinear text or interlinear glossed text (IGT)—
interlinear for short. Such glosses help the reader follow the relationship between 
the source text and its translation, and the structure of the original language. 
In its simplest form, an interlinear gloss is simply a literal, word-for-word translation of the source text." 
(Source: [Wikipedia](https://en.wikipedia.org/wiki/Interlinear_gloss))

### Simple Gloss

Code for simple glossing is provided below that uses the first definition or [synset](https://en.wikipedia.org/wiki/Synset) from [WordNet](https://en.wikipedia.org/wiki/WordNet). To get more accurate glossing more involved [word sense disambiguation (WSD)](https://en.wikipedia.org/wiki/Word-sense_disambiguation), identifying which sense of a word is meant in a sentence, must be done as well. 

- [thai_interlinear_snippet.py](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/thai_interlinear_snippet.py): Inserting English definition in parentheses after the Thai word in the text, after first word segmentation on Thai language text, then English gloss/translation lookup on the segmented words.
- [make_interlinear_function.py](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/make_interlinear_function.py): Glossing (in the above) made into a function.  
-[make_interlinear_directory.py](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/make_interlinear_directory.py): Creates Thai glossed to English files for all files in a directory, by using a function: apply_function_to_files_in_directory.
- [thai_news_summary.txt](https://github.com/jonfernq/News-Automation/blob/main/ThaiInterlinear/thai_news_summary.txt): A sample whole directory of Thai language files glossed to English copied into one text file. 
