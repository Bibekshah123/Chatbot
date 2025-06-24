import re
from email_validator import validate_email, EmailNotValidError
import dateparser

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def is_valid_phone(phone):
    return bool(re.match(r'^\+?\d{10,15}$', phone))

def extract_date(text):
    dt = dateparser.parse(text)
    if dt:
        return dt.strftime("%Y-%m-%d")
    return None
