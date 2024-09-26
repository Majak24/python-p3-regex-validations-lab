import re

# Updated name pattern to handle "D'Angelo" correctly
name_pattern = r'^[A-Z](?:[a-z]+|\'[A-Z])[a-z]*(?:[-\' ][A-Za-z][a-z]*)*$'

# Phone number pattern (unchanged)
phone_pattern = r'^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$'

# Email address pattern (unchanged)
email_pattern = r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Compile the patterns
name_regex = re.compile(name_pattern)
phone_regex = re.compile(phone_pattern)
email_regex = re.compile(email_pattern)

# Test functions
def is_valid_name(name):
    return bool(name_regex.fullmatch(name))

def is_valid_phone_number(phone):
    return bool(phone_regex.fullmatch(phone))

def is_valid_email(email):
    return bool(email_regex.fullmatch(email))