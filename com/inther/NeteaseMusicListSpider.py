from selenium import webdriver
from pyquery import PyQuery as pq
import re

class MusicListSpider():
    domain = 'https://music.163.com'
    user_home = domain + '/user/home?id='
    regex = re.compile(r'id=(\d+)')

    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options=self.option)

    def openurl(self, userid: str) -> str:
        self.browser.get(url=self.user_home + userid)
        self.browser.switch_to.frame('contentFrame')
        html = self.browser.find_element_by_css_selector('ul#cBox').get_attribute('innerHTML')
        self.browser.close()
        return html

    def parse(self, htmltext) -> list:
        doc = pq(htmltext)
        li = doc('li')
        musiclist = []
        for l in li.items():
            dic = {}
            title = l('div.u-cover a').attr('title')
            url = l('div.u-cover a').attr('href')
            listid = self.regex.search(url).group(1)
            dic.update({'title': title, 'url': self.domain + url, 'listid': listid})
            musiclist.append(dic)
        return musiclist


if __name__ == '__main__':
    m = MusicListSpider()
    ml = m.parse(m.openurl('7001543'))
    print(ml)
