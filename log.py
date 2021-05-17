import logging

logging.basicConfig(level=logging.INFO, filename="output.log", filemode="w", format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# # create file handler which logs even debug messages
# fh = logging.FileHandler('output.log', mode='w')
# fh.setLevel(logging.INFO)
#
# # create formatter and add it to the handlers
# formatter = logging.Formatter('[%(asctime)s] %(levelname)8s --- %(message)s ' +
#                               '(%(filename)s:%(lineno)s)', datefmt='%Y-%m-%d %H:%M:%S')
# fh.setFormatter(formatter)
#
# # add the handlers to the logger
#
# logger.addHandler(fh)
#
# logger.log(logging.INFO,     "INFO     Message - 20")