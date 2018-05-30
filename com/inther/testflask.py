from flask import Flask, redirect, url_for
from redis import StrictRedis
from com.inther.properties import *
import json

app = Flask(__name__)
redis = StrictRedis(host=nas_redis_ip, port=nas_redis_port)


@app.route('/')
def index():
    return redirect(url_for('get'))


@app.route('/get')
def get():
    return get_info_from_redis()


def get_info_from_redis():
    dic = {}
    name = redis.randomkey()
    data = redis.hgetall(name)
    for key, value in data.items():
        dic.update({key.decode('utf8'): value.decode('utf8')})
    return json.dumps(dic, ensure_ascii=False)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
