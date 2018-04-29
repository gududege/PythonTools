from pyquery import PyQuery as py
import requests
from PIL import Image

captcha_file_path = r'D:/captcha.jpg'


def get_response_content(url):
    return requests.get(url).content


def detect_if_has_captcha(content):
    return py(content)('#captcha_image').attr('src')


def get_login_captcha_info(content):
    pq = py(content)
    captcha_id = pq('input[name = "captcha-id"]').attr('value')
    captcha_img_url = pq('#captcha_image').attr('src')
    with open(captcha_file_path, 'wb') as image:
        image.write(requests.get(captcha_img_url).content)
    Image.open(captcha_file_path).show()
    captcha_solution = input('请输入验证码:\n')
    return captcha_id, captcha_solution


def login_douban_with_captcha(login_mail, password, captcha_id, captcha_solution):
    parms = {'source': 'index_nav',
             'redir': r'http://www.douban.com/',
             'form_email': login_mail,
             'form_password': password,
             'captcha-solution': captcha_solution,
             'captcha-id': captcha_id,
             'remember': 'on',
             'login': u'登录'}
    douban = requests.post('https://accounts.douban.com/login', data = parms)
    with open(r"D:/douban.html", 'wb') as df:
        df.write(douban.content)


def login_douban_without_captcha(login_mail, password):
    parms = {'source': 'index_nav',
             'redir': r'http://www.douban.com/',
             'form_email': login_mail,
             'form_password': password,
             'remember': 'on',
             'login': u'登录'}
    douban = requests.post('https://accounts.douban.com/login', data = parms)
    with open(r"D:/douban.html", 'wb') as df:
        df.write(douban.content)


def main():
    init_contemt = get_response_content(r'https://accounts.douban.com/login')
    if detect_if_has_captcha(init_contemt):
        info = get_login_captcha_info(init_contemt)
        login_douban_with_captcha(mail, pwd, info[0], info[1])
    else:
        login_douban_without_captcha(mail, pwd)


if __name__ == "__main__":
    mail = input('请输入登录邮箱：\n')
    pwd = input('请输入登录密码：\n')
    main()
