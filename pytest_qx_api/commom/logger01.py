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
# 写作日期: 2022/9/4 2:17 AM

import logging
import os

class Log_Message:

    def log(message):
        # 设定日志名称
        logger = logging.getLogger('pytest_qx_logs')

        # 指定日志等级
        logger.setLevel(logging.DEBUG)

        # 设定日志 内容显示的格式
        log_message = f'[%(asctime)s] [%(filename)s] [line:%(lineno)d] [%(levelname)s] [%(message)s]'

        # 格式化日志
        formatter = logging.Formatter(log_message)

        # 设定日志显示在控制台输出
        sh = logging.StreamHandler()
        # 控制台暑输出日志格式化
        sh.setFormatter(formatter)
        # 设定 控制台输出日志的级别
        sh.setLevel(logging.DEBUG)
        # 把日志流放入处理器
        # logger.addHandler(sh)
        logger.addHandler(sh)

        # 设定日志输出的目录位置
        logs = os.path.join(os.path.dirname(__file__), '../logs')
        # 判断目录是否存在，不存在就新建
        if not os.path.exists(logs):
            os.mkdir(logs)
        # 设定日志内容输出到指定的文件
        logfile = os.path.join(logs, 'qx.log')

        # 设定日志输出到文件流的方法
        fh = logging.FileHandler(logfile, mode='a', encoding='utf-8')
        # 设定日志格式化
        fh.setFormatter(formatter)
        # 设定日志输出到文件的 日志等级
        fh.setLevel(logging.DEBUG)

        # 添加日志文件流到处理器
        logger.addHandler(fh)

        return logger.info(message)


if __name__ == '__main__':
    Log_Message.log('pytest_logs')
