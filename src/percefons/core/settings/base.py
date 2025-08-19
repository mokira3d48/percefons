import os
import logging
import logging.config

LOGGING_CONFIG = "logging.conf"

if os.path.isfile(LOGGING_CONFIG):
    logging.config.fileConfig(LOGGING_CONFIG)
