import requests
from bs4 import BeautifulSoup
import threading, queue

start_page = "http://www.163.com"
url_queue = queue.Queue()
url_queue.put(start_page)
domain = "163.com"
urls = []
html = requests.get(start_page)
soup = BeautifulSoup(html.content, "html.parser")
for e in soup.findAll('a'):
    url = e.attrs.get('href', '#')
    urls.append(url)
    for next_url in urls:
        if domain in next_url:
            url_queue.put(next_url)


def get_info():
    while True:
        if not url_queue.empty():
            current_url = url_queue.get()
            print(current_url)
        else:
            break

ts = []
for i in range(10):
    t = threading.Thread(target=get_info)
    ts.append(t)
    t.start()

for i in ts:
    t.join()
