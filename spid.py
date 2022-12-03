import re
import sys
import urllib.parse
import urllib.request
import xlwt
import io
from bs4 import BeautifulSoup
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    url = "https://fanyi.baidu.com/#en/zh/"
    s = input()
    url += s
    askURL(url)


def getDate():
    1


def askURL(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
    }
    req = urllib.request.Request(url, headers=head)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    # html=res.read()

    out = open('fanyi.html', 'w', encoding='utf-8')
    out.write(html)
    out.close()


def saveDate():
    1


if __name__ == "__main__":
    main()
