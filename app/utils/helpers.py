def format_email(email: str) -> str:
    """
    Format the given email address.
    
    This function trims whitespace from the beginning and end of the email,
    and converts it to lowercase.
    
    Args:
        email (str): The input email address.
    
    Returns:
        str: The formatted email address.
    """
    return email.strip().lower()
