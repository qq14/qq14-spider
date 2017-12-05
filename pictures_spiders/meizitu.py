import requests
import os
from bs4 import BeautifulSoup
url = 'http://www.meizitu.com/a/5582.html'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')
imgs = soup.select('#picture > p > img')
mm_imgs = []

if not os.path.exists('uploads'):
    os.mkdir('uploads')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
for img in imgs:
    src = img.get('src')
    filename = (src[-18:]).replace('/','-')
    target = "uploads/{}".format(filename)
    r = requests.get(src, headers=headers)
    with open(target, "wb") as fs:
        fs.write(r.content)

    print("%s => %s" % (src, target))