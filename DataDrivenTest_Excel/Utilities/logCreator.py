import logging
import Utilities.logCreator as logCreator

def log_generatoor():
    logging.basicConfig(
        filename="Reports/Logs/testlogreport.log",
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p', force=True
    )
    return logging.getLogger()
