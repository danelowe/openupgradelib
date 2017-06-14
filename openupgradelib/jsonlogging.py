import logging
import sys
from pythonjsonlogger import jsonlogger

class StackDriverJsonFormatter(jsonlogger.JsonFormatter, object):
    def __init__(self, fmt="%(levelname) %(message)", style='%', *args, **kwargs):
        jsonlogger.JsonFormatter.__init__(self, fmt=fmt, *args, **kwargs)
    def process_log_record(self, log_record):
        log_record['severity'] = log_record['levelname']
        del log_record['levelname']
        return super(StackDriverJsonFormatter, self).process_log_record(log_record)

handler = logging.StreamHandler(sys.stdout)
formatter = StackDriverJsonFormatter()
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.handlers = []
root_logger.addHandler(handler)
