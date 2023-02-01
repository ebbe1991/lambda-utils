from lambda_utils.exception import ValidationException, ValueNotPresentException
import re

regex = re.compile(
    r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


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
