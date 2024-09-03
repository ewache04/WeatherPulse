# utils/assistant/assistant_mode/assistant_mode.py
from utils.sessions.session_utils import update_session, create_session, get_session


def activate_assistant_mode():
    """
    Activates the assistant mode by setting the session value to True.
    If session creation fails, it tries to update the session.
    """
    try:
        create_session('assistant_mode', True)
    except Exception as e:
        print(f"Error creating session: {e}")
        try:
            update_session('assistant_mode', True)
        except Exception as e:
            print(f"Error updating session: {e}")

    # Print the current session value for 'assistant_mode'
    current_value = get_session('assistant_mode')
    print(f"Assistant Mode Activated: {current_value}")


def inactivate_assistant_mode():
    """
    Deactivates the assistant mode by setting the session value to False.
    If session update fails, it tries to create the session.
    """
    try:
        update_session('assistant_mode', False)
    except Exception as e:
        print(f"Error updating session: {e}")
        try:
            create_session('assistant_mode', False)
        except Exception as e:
            print(f"Error creating session: {e}")

    # Print the current session value for 'assistant_mode'
    current_value = get_session('assistant_mode')
    print(f"Assistant Mode Deactivated: {current_value}")
