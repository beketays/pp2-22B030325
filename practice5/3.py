import re

def is_valid_email(email):
    if "@" in email:
        username, domain = email.split("@")

        username_pattern = r"^\w$"
        domain_pattern = r"^$"

        if re.match(username_pattern, username) and re.match(domain_pattern)

    else:
        print("Not valid email")