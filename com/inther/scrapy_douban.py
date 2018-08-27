from pyquery import PyQuery as py
import requests
from PIL import Image
from io import BytesIO
import re
import json
import os

user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             r'Chrome/66.0.3359.139 Safari/537.36'
_cookie_file_path = r'D:/douban_cookie.txt'
_douban_host = r'https://www.douban.com'
_douban_movie_host = r'https://movie.douban.com'
_douban_book_host = r'https://book.douban.com'
_headers = {'User-Agent': user_agent}


def _get_response_content(url):
    return requests.get(url, headers=_headers).content


def _detect_if_has_captcha(content):
    return py(content)('#captcha_image').attr('src')


def _get_login_captcha_info(content):
    pq = py(content)
    captcha_id = pq('input[name = "captcha-id"]').attr('value')
    captcha_img_url = pq('#captcha_image').attr('src')
    Image.open(BytesIO(requests.get(captcha_img_url).content)).show()
    captcha_solution = input('请输入验证码:\n')
    return captcha_id, captcha_solution


def _login_douban_with_captcha(seesion, login_mail, password, captcha_id, captcha_solution):
    parms = {'source': 'index_nav',
             'redir': _douban_host,
             'form_email': login_mail,
             'form_password': password,
             'captcha-solution': captcha_solution,
             'captcha-id': captcha_id,
             'remember': 'on',
             'login': u'登录'}
    seesion.post('https://accounts.douban.com/login', data=parms, headers=_headers)
    if seesion.cookies.get('dbcl2'):
        return True
    else:
        return False


def _login_douban_without_captcha(seesion, login_mail, password):
    parms = {'source': 'index_nav',
             'redir': _douban_host,
             'form_email': login_mail,
             'form_password': password,
             'remember': 'on',
             'login': u'登录'}
    seesion.post('https://accounts.douban.com/login', data=parms, headers=_headers)
    if seesion.cookies.get('dbcl2'):
        return True
    else:
        return False


def _login_douban_by_cookie(seesion, cookie):
    header = {'Cookie': cookie}
    header.update(_headers)
    seesion.get(_douban_host, headers=header)
    if seesion.cookies.get('dbcl2'):
        return True
    else:
        return False


def get_one_page_movie_list(url, **kwargs):
    movie_list = []
    session = kwargs.get('session')
    if session:
        pq = py(session.get(url).content)
    else:
        pq = py(_get_response_content(url))
    movie_dict = pq('.item')
    for movie in movie_dict.items():
        title_string = movie('.title em').text().strip() + movie('.title a').text().strip()
        movie_tittle = title_string.split('/')[0].strip() if title_string.count('/') else 'null'
        movie_another_title = list(map(str.strip, title_string.split('/')[1:])) if title_string.count('/') else []
        movie_url = movie('.title a').attr('href')
        movie_id = ''
        for txt in movie_url.split('/'):
            if re.match(r'^\d+$', txt):
                movie_id = ''.join(txt)
                break
        movie_coverimage_url = movie('.pic img').attr('src')
        movie_intro = movie('.intro').text()
        movie_tags = movie('.tags').text().split(':')[1].strip() if movie('.tags').text().count(':') else ''
        movie_comment = movie('.comment').text()
        movie_dict = {'id': movie_id, 'url': movie_url, 'title': movie_tittle, 'another_title': movie_another_title,
                      'cover_img_url': movie_coverimage_url, 'intro': movie_intro, 'tags': movie_tags,
                      'comment': movie_comment}
        movie_list.append(movie_dict)
    return movie_list


def get_one_page_book_list(url, **kwargs):
    book_list = []
    session = kwargs.get('session')
    if session:
        pq = py(session.get(url).content)
    else:
        pq = py(_get_response_content(url))
    book_dict = pq('.subject-item')
    for book in book_dict.items():
        book_tittle = book('.info h2').text().strip() + book('.info h2 span').text().strip()
        book_url = book('.info h2 a').attr('href')
        book_id = ''
        for txt in book_url.split('/'):
            if re.match(r'^\d+$', txt):
                book_id = ''.join(txt)
                break
        book_coverimage_url = book('.pic img').attr('src')
        book_intro = book('.pub').text()
        book_tags = book('.tags').text().split(':')[1].strip() if book('.tags').text().count(':') else ''
        book_comment = book('.comment').text()
        book_dict = {'id': book_id, 'url': book_url, 'title': book_tittle,
                     'cover_img_url': book_coverimage_url, 'intro': book_intro, 'tags': book_tags,
                     'comment': book_comment}
        book_list.append(book_dict)
    return book_list


class MyDouban:

    def __init__(self, mail, password):
        login_by_cookie = True
        if os.path.exists(_cookie_file_path) and os.path.isfile(_cookie_file_path):
            with open(_cookie_file_path, 'r') as f:
                cookie = json.loads(f.read()).get('Cookie')
                if cookie is not None:
                    self.session = requests.session()
                    if not _login_douban_by_cookie(self.session, cookie):
                        raise Exception('Cookie信息有误')
                else:
                    login_by_cookie = False
        else:
            login_by_cookie = False
        if not login_by_cookie:
            init_content = _get_response_content(_douban_host + '/login')
            if _detect_if_has_captcha(init_content):
                info = _get_login_captcha_info(init_content)
                self.session = requests.session()
                if not _login_douban_with_captcha(self.session, mail, password, info[0], info[1]):
                    raise Exception('登录信息输入错误')
            else:
                self.session = requests.session()
                if not _login_douban_without_captcha(self.session, mail, password):
                    raise Exception('登录信息输入错误')
        self.person_id = self.session.cookies.get('dbcl2').split('"')[1].split(':')[0]
        self.person_index = _douban_host + '/people/' + self.person_id
        self.movie_collect = _douban_host + '/people/' + self.person_id + r'/collect'
        self.movie_wish = _douban_host + '/people/' + self.person_id + r'/wish'
        self.book_collect = _douban_host + '/people/' + self.person_id + r'/collect'
        self.book_wish = _douban_host + '/people/' + self.person_id + r'/wish'
        self.book_page_list = []
        self.movie_page_list = []

    def save_cookie_to_local(self):
        with open(_cookie_file_path, 'w') as f:
            cookie = ''
            for key, value in self.session.cookies.items():
                cookie = cookie + key + '=' + value + ';'
            f.write(json.dumps({'Cookie': cookie[1: -1]}))

    def get_my_movie_page_list(self):
        p = py(self.movie_collect)
        page_dict = p('.paginator > a')
        for page in page_dict.items():
            url = page.attr('href')
            if url:
                self.movie_page_list.append(_douban_movie_host + url)
            else:
                continue

    def get_my_watched_movie(self):
        return get_one_page_movie_list(self.movie_collect, session=self.session)

    def get_my_watched_book(self):
        return get_one_page_book_list(self.book_collect, seesion=self.session)


if __name__ == "__main__":
    pass
