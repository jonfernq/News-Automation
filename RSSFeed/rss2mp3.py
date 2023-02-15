# rss2mp3.py - 
# choose an VOA news in Thai language RSS feed,
# then choose a story in the feed,
# then write text to .txt file
# and make text-to-speech MP3 audio file 

import inquirer, feedparser, json, os 
from datetime import datetime
from gtts import gTTS

# Define the list of VOA RSS feeds for Southeast Asia
rss_feeds = [
    {
        'name': 'VOA US & Thai News in Thai',
        'url': 'https://www.voathai.com/api/zykyoeqmvp',
    },
    {
        'name': 'VOA Business News in Thai',
        'url': 'https://www.voathai.com/api/zvkyieomv_',
    },    
    {
        'name': 'VOA Asia News in Thai',
        'url': 'https://www.voathai.com/api/ztqt_eikty', 
    },
    {
        'name': 'VOA Science/Health News in Thai',
        'url': 'https://www.voathai.com/api/z-kyrevmvo',
    },
    {
        'name': 'VOA Tech/Innovation News in Thai',
        'url': 'https://www.voathai.com/api/zbkyqetmvi',
    },
    {
        'name': 'VOA Society/Education News in Thai',
        'url': 'https://www.voathai.com/api/ztkypeimvy',
    },
    {
        'name': 'VOA Entertainment/Lifestyle News in Thai',
        'url': 'https://www.voathai.com/api/zukymepmvv',
    },
]

def make_filename(title):
    # Replace spaces with underscores
    filename = title.replace(' ', '_')
    # Append "_rss" and add the ".xml" file extension
    filename = f"{filename}_rss.xml"
    return filename

# Define the prompt for selecting an RSS feed
rss_feed_prompt = [
    inquirer.List('rss_feed',
                  message='Select an RSS feed:',
                  choices=[(str(i+1) + '. ' + feed['name'], feed) for i, feed in enumerate(rss_feeds)],
                  carousel=True),
]

# Get the selected RSS feed from the user
selected_feed = None
while not selected_feed:
    answers = inquirer.prompt(rss_feed_prompt)
    if answers['rss_feed'] == 'exit':
        exit(0)
    selected_feed = answers['rss_feed']  

# Read the RSS feed and write it to an XML file
feed = feedparser.parse(selected_feed['url'])

with open(make_filename(selected_feed['name']), 'w', encoding='utf-8') as f:
    json.dump(feed, f, ensure_ascii=False, indent=4)

# Make a list of article titles, dates, and descriptions
items = feed.entries
titles = [(item.title, datetime.strptime(item.published, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d'), item.summary) for item in items]

# Define the prompt for selecting an article
article_prompt = [
    inquirer.List('article',
                  message='Select an article:',
                  choices=[(str(i+1) + '. ' + item.title, item) for i, item in enumerate(items)],
                  carousel=True),
]

# Get the selected article from the user
selected_article = None
while not selected_article:
    answers = inquirer.prompt(article_prompt)
    if answers['article'] == 'exit':
        exit(0)
    selected_article = answers['article']

# Concatenate the article title and description
article_text = selected_article.title + '\n\n' + selected_article.summary
print('article_text: ', article_text)
 
# Write the article text to a text file and convert it to an MP3 file
filename = selected_article.title + '_' + selected_article.published[:10] + '.txt'
with open(filename, 'w', encoding='utf-8') as f: 
    f.write(article_text)

print('CONVERTING TO AUDIO') 
audio = gTTS(text=article_text, lang="th", slow=True) 
save_filename = filename[:-3] + 'mp3' 
audio.save(save_filename)   
#tts = gTTS(article_text)
#tts.save(filename[:-3] + 'mp3')

# Display a message indicating success
print('Article written to file: ' + filename[:-3] + 'txt and ' + filename[:-3] + 'mp3')

