import logging
import sys
import os

IS_DEBUG = False


def info(msg, *args, **kwargs):
    if IS_DEBUG:
        print(msg)
    else:
        logging.info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    if IS_DEBUG:
        print(msg)
    else:
        logging.debug(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    if IS_DEBUG:
        print(msg)
    else:
        logging.error(msg, *args, **kwargs)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def load_logging():
    logging.basicConfig(level=logging.INFO, filename="./Logs/logfile_{0}.txt".format(os.getpid()), filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    sys.excepthook = handle_exception


load_logging()
