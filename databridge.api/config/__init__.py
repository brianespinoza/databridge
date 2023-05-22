import os

# Load the appropriate configuration based on the environment
if os.environ.get('FLASK_ENV') == 'production':
    from .production import Config
else:
    from .development import Config
