import os
from datetime import timedelta

class Config:
    """Application configuration class"""
    
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
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
    HOSPITAL_NAME = "Easybook Hospital"
    HOSPITAL_OPERATING_HOURS = "Monday - Friday: 8:00 AM - 6:00 PM, Saturday: 9:00 AM - 3:00 PM"
    HOSPITAL_SERVICES = [
        "General Medicine",
        "Emergency Care",
        "Laboratory Services",
        "Radiology",
        "Pharmacy",
        "Outpatient Clinics"
    ]