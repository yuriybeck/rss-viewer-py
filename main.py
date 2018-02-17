import os
import webbrowser
import writehtml
import rssreader

#prepare files
filename = 'myrss'
path = os.getcwd()
filepath = 'file://' + path + '/' + filename + '.html'
feed_url = 'https://www.heise.de/newsticker/heise-top-atom.xml'

#read feeds
rss_raw = rssreader.read_feeds(feed_url)
data = rssreader.prepare_feeds(rss_raw)
#create html
writehtml.create_html(filename, data)
#show feeds in the browser
webbrowser.open(filepath)
