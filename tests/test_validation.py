import lambda_utils.validation
import pytest
from lambda_utils.exception import ValueNotPresentException, ValidationException


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
