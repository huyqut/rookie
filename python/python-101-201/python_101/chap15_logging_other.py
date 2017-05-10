# Multi-modules logging

import logging


def do_something():
    # A logger should have its root module separated by '.' (multi-level is accepted)
    module_logger = logging.getLogger('roses.violet')
    module_logger.info('Sup yo motherfucker')
