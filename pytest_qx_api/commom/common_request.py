# -*- coding: utf-8 -*-

# 用例  ID:
# 用例标题:
# 预置条件:
# 测试步骤:
#   1.封装请求方法
# 预期结果:
#   不同请求方式的请求方法，显示不同的日志内容格式
# 脚本作者: 林德浩
# 写作日期: 2022/9/3 10:06 PM
import unittest
import requests
# from commom.logger01 import log
# from commom.logger import logger
from commom.logger import logger


class CommonRequestMethod(unittest.TestCase):
    @classmethod
    def request(self, method: str, url, params=None, data=None, json=None, **kwargs):
        method_list = ['GET', 'POST', 'PUT', 'DELETE']
        method = method.upper()
        if method == 'GET':
            res = requests.get(url, params=params, **kwargs)
            if params:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{params},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{params},响应结果:{res.text}')
            elif json:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
            elif not params and not json:
                # log(f"请求方式:{method} ,请求url:{url},请求参数:{res.url.split('?')[-1]},响应结果:{res.text}")
                logger.info(f"请求方式:{method} ,请求url:{url},请求参数:{res.url.split('?')[-1]},响应结果:{res.text}")
            return res
        elif method == 'POST':
            res = requests.post(url, data=data, json=json, **kwargs)
            if data:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{data},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{data},响应结果:{res.text}')
            elif json:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
            return res
        elif method == 'PUT':
            res = requests.put(url, data=data, **kwargs)
            if data:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{data},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{data},响应结果:{res.text}')
            elif json:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
            return res
        elif method == 'DELETE':
            res = requests.delete(url, **kwargs)
            if data:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{data},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{data},响应结果:{res.text}')
            elif json:
                # log(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
                logger.info(f'请求方式:{method} ,请求url:{url},请求参数:{json},响应结果:{res.text}')
            return res
        else:
            try:
                if method not in method_list:
                    # log(f'请求方式:{method_list[method]} ,请求url:{url},请求参数:{data}')
                    logger.info(f'请求方式:{method_list[method]} ,请求url:{url},请求参数:{data}')
            except Exception as e:
                # log(e)
                logger.info(e)
