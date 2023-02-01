import os
import lambda_utils.env_utils


def test_getenv_as_boolean_value_not_present_default_false_is_false():
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', False)
    assert value_as_boolean is False


def test_getenv_as_boolean_value_not_present_default_true_is_true():
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', True)
    assert value_as_boolean is True


def test_getenv_as_boolean_value_true_lower_case_true():
    os.environ['MY_BOOLEAN_ENV'] = 'true'
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', False)
    assert value_as_boolean is True


def test_getenv_as_boolean_value_true_upper_case_true():
    os.environ['MY_BOOLEAN_ENV'] = 'True'
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', False)
    assert value_as_boolean is True


def test_getenv_as_boolean_value_t_true():
    os.environ['MY_BOOLEAN_ENV'] = 't'
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', False)
    assert value_as_boolean is True


def test_getenv_as_boolean_value_1_true():
    os.environ['MY_BOOLEAN_ENV'] = '1'
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', False)
    assert value_as_boolean is True


def test_getenv_as_boolean_value_false_false():
    os.environ['MY_BOOLEAN_ENV'] = 'FaLsE'
    value_as_boolean = lambda_utils.env_utils.getenv_as_boolean(
        'MY_BOOLEAN_ENV', True)
    assert value_as_boolean is False
