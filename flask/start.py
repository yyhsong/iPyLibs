#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask

Flask is a lightweight WSGI web application framework.
It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular
Python web application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or project layout.
It is up to the developer to choose the tools and libraries they want to use.
There are many extensions provided by the community that make adding new functionality easy.
"""

from flask import Flask, request
from flask_cors import CORS

# 初始化Flask应用
app = Flask(__name__)

# 允许跨域访问
CORS(app)


# 通过装饰器对路由和函数进行映射
@app.route('/', methods=['GET'])
def home():
    user = request.args.get('user') or 'world'  # 获取请求参数
    return '<h1>Hello, {0}</h1>'.format(user)


if __name__ == '__main__':
    # 启动应用
    app.run(
        host='localhost',
        port='8080',
        debug=True
    )
