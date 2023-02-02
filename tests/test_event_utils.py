import json
import pytest
import lambda_utils.event_utils
from datetime import date
from lambda_utils.exception import ValidationException
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEventV2


def test_extract_body_ok():
    event = create_test_event(body=json.dumps({"foo": "bar"}))
    body = lambda_utils.event_utils.extract_body(event)
    assert body == {"foo": "bar"}


def test_extract_body_none_not_ok():
    event = create_test_event(body=None)
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.event_utils.extract_body(event)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "body not present."


def test_extract_tenant_ok():
    event = create_test_event(headers={"x-tenant-id": "mytenant.com"})
    tenant = lambda_utils.event_utils.extract_tenant(event)
    assert tenant == "mytenant.com"


def test_extract_tenant_empty_not_ok():
    event = create_test_event(headers={"tenant-id": ""})
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.event_utils.extract_tenant(event)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "tenant not present."


def test_extract_tenant_none_not_ok():
    event = create_test_event(headers={})
    with pytest.raises(ValidationException) as exc_info:
        lambda_utils.event_utils.extract_tenant(event)
    exception_raised = exc_info.value
    assert exception_raised.error_text == "tenant not present."


def test_extract_stichtag_ok():
    event = create_test_event(queryParameters={"stichtag": "2022-01-01"})
    stichtag = lambda_utils.event_utils.extract_stichtag(event)
    assert stichtag == date(2022, 1, 1)


def test_extract_stichtag_none_ok():
    event = create_test_event(queryParameters={})
    stichtag = lambda_utils.event_utils.extract_stichtag(event)
    assert stichtag is None


def create_test_event(path: str = "/example", body: str = None, queryParameters: dict = None, headers: dict = None) -> APIGatewayProxyEventV2:
    return APIGatewayProxyEventV2({
        'version': '2.0',
        'routeKey': f'GET {path}',
        'rawPath': path,
        'rawQueryString': '',
        'cookies': [],
        'requestContext': {
            'accountId': '123',
            'apiId': 'test',
            'domainName': 'test.execute-api.eu-central-1.amazonaws.com',
            'domainPrefix': 'test',
            'http': {
                'method': "GET",
                'path': path,
                'protocol': 'HTTP/1.1',
                'sourceIp': '127.0.0.1'
            },
            'stage': '$default',
            'requestId': '123',
            'routeKey': f'GET {path}',
            'timeEpoch': 1673596800000
        },
        "queryStringParameters": queryParameters,
        'pathParameters': None,
        "headers": headers,
        "body": body,
        'isBase64Encoded': False
    })
