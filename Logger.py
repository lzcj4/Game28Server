import logging
import sys
import os

IS_DEBUG = False


def info(msg, *args, **kwargs):
    if IS_DEBUG:
        print(msg)
    else:
        if args and kwargs:
            logging.info(msg, args, kwargs)
        elif args:
            logging.info(msg, args)
        elif kwargs:
            logging.info(msg, kwargs)
        else:
            logging.info(msg)


def debug(msg, *args, **kwargs):
    if IS_DEBUG:
        print(msg)
    else:
        if args and kwargs:
            logging.debug(msg, args, kwargs)
        elif args:
            logging.debug(msg, args)
        elif kwargs:
            logging.debug(msg, kwargs)
        else:
            logging.debug(msg)


def error(msg, *args, **kwargs):
    if IS_DEBUG:
        print(msg)
    else:
        if args and kwargs:
            logging.error(msg, args, kwargs)
        elif args:
            logging.error(msg, args)
        elif kwargs:
            logging.error(msg, kwargs)
        else:
            logging.error(msg)


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
