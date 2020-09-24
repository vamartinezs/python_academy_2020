import logging
from logging.handlers import RotatingFileHandler

LOG_FILENAME = "logs/generatorlogs.log"


class Singleton:
    __instance = None
    _generator_calls = 0
    _id_repetitions = 0

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def get_number_calls(self):
        return self._generator_calls

    def get_repetition_id(self):
        return self._id_repetitions

    def increment_generator_call_count(self):
        self._generator_calls += 1
        return self._generator_calls

    def incremeent_repeated_id_count(self):
        self._id_repetitions += 1
        return self._id_repetitions

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            pass
        else:
            Singleton.__instance = self


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.generatorcalls = Singleton().getInstance().get_number_calls()
        record.idrepetition = Singleton.getInstance().get_repetition_id()
        return True


class GeneratorLogger(Singleton):
    """
    Logger Manager
    """

    def __init__(self, loggername):
        self.logger = logging.getLogger(loggername)

        try:
            rhandler = RotatingFileHandler(
                LOG_FILENAME,
                mode='a',
                maxBytes=10 * 1024 * 1024,
                backupCount=5
            )
        except:
            raise IOError(f"Couldn't open file{LOG_FILENAME}")

        self.logger.setLevel(logging.DEBUG)
        self.logger.addFilter(ContextFilter())

        formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)-8s] [%(message)s] [Instances Counter:%('
                'generatorcalls)s] [Repeated Id Counter : %(idrepetition)s] ',
            datefmt='%F %H:%M:%S'
        )
        rhandler.setFormatter(formatter)
        self.logger.addHandler(rhandler)

    def debug(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.debug(msg)

    def error(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.error(msg)

    def info(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.info(msg)

    def warning(self, loggername, msg):
        self.logger = logging.getLogger(loggername)
        self.logger.warning(msg)


class GeneratorLogs(object):
    """
    Logger object.
    """

    def __init__(self, loggername="root"):
        self.lm = GeneratorLogger(loggername)  # LoggerManager instance
        self.loggername = loggername  # logger name

    def debug(self, msg):
        self.lm.debug(self.loggername, msg)

    def error(self, msg):
        self.lm.error(self.loggername, msg)

    def info(self, msg):
        self.lm.info(self.loggername, msg)

    def info_calls(self, msg):
        Singleton.getInstance().increment_generator_call_count()
        self.lm.info(self.loggername, msg)

    def info_ids(self, msg):
        Singleton.getInstance().incremeent_repeated_id_count()
        self.lm.info(self.loggername, msg)

    def warning(self, msg):
        self.lm.warning(self.loggername, msg)