import logging

def log(name=__name__, log_file='app.log', level=logging.INFO):
    format = logging.Formatter('%(asctime)s - %(name)s - %(level)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(format)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger
