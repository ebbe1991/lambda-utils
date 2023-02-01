def is_email_send_ok(response: dict) -> bool:
    metadata = response.get('ResponseMetadata')
    if metadata:
        return metadata.get('HTTPStatusCode') == 200
    else:
        return False
