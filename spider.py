from urllib import request
from bs4 import  BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse

def get():
    response = request.urlopen('http://view.sdu.edu.cn')

    html = response.read()
    soup = BeautifulSoup(html)
    trs = soup.find_all("a")
    lens = len(trs)
    for i in range(lens):
        print(trs[i].get('href'))


    html = html.decode('utf8')
#
#     print(html)



class Robot:
    def __init__(self, start,range, save_path):
        self.url = start
        self.save_path = save_path
        self.range = range
        self.web_list = []
        self.web_viewed = []
        self.count = 0

    def run(self):
        self.fetch()
        while len(self.web_list):
            if self.count == 10:
                break
            self.url = self.web_list.pop()
            self.fetch()

    def fetch(self):
        if self.url not in self.web_viewed:
            response = request.urlopen(self.url)
            self.web_viewed.append(self.url)
            if response.getcode() == 200:
                self.count += 1
                print(self.count)
                html = response.read()

                text = html.decode('utf8')

                self.savehtml(text)
                soup = BeautifulSoup(html)

                for link in soup.find_all("a"):
                    url = urljoin(self.url,link.get('href'))
                    url_pa = urlparse(url)
                    if url_pa.netloc == self.range:
                        self.web_list.append(url)


    def savehtml(self,html):
        filename = self.save_path+str(self.count)
        with open(filename+'.html','w', encoding='utf8',) as f:
            f.write(html)










if __name__ == '__main__':
    arobot = Robot('http://view.sdu.edu.cn',"view.sdu.edu.cn",'data/')
    arobot.run()