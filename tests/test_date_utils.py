import lambda_utils.date_utils
from datetime import date, datetime
import pytest
from lambda_utils.exception import ValidationException

def test_compute_ttl_for_date_none():
    input_date = None
    result = lambda_utils.date_utils.compute_ttl_for_date(input_date)
    assert result is None


def test_compute_ttl_for_date():
    input_date = date.fromisoformat("2023-01-27")
    result = lambda_utils.date_utils.compute_ttl_for_date(input_date)
    assert result == 1683417600


def test_compute_ttl_for_datetime_none():
    input_datetime = None
    result = lambda_utils.date_utils.compute_ttl_for_datetime(input_datetime)
    assert result is None


def test_compute_ttl_for_datetime():
    input_datetime = datetime.fromisoformat("2023-01-27T12:30:15")
    result = lambda_utils.date_utils.compute_ttl_for_datetime(input_datetime)
    assert result == 1683462615


def test_fromisoformat_ok():
    input_datestring = "2022-01-01"
    result = lambda_utils.date_utils.fromisoformat(input_datestring)
    assert result == date(2022, 1, 1)


def test_fromisoformat_invalid_format():
    input_datestring = "2022-01.01"
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.date_utils.fromisoformat(input_datestring)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "Invalid isoformat string: '2022-01.01'"
