# -*- coding: utf-8 -*-

# 用例  ID:
# 用例标题:
# 预置条件:
# 测试步骤:
#   1.调用接口：sigin,传入账号，密码，请求url，header发起post请求
# 预期结果:
#   1.登录成功，返回当前账户信息
#   2.检查响应码为：200，各字段正确
# 脚本作者: 林德浩
# 写作日期: 2021/6/3 10:05 PM
import json

import requests

import config
from commom.common_request import CommonRequestMethod
import sys, os

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])


def test_getToken():
    url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
    body = {
        "phone": config.message['正确且有权限登录后台的手机号码']['phone'],
        "code": config.message['正确且有权限登录后台的手机号码']['code']
    }
    res = CommonRequestMethod.request(method='GET', url=url, params=body)
    # print(res.text)
    # print(res.json()['data']['token'])
    # print(res.text)
    return res.json()['data']['token']


def test_Session_getToken():
    url = "https://qx-mall-test.belle.net.cn/v2/admin/mp/login"
    body = {
        "phone": config.message['正确且有权限登录后台的手机号码']['phone'],
        "code": config.message['正确且有权限登录后台的手机号码']['code']
    }

    headers = {
        'Content - Type': 'application / json;charset=UTF-8'
    }

    # res = CommonRequestMethod.request(method='GET', url=url, params=body)
    res = requests.Session
    session_result = res.post(url=url, data=body,headers=headers)
    print(session_result.text)
    # print(res.text)
    # print(res.json()['data']['token'])
    # print(res.text)
    return res.json()['data']['token']


if __name__ == '__main__':
    # test_getToken()
    test_Session_getToken()
