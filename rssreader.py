import feedparser

def read_feeds(feed_url):
    rss_feed = feedparser.parse(feed_url)
    return rss_feed

def prepare_feeds(rss_feeds):
    entries = []
    for feed in rss_feeds:
        entries.extend(feed['items'])
    return entries
