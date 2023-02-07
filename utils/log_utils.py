# -*- coding: utf-8 -*-

import logging
import sys

formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)07s - %(message)-110s",
    datefmt='%Y-%m-%dT%H:%M:%S')

handler_stdout = logging.StreamHandler(sys.stdout)
handler_stdout.setFormatter(formatter)


def add_logger(arg_name, arg_level):
    this_logger = logging.getLogger(arg_name)
    this_logger.setLevel(get_debug_level(arg_level))
    for handler in [handler_stdout]:
        this_logger.addHandler(handler)


def get_debug_level(arg_level):
    if arg_level == 1:
        return logging.WARNING
    elif arg_level == 2:
        return logging.INFO
    elif arg_level > 2:
        return logging.DEBUG
    else:
        return logging.ERROR


def add_loggers(dm, dp, de, ds):
    add_logger('model', dm)
    add_logger('plugin', dp)
    add_logger('event', de)
    add_logger('simulation', ds)
