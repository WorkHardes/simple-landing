import logging
import logging.config

import yaml

from src.core.settings import settings

with open(settings.LOGGER_CONFIG_FILE_PATH) as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))

logger = logging.getLogger(__name__)
