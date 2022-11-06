# # -*- coding: utf-8 -*-
#
# # 用例  ID:
# # 用例标题:
# # 预置条件:
# # 测试步骤:
# #   1.调用接口：sigin,传入账号，密码，请求url，header发起post请求
# # 预期结果:
# #   1.登录成功，返回当前账户信息
# #   2.检查响应码为：200，各字段正确
# # 脚本作者: 林德浩
# # 写作日期: 2022/9/8 12:54 PM
#
#
# import pytest
#
#
# @pytest.fixture(scope='session', autouse=True)
# def session():
#     print('before session.........')
#     yield
#     print('after session..........')
#
#
# @pytest.fixture(scope='module', autouse=True)
# def module():
#     print('before module.........')
#     yield
#     print('after module..........')
#
#
# @pytest.fixture(scope='class', autouse=True)
# def classDemo():
#     print('before class..........')
#     yield
#     print('after class............')
#
#
# @pytest.fixture(scope='function', autouse=True)
# def fun():
#     print('before function.............')
#     yield
#     print('after function..............')
