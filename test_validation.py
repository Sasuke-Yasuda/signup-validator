from validation import (
    is_valid_username,
    is_valid_email,
    is_valid_password,
    is_valid_age,
    is_valid_terms,
    sign_up
)


def test_username():
    assert is_valid_username("sasuke_9") == True
    assert is_valid_username("sk") == False
    assert is_valid_username("sasuke!") == False
    assert is_valid_username(123) == False


def test_email():
    assert is_valid_email("sasuke@example.com") == True
    assert is_valid_email("sasukeexample.com") == False
    assert is_valid_email("sasuke@@example.com") == False
    assert is_valid_email(123) == False


def test_password():
    assert is_valid_password("secret123") == True
    assert is_valid_password("password") == False
    assert is_valid_password("12345678") == False
    assert is_valid_password(12345678) == False


def test_age():
    assert is_valid_age(13) == True
    assert is_valid_age(120) == True
    assert is_valid_age(12) == False
    assert is_valid_age(121) == False
    assert is_valid_age("15") == False
    assert is_valid_age(True) == False


def test_terms():
    assert is_valid_terms(True) == True
    assert is_valid_terms(False) == False
    assert is_valid_terms("True") == False


def test_sign_up():
    assert sign_up(
        "sasuke_9",
        "sasuke@example.com",
        "secret123",
        15,
        True
    ) == True

    assert sign_up(
        "sk",
        "sasuke@example.com",
        "secret123",
        15,
        True
    ) == False