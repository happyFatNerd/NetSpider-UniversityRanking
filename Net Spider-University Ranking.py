import bs4
from bs4 import BeautifulSoup
import requests

def readUrl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'unsolving problem:'+r.status_code

def readList(html):
    soup = BeautifulSoup(html,'html.parser')
    uList = []
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            u = [tds[0].string,tds[1].string,tds[2].string]
            uList.append(u)
    return uList

def printList(uList,num):
    print('{:^8}\t{:^80}\t{:^20}\t'.format('Ranking','University Name','Location'))
    for i in range(num):
        print('{:^8}\t{:^80}\t{:^20}\t'.format(uList[i][0],uList[i][1],uList[i][2]))

def main():
    url = 'https://cwur.org/2018-19.php'
    html = readUrl(url)
    uList = readList(html)
    flag = False
    while not flag:
        num = input('Please input the number of universities(<=1000)')
        if num.isdigit() and int(num)<=1000 and int(num)>0:
            printList(uList,int(num))
            flag = True
        else:
            print('invalid input')
            flag = False
    

main()
input()


