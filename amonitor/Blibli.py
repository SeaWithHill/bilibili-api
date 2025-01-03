import subprocess
import logging

from loguru import logger
if __name__ == '__main__':
    # 将日志输出到文件，rotation 表示文件大小达到 1MB 时自动旋转，compression 表示对旧文件进行压缩
    logger.add("../log/test.log", rotation="1 MB", compression="zip")
    logger.debug("这是一条调试信息")
    logger.info("这是一条信息")
    logger.warning("这是一条警告")
    logger.error("这是一条错误")
    logger.critical("这是一条严重错误")
