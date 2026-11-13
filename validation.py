
def is_valid_username(username):
    if not isinstance(username, str):
        return False

    if len(username) < 3 or len(username) > 20:
        return False

    if not username.replace("_", "").isalnum():
        return False

    return True


def is_valid_email(email):
    if not isinstance(email, str):
        return False

    if email.count("@") != 1:
        return False

    parts = email.split("@")

    if not parts[0]:
        return False

    if "." not in parts[1]:
        return False

    return True


def is_valid_password(password):
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)

    if not has_letter or not has_number:
        return False

    return True


def is_valid_age(age):
    if type(age) != int:
        return False

    if age < 13 or age > 120:
        return False

    return True


def is_valid_terms(accepted_terms):
    return accepted_terms is True


def sign_up(username, email, password, age, accepted_terms):
    return (
        is_valid_username(username)
        and is_valid_email(email)
        and is_valid_password(password)
        and is_valid_age(age)
        and is_valid_terms(accepted_terms)
    )
