# login_credentials.py

import os

CREDENTIAL_FILE = "credentials.txt"


def save_user(username, password):
    with open(CREDENTIAL_FILE, "a") as f:
        f.write(f"{username}:{password}\n")


def load_credentials():
    if not os.path.exists(CREDENTIAL_FILE):
        return {}

    creds = {}
    with open(CREDENTIAL_FILE, "r") as f:
        for line in f:
            if ":" in line:
                user, pwd = line.strip().split(":")
                creds[user] = pwd
    return creds


def authenticate(username, password):
    creds = load_credentials()
    return creds.get(username) == password


def user_exists(username):
    creds = load_credentials()
    return username in creds


def get_password(username):
    creds = load_credentials()
    return creds.get(username)


def update_password(username, new_password):
    creds = load_credentials()
    creds[username] = new_password

    with open(CREDENTIAL_FILE, "w") as f:
        for user, pwd in creds.items():
            f.write(f"{user}:{pwd}\n")