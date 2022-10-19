"""
Emails
Estimate: 20 minutes
Actual:   44 minutes
"""


def main():
    "Create dictionary of emails_to_names"
    email_to_names = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirm_name = input(f"Is your name {name}? (Y/N)")
        if confirm_name.upper() != 'Y' and confirm_name != "":
            name = input('What is your name?: ')
        email_to_names[email] = name
        email = input("Email: ")

    for email, name in email_to_names.items():
        print(f"{name}: {email}")


def extract_name_from_email(email):
    """Extract name from email ."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
