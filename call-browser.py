import os
import webbrowser
import writehtml

filename = 'helloworld2'

path = os.getcwd()
print(path)

filepath = 'file://' + path + '/' + filename + '.html'

writehtml.create_html(filename)
webbrowser.open(filepath)
