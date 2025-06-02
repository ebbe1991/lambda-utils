from lambda_utils.exception import ValidationException, ValueNotPresentException
from datetime import date
import re

regex = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def check_required_field(field, fieldname: str):
    missing = False
    if field is None:
        missing = True
        raise ValueNotPresentException(fieldname)

    if isinstance(field, str) and len(field.strip()) <= 0:
        missing = True

    if missing:
        raise ValueNotPresentException(fieldname)


def check_email(email):
    if re.fullmatch(regex, email):
        pass
    else:
        raise ValidationException(f"invalid email address '{email}'.")


def check_daterange(von: date, bis: date):
    if von and bis and von > bis:
        raise ValidationException(f"start '{von}' is after '{bis}'.")


def check_list_not_empty(items: list, fieldname: str):
    if items is None or len(list(filter(lambda i: i is not None, items))) < 1:
        raise ValidationException(f"list '{fieldname}' is empty.")
