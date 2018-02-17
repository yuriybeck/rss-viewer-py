import lib.feedparser
import urllib2
import json

def read_feeds(feed_url):
    rss_feed = lib.feedparser.parse(feed_url)
    return rss_feed

def read_feed_from_url(feed_url):
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    return data

def prepare_feeds(rss_data):
    entries = []
    #print rss_data['entries']
    for item in rss_data['entries']:
        content = (str(item['title'].encode('utf-8')), str(item['summary'].encode('utf-8')))
        entries.append(content)
    return entries
