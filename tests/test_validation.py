import lambda_utils.validation
import pytest
from lambda_utils.exception import ValueNotPresentException, ValidationException
from datetime import date


def test_check_required_field_ok():
    bananas = 'bananas'
    lambda_utils.validation.check_required_field(bananas, 'bananas')


def test_check_required_field_none_exception():
    bananas = None
    with pytest.raises(ValueNotPresentException) as exc_info:
        lambda_utils.validation.check_required_field(bananas, 'bananas')
    exception_raised = exc_info.value
    assert exception_raised.error_text == "'bananas' not present."


def test_check_required_field_empty_exception():
    bananas = ''
    with pytest.raises(ValueNotPresentException) as exc_info:
        lambda_utils.validation.check_required_field(bananas, 'bananas')
    exception_raised = exc_info.value
    assert exception_raised.error_text == "'bananas' not present."


def test_check_required_field_just_spaces_exception():
    bananas = ' '
    with pytest.raises(ValueNotPresentException) as exc_info:
        lambda_utils.validation.check_required_field(bananas, 'bananas')
    exception_raised = exc_info.value
    assert exception_raised.error_text == "'bananas' not present."


def test_check_required_field_float_ok():
    my_number = 5
    lambda_utils.validation.check_required_field(my_number, 'my number')


def test_check_email_ok():
    email = 'example@example.com'
    lambda_utils.validation.check_email(email)


def test_check_email_with_subdomain_ok():
    email = 'example@sub.example.com'
    lambda_utils.validation.check_email(email)


def test_check_email_local_part_missing_exception():
    email = '@example.com'
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.validation.check_email(email)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "invalid email address '@example.com'."


def test_check_email_domain_missing_exception():
    email = 'example@'
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.validation.check_email(email)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "invalid email address 'example@'."


def test_check_email_third_level_domain_missing_exception():
    email = 'example@example'
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.validation.check_email(email)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "invalid email address 'example@example'."


def test_check_email_at_missing_exception():
    email = 'exampleexample.com'
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.validation.check_email(email)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "invalid email address 'exampleexample.com'."


def test_check_daterange_ok():
    von = date(2022, 1, 1)
    bis = date(2023, 12, 31)
    lambda_utils.validation.check_daterange(von, bis)


def test_check_daterange_von_none_ok():
    von = None
    bis = date(2023, 12, 31)
    lambda_utils.validation.check_daterange(von, bis)


def test_check_daterange_bis_none_ok():
    von = date(2023, 1, 1)
    bis = None
    lambda_utils.validation.check_daterange(von, bis)


def test_check_daterange_all_none_ok():
    von = None
    bis = None
    lambda_utils.validation.check_daterange(von, bis)


def test_check_daterange_von_bis_equal_ok():
    von = date(2022,1,1)
    bis = date(2022,1,1)
    lambda_utils.validation.check_daterange(von, bis)


def test_check_daterange_von_after_bis_equal_exception():
    von = date(2022,1,1)
    bis = date(2021,1,1)
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.validation.check_daterange(von, bis)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "start '2022-01-01' is after '2021-01-01'."
