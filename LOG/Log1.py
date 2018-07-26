'''
1.需求
    1，要求将所有级别的所有日志都写如到磁盘文件当中
    2，all.log文件中记录所有的日志信息，日志格式：日期和时间 - 日志级别 - 日志信息
    3，error.log 文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名【：行号】- 日志信息
    4，要求 all.log在每天凌晨进行日志切割


'''

import logging
import logging.handlers
import datetime


logger=logging.gerLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler=logging.handlers.TimedRotatingFileHandler('all.log',when='midnight',interval=1,backupCount=7)

rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))





