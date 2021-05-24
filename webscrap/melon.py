from bs4 import BeautifulSoup
from urllib.request import urlopen
class Melon(object):

    url = ''
    headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57'}


    @staticmethod
    def main():
        melon = Melon()
        while 1:
            menu = int(input('0. Exit\n  1. Input URL 2.Title Ranking\n 3.Artist Ranking'))
            if menu == 0:
                break
            elif menu == 1:
                melon.url = input('Input URL')
            elif menu == 2:
                soup = BeautifulSoup(urlopen(melon.url), 'lxml')
                count = 0
                for i in soup.find_all("div", {"class":"ellipsis rank01"}):
                    count += 1
                    print(f'{str(count)} 위')
                    print(f' Title: {i.find("a").text}')
            elif menu == 3:
                soup = BeautifulSoup(urlopen(melon.url), 'lxml')
                count = 0
                for i in soup.find_all("div", {"class":"ellipsis rank02"}):
                    count += 1
                    print(f'{str(count)} 위')
                    print(f'Artist: {i.find("a").text}')
            else:
                print('다시 입력하세요')
                continue
                # https://www.melon.com/chart/index.htm

Melon.main()
