import re


def email_is_valid(email):

    pattern = r"^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(pattern, email) is not None

email1 = "test@example.com"
email2 = "invalid.email"


print(email_is_valid(email1))
print(email_is_valid(email2))