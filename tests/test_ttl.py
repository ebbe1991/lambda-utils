import lambda_utils.ttl
from datetime import date, datetime


def test_compute_ttl_for_date_none():
    input_date = None
    result = lambda_utils.ttl.compute_ttl_for_date(input_date)
    assert result is None


def test_compute_ttl_for_date():
    input_date = date.fromisoformat("2023-01-27")
    result = lambda_utils.ttl.compute_ttl_for_date(input_date)
    assert result == 1683417600


def test_compute_ttl_for_datetime_none():
    input_datetime = None
    result = lambda_utils.ttl.compute_ttl_for_datetime(input_datetime)
    assert result is None


def test_compute_ttl_for_datetime():
    input_datetime = datetime.fromisoformat("2023-01-27T12:30:15")
    result = lambda_utils.ttl.compute_ttl_for_datetime(input_datetime)
    assert result == 1683462615
