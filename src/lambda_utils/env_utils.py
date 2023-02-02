import os
from lambda_utils import bool_utils


def getenv_as_boolean(key: str, defaultvalue: bool) -> bool:
    value = os.getenv(key, str(defaultvalue))
    if value:
        return bool_utils.parse_bool(value)
    else:
        return defaultvalue
