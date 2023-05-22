import hashlib

def generate_hash(password):
    """Generates a hash of the given password."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    """Validates the format of an email address."""
    # Add your email validation logic here
    pass

def parse_request_data(request):
    """Parses and returns the JSON data from a Flask request object."""
    if request.is_json:
        return request.get_json()
    return None

def log_request(request):
    """Logs information about an incoming request."""
    # Add your logging logic here
    pass
