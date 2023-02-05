import json
from aws_lambda_powertools.event_handler import Response


def extract_body(response) -> str:
    body = response['body']
    if body and len(body) > 0:
        return json.loads(body)
    else:
        return None


def extract_headers(response) -> str:
    return response['headers']


def extract_header_value(response, key) -> str:
    headers = response['headers']
    if headers:
        return headers.get(key)
    else:
        return None


def extract_status_code(response) -> int:
    status_code = response['statusCode']
    if status_code:
        return int(status_code)
    else:
        return None


def extract_id(response) -> str:
    body = extract_body(response)
    if body:
        return body['id']
    else:
        return None


def empty_response(statusCode: int) -> Response:
    return Response(
        status_code=statusCode,
        content_type='application/json',
        body=None
    )


def response(statusCode: int, body: str = None, headers: dict = None) -> Response:
    return Response(
        status_code=statusCode,
        content_type='application/json',
        body=body,
        headers=headers
    )


def to_json_array(json_items: list[str]) -> str:
    jsonarray = "["
    json_items_length = len(json_items)
    for i in range(json_items_length):
        jsonarray = jsonarray + json_items[i]
        if i < json_items_length-1:
            jsonarray = jsonarray + ","

    return jsonarray + "]"
