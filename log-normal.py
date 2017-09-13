
# import logging
import logging.config

logging.config.fileConfig('logging.conf')


# get 'our special' logger
logger = logging.getLogger('nplogF')

logger.debug('file debug message')
logger.info('file info message')
logger.warning('file warn message')
logger.error('file error message')
logger.critical('file critical message')


# This goes to 'root' logger

logging.debug('console debug message')
logging.info('console info message')
logging.warning('console warn message')
logging.error('console error message')
logging.critical('console critical message')


# This goes to 'root' logger, too!

l = logging.getLogger('root')
l.debug('THIS IS CONSOLE, AS ABOVE')
