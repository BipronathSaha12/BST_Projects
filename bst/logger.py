# logging file for bst
import logging 

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    logging.basicConfig(level=level,
                        format='%(asctime)s %(name)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[
                            logging.FileHandler(log_file),
                            logging.StreamHandler()
                        ])
    