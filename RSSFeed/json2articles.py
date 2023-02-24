import json

with open('voa_thai_feed.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

for article in articles:
    title = article['title']
    published = article['published']
    summary = article['summary']

    # Replace any characters in the title that can't be used in a filename
    title = title.replace('/', '-').replace('\\', '-')

    # Write out the article to a file with the title as the filename
    with open(f'{title}.txt', 'w', encoding='utf-8') as out_file:
        out_file.write(f'Title: {title}\n')
        out_file.write(f'Published: {published}\n\n')
        out_file.write(summary)
        
"""
This code assumes that the news articles are stored in a JSON file called news_articles.json. It reads in the JSON file and stores the list of articles in the articles variable.

The code then iterates over each article in the list and extracts the title, published, and summary fields. It replaces any characters in the title that can't be used in a filename (e.g. /, \) and uses the title as the filename for the output text file.

Finally, the code opens the output text file and writes out the title, publication date, and summary of the article in the specified format. Note that the output text file is encoded in UTF-8 to support non-ASCII characters.

"""
