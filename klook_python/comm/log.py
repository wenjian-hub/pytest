import logging
# 设置日志级别，输出格式和过滤


class logConf:
    def logging(self):

        logging.basicConfig(level=logging.DEBUG, filename='sample.log', format="%(asctime)s:%(levelno)s->%(lineno)d::%(message)s")

        fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)

