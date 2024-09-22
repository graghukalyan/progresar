from app.models.user import User

def send_invite(user: User):
    """
    Send an invite to the given user.

    This function simulates sending an invite by printing a message.

    Args:
        user (User): The user to send the invite to.
    """
    print(f"Sending invite to {user.email}")
