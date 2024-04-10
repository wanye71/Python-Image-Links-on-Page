## Get image links on page

## Testing in Ptpython Repl
```console
ptpython

>>> import requests
>>>
>>> response = requests.get("https://kennethreitz.org/nsfw")
>>>
>>> response
<Response [200]>
>>>
>>> response.content
>>> response.text
>>>
>>> print(response.text)
>>>
>>> from bs4 import BeautifulSoup
>>>
>>> soup = BeautifulSoup(response.text, 'html.parser')
>>>
>>> soup
>>> soup.find_all('img')
>>> [img.attrs for img in soup.find_all('img')]
>>> [img.attrs['src'] for img in soup.find_all('img')]
>>> import os.path as path
>>>
>>> base_url = 'https://kennethreitz.org/nsfw'
>>>
>>> image_source = [img.attrs['src'] for img in soup.find_all('img')]
>>>
>>> full_image_sources = [path.join(base_url, src) for src in image_source]
>>>
>>> full_image_sources
>>>
>>> with open('images.txt', 'w') as f:
     f.write('\n'.join(full_image_sources))
```

## main.py file
```python
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
```