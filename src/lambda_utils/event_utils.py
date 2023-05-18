import json
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEventV2
from lambda_utils.exception import ValidationException
from datetime import date
from lambda_utils.date_utils import fromisoformat


def extract_stichtag(event: APIGatewayProxyEventV2) -> date:
    value = event.get_query_string_value('stichtag')
    return fromisoformat(value) if value else None


def extract_count(event: APIGatewayProxyEventV2) -> date:
    value = event.get_query_string_value('count')
    try:
        return int(value) if value else None
    except ValueError as ex:
        raise ValidationException(ex.args[0]) if value else None


def extract_body(event: APIGatewayProxyEventV2) -> str:
    body = event.decoded_body
    json_body = None
    if body:
        json_body = json.loads(body)
    if json_body and len(json_body) > 0:
        return json_body
    else:
        raise ValidationException("body not present.")


def extract_tenant(event: APIGatewayProxyEventV2) -> str:
    tenant_id = event.get_header_value('x-tenant-id')
    if tenant_id and len(tenant_id) > 0:
        return tenant_id
    else:
        raise ValidationException('tenant not present.')
