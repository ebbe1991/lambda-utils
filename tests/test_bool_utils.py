from lambda_utils.bool_utils import parse_bool

def test_bool_true():
    input = "true"
    result = parse_bool(input)
    assert result == True


def test_bool_True():
    input = "True"
    result = parse_bool(input)
    assert result == True


def test_bool_1():
    input = "1"
    result = parse_bool(input)
    assert result == True

    
def test_bool_true_bool():
    input = True
    result = parse_bool(input)
    assert result == True


def test_bool_none():
    input = None
    result = parse_bool(input)
    assert result == False


def test_bool_false():
    input = "false"
    result = parse_bool(input)
    assert result == False