import urllib
import urllib2
import BeautifulSoup
import re

Soup = BeautifulSoup.BeautifulSoup
keywords = ['Orange', 'Rainbow', 'Wolverine', 'Sushi',
            'Unicorn', 'Nuclear Reactor', 'Bon Jovi',
            'ColdPlay', 'Donald Trump', 'January']

def get_links(keywords):
    parsed_links = []
    for keyword in keywords:
        query = urllib.quote(keyword)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = Soup(html)

        for t in soup.findAll('h3', {'class': 'yt-lockup-title '}):
            a = t.findNext('a')
            text = a.findNext('span')
            duration = text.text
            res = re.search('[0-9]{1}[:][0-9]{2}', duration)
            if res and int(res.group(0)[0]) <= 6 and int(res.group(0)[0]) > 0:
                link = 'https://www.youtube.com' + a.get('href')
                parsed_links.append(str(link))
    return parsed_links

print get_links(keywords)
