import re

# Name pattern matches:
# - "John Cena"
# - "Anya Taylor-Joy"
# - "D'Angelo"
# Doesn't match empty string
name = r"^[A-Z][a-zA-Z'-]+(?: [A-Z][a-zA-Z'-]+)+$"
name_regex = re.compile(name)

# Phone number pattern matches:
# - "5555555555"
# - "555-555-5555"
# - "(555) 555-5555"
phone_number = r"^(?:\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# Email pattern matches:
# - "johncena@wwe.com"
# - "john.cena@wwe.com"
# - "john.cena123@wwe.com"
email_address = r"^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)