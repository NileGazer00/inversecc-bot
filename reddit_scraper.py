import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, SYMBOLS

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def fetch_recent_posts(subreddits=["CryptoCurrency", "wallstreetbets"], limit=50):
    results = []
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        for post in subreddit.hot(limit=limit):
            text = post.title + " " + (post.selftext or "")
            symbols_found = [s for s in SYMBOLS if s.replace("USDT", "") in text.upper()]
            if symbols_found:
                results.append({"text": text, "symbols": symbols_found})
            post.comments.replace_more(limit=5)
            for comment in post.comments.list()[:10]:
                comment_text = comment.body
                syms = [s for s in SYMBOLS if s.replace("USDT", "") in comment_text.upper()]
                if syms:
                    results.append({"text": comment_text, "symbols": syms})
    return results
