import urllib2
import timestr
import test2
from bs4 import BeautifulSoup
import time
import sys
import re

url = sys.argv[1]
openUrl = urllib2.urlopen(url)
page = openUrl.read()
soup = BeautifulSoup(page,"lxml")
soup.prettify()

ques_title = soup.find("h1", {"class":"entry-title"}).text

for tags in soup.findAll("div", { "class" : "entry-content" }):
    ques_desc = tags.find('p').text

ans = soup.findAll("pre")[1].text

def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return "" # note: a space and not an empty string
        else:
            return s

    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

#print ans
result = comment_remover(ans)
print result
sys.exit()

timestr = time.strftime("%d-%m-%Y")
filename = "/home/vijay/Library/code-snippets/markdowns/" + timestr + ".md"

with open(filename, "a") as myfile:
    str = "\n\n" + "# " + ques_title + "\n\n" + ques_desc + "\n"
    str = str + "```sh" + "\n\n" + ans + "```" + "\n"
    str = str + "[Full Code]" + "(" + url +")"
    myfile.write(str)
