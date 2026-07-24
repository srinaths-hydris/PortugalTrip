"""Configuration for Portugal Trip web app."""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """App configuration."""

    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    PREFERRED_URL_SCHEME = 'https' if os.getenv('FLASK_ENV') == 'production' else 'http'

    # Google OAuth
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

    # Whitelist
    ALLOWED_EMAILS = os.getenv('ALLOWED_EMAILS', '').split(',')

    # Session
    SESSION_COOKIE_SECURE = os.getenv('FLASK_ENV') == 'production'
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 604800  # 7 days

    # Weather API (OpenWeatherMap)
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
