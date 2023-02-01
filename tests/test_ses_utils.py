import lambda_utils.ses_utils


def test_email_send_response_status_200_ok():
    ses_response = {
        "ResponseMetadata": {
            "HTTPStatusCode": 200
        }
    }
    result = lambda_utils.ses_utils.is_email_send_ok(ses_response)
    assert result is True


def test_email_send_response_status_400_not_ok():
    ses_response = {
        "ResponseMetadata": {
            "HTTPStatusCode": 400
        }
    }
    result = lambda_utils.ses_utils.is_email_send_ok(ses_response)
    assert result is False


def test_email_send_response_status_none_not_ok():
    ses_response = {
        "ResponseMetadata": None
    }
    result = lambda_utils.ses_utils.is_email_send_ok(ses_response)
    assert result is False


def test_email_send_response_metadata_none_not_ok():
    ses_response = {
    }
    result = lambda_utils.ses_utils.is_email_send_ok(ses_response)
    assert result is False
