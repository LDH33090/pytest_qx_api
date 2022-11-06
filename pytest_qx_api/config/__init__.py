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
# 写作日期: 2022/9/3 4:25 PM
import os
import yaml

# 获取 token请求参数yaml文件的路径
file_path = os.path.join(os.path.dirname(__file__), 'token_requestdata.yaml')

with open(file_path) as m:
    message = yaml.safe_load(m)
