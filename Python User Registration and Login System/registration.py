# registration.py

import re

def validate_username(username: str) -> bool:
    """
    Validation rules (from your PDF):
    - Must contain '@'
    - Must contain '.' after '@'
    - No special characters or numbers at the beginning
    - No '.' immediately after '@'
    """
    if not username or "@" not in username:
        return False

    # Cannot start with number/special char
    if not username[0].isalpha():
        return False

    # Must contain "." after "@"
    at_index = username.index("@")
    if "." not in username[at_index:]:
        return False

    # No . immediately after @ — invalid my@.in
    if username[at_index + 1] == ".":
        return False

    return True


def validate_password(password: str) -> bool:
    """
    Rules:
    - 6 to 16 characters
    - At least one uppercase, one lowercase, one digit, one special character
    """

    if len(password) < 6 or len(password) > 16:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True