import logging

logging.basicConfig(filename="INFO.log", format='%(asctime)s %(filename)s:line:%(lineno)d [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S ',
                    level=logging.INFO)
logger = logging.getLogger()
KZT = logging.StreamHandler()
KZT.setLevel(logging.INFO)
logger.addHandler(KZT)

