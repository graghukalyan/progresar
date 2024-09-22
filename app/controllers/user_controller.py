from app.services.network_service import send_invite
from app.models.user import User

def create_user(name: str, email: str) -> User:
    """
    Create a new user and send them an invite.

    Args:
        name (str): The name of the user.
        email (str): The email of the user.

    Returns:
        User: The newly created User object.
    """
    # Create a new User object
    user = User(name, email)
    
    # Send an invite to the new user
    send_invite(user)
    
    return user
