from teacher.models import Teacher

special_chars = "!@"  # $%&'()*+,-./:;<=>?@[\]^_`{|}~"


def password_match(password, password_confirmation, error_list):
    """ Checks if password and password confirmation are equals """
    if password != password_confirmation:
        error_list['password'] = 'Password and Password Confirmation did not match.'


def is_characters_only(input_value, input_label, error_list):
    """ Checks if input contains only characters """
    if any(char.isdigit() for char in input_value):
        error_list[input_label] = f'This field must not contain numbers'
    if any(char in special_chars for char in input_value):
        error_list[input_label] = f'This field must not contain special characters'


def email_is_unique(email, input_label, error_list):
    if Teacher.objects.filter(email=email).exists():
        error_list[input_label] = f'This email is already taken'
