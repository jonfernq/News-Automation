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
