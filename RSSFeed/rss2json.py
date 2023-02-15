# rss2json.py - 
# retrieve an online RSS feed and convert to JSON format  

import feedparser
import json

# Parse the VOA Thai language RSS feed
rss_url = "https://www.voathai.com/api/zvkyieomv_"
feed = feedparser.parse(rss_url)

# Convert the parsed feed data to a list of dictionaries
entries = feed.entries

# Save the parsed feed data as a JSON file with indentation
with open('voa_thai_feed.json', 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=4)
    
