import getpass
import os
import re

from util.config import config
from util.hash_string import hash_string
from util.system_path import get_cnas_path

_EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)


def _is_valid_email(value: str) -> bool:
    """Return True if value looks like a valid email address."""
    if not value or len(value) > 254:
        return False
    return _EMAIL_PATTERN.match(value) is not None


def _prompt_admin_credentials() -> tuple[str, str]:
    """Prompt for email (admin_id) and admin_password (masked, twice). Return (email, admin_password)."""
    print("===============================")
    print("=== Setup Admin Credentials ===")
    print("===============================")
    while True:
        admin_id = input("Admin ID (email): > ").strip()
        if not admin_id:
            print("Admin ID (email) cannot be empty.")
            continue
        if not _is_valid_email(admin_id):
            print("Invalid Admin ID (email) format. Try again.")
            continue
        break

    while True:
        password = getpass.getpass("Admin Password: > ")
        password_again = getpass.getpass("Admin Password (again): > ")
        if password != password_again:
            print("Passwords do not match. Try again.")
            continue
        if not password:
            print("Password cannot be empty. Try again.")
            continue
        break
    return admin_id, password


def setup() -> bool:
    """
    Setup the CNAS: ensure ~/.cnas and config.json exist (via config),
    and ensure config has admin_id and admin_password (prompt if missing).
    """
    # 1. Ensure ~/.cnas exists (get_cnas_path creates it)
    if not os.path.isdir(get_cnas_path()):
        return False

    # 2. Use config; avoid early_load so we can fix empty file before load
    cfg = config(early_load=False)
    config_file = cfg.config_file

    # 3. Ensure config.json exists and is valid JSON (config may create empty file)
    if not os.path.exists(config_file) or os.path.getsize(config_file) == 0:
        cfg.config_data = {}
        cfg.save()
    cfg.load()

    # 4. Ensure admin_id and admin_password; prompt if missing
    if not cfg.get("admin_id") or not cfg.get("admin_password"):
        try:
            email, admin_password = _prompt_admin_credentials()
            cfg.set("admin_id", hash_string(email))
            cfg.set("admin_password", hash_string(admin_password))
            cfg.save()
        except (ValueError, EOFError) as e:
            print(e)
            return False

    return True
