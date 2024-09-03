# utils/sessions/session_utils.py
from flask import session


def create_session(key, value):
    """Create or update a session key-value pair."""
    session[key] = value


def update_session(key, value):
    """Update the value of an existing session key."""
    if key in session:
        session[key] = value
    else:
        raise KeyError(f"Session key '{key}' does not exist.")


def get_session(key):
    """
    Retrieves the value of a session variable by its key.

    Args:
        key (str): The key for the session variable you want to retrieve.

    Returns:
        The value of the session variable if it exists, otherwise None.
    """
    return session.get(key, None)


def delete_session(key):
    """Delete a session key-value pair."""
    if key in session:
        session.pop(key)
    else:
        raise KeyError(f"Session key '{key}' does not exist.")


def clear_session():
    """Clear all session data."""
    session.clear()
