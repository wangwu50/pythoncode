import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("this is debug log")
    logging.info("this is info log")
    logging.error("this is error log")