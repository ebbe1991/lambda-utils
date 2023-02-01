import json
import lambda_utils.response_utils


def test_extract_body_ok():
    body = lambda_utils.response_utils.extract_body({
        "body": json.dumps({"foo": "bar"})
    })
    assert body == {"foo": "bar"}


def test_extract_body_none_ok():
    body = lambda_utils.response_utils.extract_body({
        "body": None
    })
    assert body is None


def test_extract_headers_ok():
    headers = lambda_utils.response_utils.extract_headers({
        "headers": {"x-foo": "bar"}
    })
    assert headers == {"x-foo": "bar"}


def test_extract_headers_none_ok():
    headers = lambda_utils.response_utils.extract_headers({
        "headers": None
    })
    assert headers is None


def test_extract_header_value_ok():
    value = lambda_utils.response_utils.extract_header_value({
        "headers": {"x-foo": "bar"}
    }, "x-foo")
    assert value == "bar"


def test_extract_header_value_none_ok():
    value = lambda_utils.response_utils.extract_header_value({
        "headers": {"x-foo": "bar"}
    }, "x-bar")
    assert value is None


def test_extract_header_value_headers_none_ok():
    value = lambda_utils.response_utils.extract_header_value({
        "headers": None
    }, "x-foo")
    assert value is None


def test_extract_status_code_ok():
    status_code = lambda_utils.response_utils.extract_status_code({
        "statusCode": "200"
    })
    assert status_code == 200


def test_extract_status_code_none_ok():
    status_code = lambda_utils.response_utils.extract_status_code({
        "statusCode": None
    })
    assert status_code is None


def test_extract_id_ok():
    id = lambda_utils.response_utils.extract_id({
        "body": json.dumps({"id": "abc"})
    })
    assert id == "abc"


def test_extract_id_none_ok():
    id = lambda_utils.response_utils.extract_id({
        "body": json.dumps({"id": None})
    })
    assert id is None


def test_extract_id_body_none_ok():
    id = lambda_utils.response_utils.extract_id({
        "body": None
    })
    assert id is None
