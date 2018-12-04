import logging.config
import os

class Config(object):
    LOGGING_CONFIG_FILE = 'logging_config.ini'    
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False

    @classmethod
    def init_app(cls, app):
        logging_config_path = os.path.normpath(
            os.path.join(
                os.path.dirname(__file__), cls.LOGGING_CONFIG_FILE))
        logging.config.fileConfig(logging_config_path)

class DevelopmentConfig(Config):
    DEBUG = True
    LOGGING_CONFIG_FILE = 'logging_config.ini'    
    SERVER_NAME = 'localhost:8888'

config_map = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

