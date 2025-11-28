import os
from datetime import timedelta

class Config:
    """Application configuration class"""
    
    # Secret key for session management
    _default_secret = 'dev-secret-key-change-in-production'
    _secret_key = os.environ.get('SECRET_KEY') or _default_secret
    
    # Warn/error if using default SECRET_KEY in production
    if os.environ.get('FLASK_ENV') == 'production' and _secret_key == _default_secret:
        raise ValueError(
            "ERROR: Using default SECRET_KEY in production is not allowed! "
            "Set a strong SECRET_KEY environment variable before deploying."
        )
    
    SECRET_KEY = _secret_key
    
    # Database configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'easybook.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Application settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Hospital information
    HOSPITAL_NAME = "Easybook"
    HOSPITAL_OPERATING_HOURS = "Monday - Friday: 8:00 AM - 6:00 PM, Saturday: 9:00 AM - 3:00 PM"
    HOSPITAL_SERVICES = [
        "General Medicine",
        "Emergency Care",
        "Laboratory Services",
        "Radiology",
        "Pharmacy",
        "Outpatient Clinics"
    ]