import webbrowser

favUrls = ['http://www.omgubuntu.co.uk','http://www.webupd8.org/','http://linuxscoop.com/','http://www.ubuntugeek.com','http://www.techdrivein.com/',
                'http://ubuntuhandbook.org/','https://www.unixmen.com/','http://linuxg.net/']

# Linux
chrome_path = '/usr/bin/google-chrome %s'

for url in favUrls:
    webbrowser.get(chrome_path).open_new_tab(url)
