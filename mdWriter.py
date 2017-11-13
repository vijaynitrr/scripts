import urllib2
from bs4 import BeautifulSoup
import time
import sys
from os.path import expanduser

home = expanduser("~")

url = sys.argv[1]
openUrl = urllib2.urlopen(url)
page = openUrl.read()
soup = BeautifulSoup(page,"lxml")
soup.prettify()

ques_title = soup.find("h1", {"class":"entry-title"}).text

for tags in soup.findAll("div", { "class" : "entry-content" }):
    ques_desc = tags.find('p').text

timestr = time.strftime("%d-%m-%Y")
filename = home + "/Library/code-snippets/markdowns/" + timestr + ".md"

with open(filename, "a") as myfile:
    str = "\n\n" + "# " + ques_title + "\n\n" + ques_desc + "\n"
    str = str + "```sh" + "\n\n" + "```" + "\n"
    str = str + "[Full Code]" + "(" + url +")"
    myfile.write(str)
