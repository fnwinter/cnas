import hashlib
import secrets


_PBKDF2_ITERATIONS = 100_000
_HASH_NAME = "sha256"
# Fixed salt so same string always yields same hash (for client-side hash comparison).
_FIXED_SALT = b"cnas_config_salt"


def hash_string(value: str) -> str:
    """Hash a string with a fixed salt. Same value always returns the same hash.

    >>> from util.hash_string import hash_string, verify_string
    >>> stored = hash_string("my_secret")
    >>> len(stored) > 0
    True
    >>> hash_string("my_secret") == stored
    True
    >>> verify_string("my_secret", stored)
    True
    >>> verify_string("wrong_value", stored)
    False

    """
    key = hashlib.pbkdf2_hmac(
        _HASH_NAME,
        value.encode("utf-8"),
        _FIXED_SALT,
        _PBKDF2_ITERATIONS,
    )
    return key.hex()


def verify_string(value: str, stored: str) -> bool:
    """Verify a string against a stored hash (hex only, or legacy 'salt_hex:hash_hex').

    >>> from util.hash_string import hash_string, verify_string
    >>> h = hash_string("same_value")
    >>> verify_string("same_value", h)
    True
    >>> verify_string("different_value", h)
    False
    >>> verify_string("same_value", "")
    False
    >>> verify_string("same_value", "invalid")
    False

    """
    if not stored:
        return False
    # New format: stored is key hex only.
    if ":" not in stored:
        return secrets.compare_digest(hash_string(value), stored)
    # Legacy format: salt_hex:hash_hex
    salt_hex, hash_hex = stored.split(":", 1)
    try:
        salt = bytes.fromhex(salt_hex)
        stored_key = bytes.fromhex(hash_hex)
    except ValueError:
        return False
    key = hashlib.pbkdf2_hmac(
        _HASH_NAME,
        value.encode("utf-8"),
        salt,
        _PBKDF2_ITERATIONS,
    )
    return secrets.compare_digest(key, stored_key)
