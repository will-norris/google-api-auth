import logging

fmt = logging.Formatter('%(name)s -> %(asctime)s || %(message)s')

def setup_logger(logger_name):
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    file_handler = logging.FileHandler(f'{logger_name}.log', mode='w')
    file_handler.setFormatter(fmt)

    logger = logging.getLogger(f'{logger_name}')
    logger.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger