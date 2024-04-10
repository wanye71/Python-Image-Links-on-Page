import requests
import os.path as path

from bs4 import BeautifulSoup

base_url = 'https://kennethreitz.org/nsfw'

def main():
    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    image_sources = [img.attrs['src'] for img in soup.find_all('img')]

    full_image_sources = [path.join(base_url, src) for src in image_sources]

    with open('images.txt', 'w') as f:
        f.write('\n'.join(full_image_sources))

if __name__ == '__main__':
     main()