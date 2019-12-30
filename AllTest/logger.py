import logging
import time
import os

class Logger():
    def __init__(self,logger):

        #创建一个logger
        self.logger = logging.getLogger(logger)

        #创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))

        log_dir = os.path.abspath('.') + '/logs/'
        log_name = log_dir + rq + '.log'
        fh = logging.FileHandler(log_name)

        fh.setLevel(logging.DEBUG)

        #创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #定义handler输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
