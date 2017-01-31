import webbrowser

favUrls = ['http://www.infoworld.com/category/open-source-tools/','http://opensourceforu.com/','https://github.com/trending']

# Linux
chrome_path = '/usr/bin/google-chrome %s'

for url in favUrls:
    webbrowser.get(chrome_path).open_new_tab(url)
