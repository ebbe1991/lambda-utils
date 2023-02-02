def parse_bool(bool_obj) -> bool:
    if isinstance(bool_obj, bool):
        return bool_obj if bool_obj else False

    return str(bool_obj).lower() in ('true', 't', '1')
