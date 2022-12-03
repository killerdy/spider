import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite


def main():
    url = "https://movie.douban.com/top250?start="
    # url="https://www.douban.com"
    savepath = "豆瓣电影Top250.xls"
    dbpath = "test.db"
    datalist = getData(url)
    # print(datalist)
    # saveDate(datalist, savepath)
    sqlite.saveDataDB(datalist, dbpath)


findLink = re.compile('<a href="(.*)">')
findName = re.compile('<span class="title">(.*)</span>')
findPic = re.compile('src="(.*)" ')
findRate = re.compile(
    '<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile('<span>(.*)</span>')


def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        url = baseurl+str(i*25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            # print(item)
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            rate = re.findall(findRate, item)[0]
            name = re.findall(findName, item)
            pic = re.findall(findPic, item)[0]
            # judgename=re.findall(findJudge,item)[0]
            if (len(name) == 2):
                data.append(name[0])
                data.append(name[1].replace('/', ''))
            else:
                data.append(name[0])
                data.append(' ')
            data.append(pic)
            data.append(rate)

            datalist.append(data)
    return datalist


def askURL(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
    }
    req = urllib.request.Request(url, headers=head)
    res = urllib.request.urlopen(req)
    html = (res.read().decode('utf-8'))
    return html


def saveDate(datalist, path):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('sheet1')
    col = ('电影名字', '外国名字' '链接', '图片', '评分')
    for i in range(0, len(col)):
        worksheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, len(col)):
            worksheet.write(i+1, j, data[j])
    workbook.save(path)


if __name__ == "__main__":
    main()
    print("爬取完毕")
