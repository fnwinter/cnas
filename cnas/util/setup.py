import getpass
import os

from util.config import config
from util.system_path import get_cnas_path


def _prompt_admin_credentials() -> tuple[str, str]:
    """Prompt for admin_id and admin_password (masked, twice). Return (admin_id, admin_password)."""
    admin_id = input("admin_id: ").strip()
    if not admin_id:
        raise ValueError("admin_id cannot be empty")

    while True:
        password = getpass.getpass("admin_password: ")
        password_again = getpass.getpass("admin_password (again): ")
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
            admin_id, admin_password = _prompt_admin_credentials()
            cfg.set("admin_id", admin_id)
            cfg.set("admin_password", admin_password)
            cfg.save()
        except (ValueError, EOFError) as e:
            print(e)
            return False

    return True
