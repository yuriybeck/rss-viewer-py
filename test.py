import urllib2
import json


url = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fnews.ycombinator.com%2Frss"

response = urllib2.urlopen(url)

data = json.loads(response.read());


print '====== ' + data['status'] + ' ======';

for item in data['items']:
    print item['title']
