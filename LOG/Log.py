import logging
# 默认值是warning以上的日志不输出，所以info和debug不输出。其他的输出
logging.debug("这个不输出")
logging.info("这个输出吗")
logging.warning("这个输出")
logging.error("这个输出")
logging.critical("这个必输出")