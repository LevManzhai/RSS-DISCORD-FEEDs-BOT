import feedparser
import requests
from datetime import datetime
import re
import time
import os

RSS_URL = "https://www.hltv.org/rss/news"
WEBHOOK_URL = "https://discord.com/api/webhooks/1413694406594134087/jV_QsuriQjfDE6uAaSRhQbk98xR_gBUjl20HNJRjMj7I4A8j4Yae3QWAyyDUjCW1xowt"
COLOR = 0x7CFC00  # light green

LAST_NEWS_FILE = "last_news.txt"

def get_last_news_id():
    # Read the last saved news ID from file (to avoid reposting the same news)
    if os.path.exists(LAST_NEWS_FILE):
        with open(LAST_NEWS_FILE, "r", encoding="utf-8") as f:
            return f.read().strip() 
    return ""

def save_last_news_id(news_id):
    # Save the latest news ID to file
    with open(LAST_NEWS_FILE, "w", encoding="utf-8") as f:
        f.write(news_id)

def send_news(latest):
    # Extract title and link
    title = latest.title
    url = latest.link

    # Get image if available, otherwise use default HLTV icon
    if hasattr(latest, 'media_content') and latest.media_content:
        image_url = latest.media_content[0]['url']
    else:
        image_url = "https://www.hltv.org/img/static/hl-icon.png"

    # Extract summary text
    summary_text = latest.summary if hasattr(latest, 'summary') else ""

    # Try to find player quotes in the summary
    player_quote = ""
    match = re.search(r'([A-Za-z0-9]+):\s*“(.+?)”', summary_text)
    if match:
        player_quote = f"**{match.group(1)}:** \"{match.group(2)}\""

    # Clean summary text (remove quotes from players)
    news_text = re.sub(r'([A-Za-z0-9]+):\s*“(.+?)”', '', summary_text).strip()
    if news_text:
        news_text = f'“{news_text}”'

    # Format published time if available
    published_time = ""
    if hasattr(latest, 'published'):
        dt = datetime(*latest.published_parsed[:6])
        published_time = dt.strftime("%d.%m.%Y %H:%M")

    # Build description for Discord embed
    description = ""
    if player_quote:
        description += f"{player_quote}\n\n"
    description += news_text

    # Prepare the payload for Discord webhook
    data = {
        "username": "HLTV NEWS",
        "avatar_url": "https://www.hltv.org/img/static/hl-icon.png",  # avatar of the bot
        "embeds": [
            {
                "title": title,
                "url": url,
                "description": description,
                "color": COLOR,
                "image": {"url": image_url},
                "footer": {"text": f"hltv.org • {published_time}"}
            }
        ]
    }

    # Send request to Discord webhook
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"✅ News sent: {title}")
    else:
        print(f"❌ Error sending: {response.status_code}, {response.text}")

# Main loop
while True:
    feed = feedparser.parse(RSS_URL)
    if feed.entries:
        latest = feed.entries[0]
        last_id = get_last_news_id()
        if latest.link != last_id:
            send_news(latest)
            save_last_news_id(latest.link)
        else:
            print("⏳ No new news yet")
    else:
        print("❌ RSS is empty or unavailable")

    time.sleep(300)  # check every 5 minutes
