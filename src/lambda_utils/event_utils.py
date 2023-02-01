import json
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEventV2
from lambda_utils.exception import ValidationException


def extract_id(event: APIGatewayProxyEventV2) -> str:
    path_parameters = event.path_parameters
    id = None
    if path_parameters:
        id = path_parameters.get('id')
    if id and len(id) > 0:
        return id
    else:
        raise ValidationException("id not present.")


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
