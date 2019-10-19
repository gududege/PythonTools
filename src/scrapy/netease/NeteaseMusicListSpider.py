from time import sleep

from selenium import webdriver
from pyquery import PyQuery as pq
import re
import json
from com.netease.RedisDB import *


class MusicListSpider:
    domain = 'https://music.163.com'
    user_home = domain + '/user/home?id='
    regex = re.compile(r'id=(\d+)')
    userid = ''

    def __init__(self, userid):
        self.userid = userid
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options=self.option)

    def openuserdomain(self) -> str:
        self.browser.get(url=self.user_home + self.userid)
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

    def putjsondatatoredis(self, datalist):
        jsondatalist = []
        for data in datalist:
            jsondatalist.append(json.dumps(data, ensure_ascii=False))
        redisconn = RedisConnection()
        [redisconn.putset('netease:' + self.userid + ':musiclist', i) for i in jsondatalist]
        redisconn.close()


if __name__ == '__main__':
    m = MusicListSpider('7001543')
    m.putjsondatatoredis(m.parse(m.openuserdomain()))
