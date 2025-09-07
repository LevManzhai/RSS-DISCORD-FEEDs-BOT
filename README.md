# HLTV NEWS Discord Bot

## 📌 What does this script do?
This Python script fetches the latest news from an RSS feed (by default, [HLTV.org](https://www.hltv.org/)) and automatically sends them to a **Discord channel** using a webhook.  
The bot formats the message with:
- Title (clickable link to the article)
- Description (including player quotes if available)
- News image
- Publish date and time  

This way, you always have the latest news in your Discord server.

---

## 🔄 Can I use it with other RSS feeds?
Yes ✅  
You can use **any RSS feed URL**, not just HLTV.  
To change the feed, edit this line in the script:
```python
RSS_URL = "https://www.hltv.org/rss/news"
```
Replace it with the RSS link of any website, blog, or service that provides RSS.

---

## ⚙️ Installation Guide

### 1. Install Python
Download and install Python 3.8+.
Make sure Python and pip are added to your system PATH.

To verify installation, run in terminal:
```bash
python --version
pip --version
```

### 2. Install dependencies
In your terminal, install required Python libraries:
```bash
pip install feedparser requests
```

### 3. Get the script
Download or clone this repository:
```bash
git clone https://github.com/your-username/hltv-news-bot.git
cd hltv-news-bot
```
Or simply download the file `hltv_news.py` to your computer.

### 4. Create a Discord webhook
1. Open your Discord server.  
2. Go to **Server Settings → Integrations → Webhooks**.  
3. Create a new webhook, choose a channel, and copy the Webhook URL.  
4. Paste it into the script:
```python
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_here"
```

### 5. (Optional) Customize the bot
You can change:

- **RSS feed source:**
```python
RSS_URL = "https://www.hltv.org/rss/news"
```

- **Bot name and avatar:**
```python
"username": "HLTV NEWS",
"avatar_url": "https://i.imgur.com/your_custom_avatar.png"
```
(The avatar must be a direct image URL, not a local file.)

- **Embed color (default = green 0x7CFC00):**
```python
COLOR = 0x7CFC00
```

### 6. Run the bot
In the project folder, run:
```bash
python hltv_news.py
```

The bot will:
- Check the RSS feed every 5 minutes.  
- Send the newest article to Discord if it hasn’t been posted yet.  
- Save the last posted article in `last_news.txt` to prevent duplicates.  
- Print log messages in your terminal (e.g., “✅ News sent” or “⏳ No new news yet”).  

---

## 🎨 Example output in Discord
- **Title** → clickable link to the article.  
- **Description** → short summary with player quotes.  
- **Image** → article image or HLTV default icon.  
- **Footer** → publish date and time.  

---

## 📸 Screenshots

### Discord вывод
![News in discors](screenshot1.png)



## 🖥️ Notes
Keep the script running if you want it to continuously fetch and send news.

You can host it on:
- Your local machine  
- A VPS or dedicated server  
- Cloud services like Railway, Heroku, or Docker  

The file `last_news.txt` must stay in the same directory as the script.

---

## ✅ Summary
1. Install Python and dependencies.  
2. Create a Discord webhook.  
3. Set your `WEBHOOK_URL` in the script.  
4. (Optional) Change `RSS_URL`, bot name, or avatar.  
5. Run the script → news goes straight to your Discord! 🚀
