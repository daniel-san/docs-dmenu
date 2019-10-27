import requests
import sys
from bs4 import BeautifulSoup

languages = {
    'laravel': {
        'url': 'https://laravel.com/api/',
        'default': '6.x',
    },
    'python': {}
}

slug = sys.argv[1].split(':')

(language, version) = [slug[0], None] if len(slug) < 2 else slug

docs_url = languages[language]['url']

if not version:
    version = languages[language]['default']

docs = requests.get(docs_url + version + '/')

soup = BeautifulSoup(docs.text, 'html.parser')

docs = soup.find('div', { 'class': 'namespace-container' })

links = docs.find_all('a')

for l in links:
    print(docs_url + version + '/' + l.attrs['href'])
