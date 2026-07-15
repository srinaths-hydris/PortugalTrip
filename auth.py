"""Google OAuth authentication."""
import json
import os
from flask import redirect, request, url_for, session
from authlib.integrations.flask_client import OAuth
import requests
from datetime import datetime

oauth = OAuth()

def init_oauth(app):
    """Initialize OAuth with Flask app."""
    oauth.init_app(app)

    oauth.register(
        name='google',
        client_id=app.config['GOOGLE_CLIENT_ID'],
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

def is_authenticated():
    """Check if user is authenticated."""
    return 'user' in session

def load_whitelist():
    """Load whitelist from JSON file."""
    filepath = 'data/whitelist.json'
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return {'admin_emails': ['srinaths@gmail.com'], 'allowed_emails': ['srinaths@gmail.com']}

def save_whitelist(whitelist_data):
    """Save whitelist to JSON file."""
    filepath = 'data/whitelist.json'
    with open(filepath, 'w') as f:
        json.dump(whitelist_data, f, indent=2)

def is_allowed_email(email):
    """Check if email is in whitelist."""
    whitelist = load_whitelist()
    allowed = whitelist.get('allowed_emails', [])
    return email.lower().strip() in [e.lower().strip() for e in allowed if e]

def is_admin(email):
    """Check if email is an admin."""
    whitelist = load_whitelist()
    # Support both old format (admin_email) and new format (admin_emails)
    admins = whitelist.get('admin_emails', [])
    if not admins:
        admin = whitelist.get('admin_email', 'srinaths@gmail.com')
        admins = [admin]
    return email.lower().strip() in [a.lower().strip() for a in admins if a]

def get_user():
    """Get current user from session."""
    return session.get('user')

def login():
    """Initiate Google OAuth login."""
    redirect_uri = url_for('auth_callback', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

def callback():
    """Handle OAuth callback."""
    token = oauth.google.authorize_access_token()
    user_info = token.get('userinfo')

    if not user_info:
        return None, "Failed to get user info from Google"

    email = user_info.get('email')

    if not is_allowed_email(email):
        return None, f"Access denied. Email {email} is not authorized."

    # Store user info in session
    session['user'] = {
        'email': email,
        'name': user_info.get('name'),
        'picture': user_info.get('picture')
    }
    session.permanent = True

    return user_info, None

def logout():
    """Clear user session."""
    session.pop('user', None)
