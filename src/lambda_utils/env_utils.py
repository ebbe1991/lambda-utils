import os


def getenv_as_boolean(key: str, defaultvalue: bool) -> bool:
    value = os.getenv(key, str(defaultvalue))
    if value:
        return value.lower() in ('true', 't', '1')
    else:
        return defaultvalue
