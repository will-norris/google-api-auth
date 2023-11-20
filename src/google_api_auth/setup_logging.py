import logging
import logging.handlers # https://stackoverflow.com/questions/64951836/python-logging-attributeerror-module-logging-has-no-attribute-handlers

fmt = logging.Formatter('%(name)s -> %(asctime)s || %(message)s')

def setup_logger(logger_name):
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    file_handler = logging.handlers.TimedRotatingFileHandler(f'{logger_name}.log', when='midnight', backupCount=3)
    file_handler.setFormatter(fmt)

    logger = logging.getLogger(f'{logger_name}')
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger