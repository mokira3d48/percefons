import re
from .exceptions import (
    InvalidEmailError,
    InvalidUsernameError,
    InvalidNameError,
    InvalidUserPasswordError
)

email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
username_pattern = re.compile(r"[a-z_0-9]")
name_pattern = re.compile(r"[A-Za-z '-]")


def validate_email(value: str):
    """
    Validation function implemented to validate email value.

    :raises InvalidEmailError:
    """
    if not email_pattern.match(value):
        raise InvalidEmailError(
            "The email address provided is not valid. "
            f"Here is the current value of your email: \"{value}\".",
            code='input_error',
            field='email',
        )


def validate_username(value: str):
    """
    Validation function implemented to validate username value.

    :raises InvalidUsernameError:
    """
    if ' ' in value:
        raise InvalidUsernameError(
            "The space character is not allow in username.",
            code='input_error',
            field='username',
        )
    if not username_pattern.match(value):
        raise InvalidUsernameError(
            "The username must be contained only the following "
            "characters: uppercase and lowercase letters (a-z), digit "
            "(0 - 9) and the special character underscore (\"_\").",
            code='input_error',
            field='username',
        )


def validate_name(value: str, field_name: str='name'):
    """
    Validation function implemented to validate a first or last name.

    :raises InvalidNameError:
    """
    if not name_pattern.match(value):
        raise InvalidNameError(
            f"The name input: \"{value}\" is not valid.",
            code='input_error',
            field=field_name,
        )


def validate_user_password(value: str):
    """
    Validation function implemented to validate a user password.

    Requirements:
      - Length: 12-128 characters;
      - At least 2 uppercase letters;
      - At least 2 lowercase letters;
      - At least 2 digits;
      - At least 2 special characters;
      - No more than 2 consecutive identical characters;
      - No sequential characters (abc, 123, etc.);
      - Not in common password list.

    :raises InvalidUserPasswordError:
    """
    # Check length constraints
    if len(value) < 12:
        raise InvalidUserPasswordError(
            "Password must be at least 12 characters long.",
            code='input_error',
            field='password'
        )
    if len(value) > 128:
        raise InvalidUserPasswordError(
            "Password must not exceed 128 characters.",
            code='input_error',
            field='password'
        )
    # Check for uppercase letters (minimum 2):
    uppercase_count = len(re.findall(r'[A-Z]', value))
    if uppercase_count < 2:
        raise InvalidUserPasswordError(
            "Password must contain at least 2 uppercase letters.",
            code='input_error',
            field='password'
        )
    # Check for lowercase letters (minimum 2):
    lowercase_count = len(re.findall(r'[a-z]', value))
    if lowercase_count < 2:
        raise InvalidUserPasswordError(
            "Password must contain at least 2 lowercase letters.",
            code='input_error',
            field='password'
        )
    # Check for digits (minimum 2):
    digit_count = len(re.findall(r'[0-9]', value))
    if digit_count < 2:
        raise InvalidUserPasswordError(
            "Password must contain at least 2 digits.",
            code='input_error',
            field='password'
        )
    # Check for special characters (minimum 2):
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    special_count = len(
        re.findall(f'[{re.escape(special_chars)}]', value)
    )
    if special_count < 2:
        raise InvalidUserPasswordError(
            "Password must contain at least 2 special characters.",
            code='input_error',
            field='password'
        )
    # Check for consecutive repeated characters (no more than 2):
    if re.search(r'(.)\1{2,}', value):
        raise InvalidUserPasswordError(
            "Password cannot contain more than 2 consecutive identical "
            "characters.",
            code='input_error',
            field='password'
        )
