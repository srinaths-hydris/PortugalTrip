"""Portugal Trip 2026 - Family Itinerary Web App"""
from flask import Flask, render_template, redirect, url_for, session, flash, jsonify, request
from werkzeug.middleware.proxy_fix import ProxyFix
from functools import wraps
import json
import os
from datetime import datetime

from config import Config
import auth

app = Flask(__name__)
app.config.from_object(Config)

# Handle Heroku proxy headers (for HTTPS detection)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Initialize OAuth
auth.init_oauth(app)

# Helper: require authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not auth.is_authenticated():
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

# Helper: load JSON data
def load_data(filename):
    """Load JSON data file."""
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    return None

# Helper: save JSON data
def save_data(filename, data):
    """Save JSON data file."""
    filepath = os.path.join('data', filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

# =====================
# AUTH ROUTES
# =====================

@app.route('/login')
def login_page():
    """Login page."""
    if auth.is_authenticated():
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/auth/google')
def auth_google():
    """Initiate Google OAuth."""
    return auth.login()

@app.route('/auth/callback')
def auth_callback():
    """Handle OAuth callback."""
    user_info, error = auth.callback()

    if error:
        flash(error, 'error')
        return redirect(url_for('login_page'))

    flash(f"Welcome, {user_info.get('name')}!", 'success')
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    """Logout user."""
    auth.logout()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login_page'))

# =====================
# MAIN ROUTES
# =====================

@app.route('/')
def index():
    """Redirect to dashboard or login."""
    if auth.is_authenticated():
        return redirect(url_for('dashboard'))
    return redirect(url_for('login_page'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Dashboard with overview."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])
    trip_date = datetime(2026, 7, 27)
    days_until = (trip_date - datetime.now()).days

    # Load checklist for quick stats
    checklist = load_data('checklist.json')
    completed_items = 0
    total_items = 0
    if checklist and 'items' in checklist:
        total_items = len(checklist['items'])
        completed_items = sum(1 for item in checklist['items'] if item.get('completed', False))

    return render_template('dashboard.html',
                         user=user,
                         days_until=days_until,
                         trip_date=trip_date,
                         completed_items=completed_items,
                         total_items=total_items)

@app.route('/itinerary')
@login_required
def itinerary():
    """Full itinerary page."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])
    itinerary_data = load_data('itinerary.json')
    return render_template('itinerary.html',
                         user=user,
                         itinerary=itinerary_data)

@app.route('/reservations')
@login_required
def reservations():
    """Reservations page."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])
    reservations_data = load_data('reservations.json')
    return render_template('reservations.html',
                         user=user,
                         reservations=reservations_data)

@app.route('/checklist')
@login_required
def checklist():
    """Pre-trip checklist."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])
    checklist_data = load_data('checklist.json') or {
        'items': [
            {'id': 1, 'text': 'Book Tomar hotel', 'completed': False, 'priority': 'high'},
            {'id': 2, 'text': 'Book Pena Palace tickets (Day 10)', 'completed': False, 'priority': 'high'},
            {'id': 3, 'text': 'Book Benagil catamaran (Day 12)', 'completed': False, 'priority': 'high'},
            {'id': 4, 'text': 'Book Algarve restaurants (group of 6)', 'completed': False, 'priority': 'medium'},
            {'id': 5, 'text': 'Confirm Darshan & Rika Faro flight times', 'completed': False, 'priority': 'medium'},
            {'id': 6, 'text': 'Set alarms for 4:30 AM on Aug 11', 'completed': False, 'priority': 'high'},
            {'id': 7, 'text': 'Download offline maps for Portugal', 'completed': False, 'priority': 'low'},
            {'id': 8, 'text': 'Print hotel confirmations', 'completed': False, 'priority': 'low'},
        ]
    }
    return render_template('checklist.html',
                         user=user,
                         checklist=checklist_data)

@app.route('/attractions')
@login_required
def attractions():
    """Attractions guide."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])
    attractions_data = load_data('attractions.json')
    comments_data = load_data('comments.json')
    return render_template('attractions.html',
                         user=user,
                         attractions=attractions_data,
                         comments=comments_data)

@app.route('/budget')
@login_required
def budget():
    """Budget breakdown - Admin only."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])

    # Check if user is admin
    if not user['is_admin']:
        flash('Access denied. Budget is admin-only.', 'error')
        return redirect(url_for('dashboard'))

    budget_data = load_data('budget.json')
    return render_template('budget.html',
                         user=user,
                         budget=budget_data)

@app.route('/admin')
@login_required
def admin():
    """Admin page - manage whitelist."""
    user = auth.get_user()
    user['is_admin'] = auth.is_admin(user['email'])

    # Check if user is admin
    if not user['is_admin']:
        flash('Access denied. Admin only.', 'error')
        return redirect(url_for('dashboard'))

    whitelist = auth.load_whitelist()

    # Normalize admin_emails format for template
    if 'admin_emails' not in whitelist:
        old_admin = whitelist.get('admin_email', 'srinaths@gmail.com')
        whitelist['admin_emails'] = [old_admin]

    return render_template('admin.html',
                         user=user,
                         whitelist=whitelist)

# =====================
# API ROUTES
# =====================

@app.route('/api/checklist/toggle/<int:item_id>', methods=['POST'])
@login_required
def toggle_checklist_item(item_id):
    """Toggle checklist item completion."""
    checklist_data = load_data('checklist.json')
    if checklist_data:
        for item in checklist_data['items']:
            if item['id'] == item_id:
                item['completed'] = not item['completed']
                save_data('checklist.json', checklist_data)
                return jsonify({'success': True, 'completed': item['completed']})
    return jsonify({'success': False}), 404

@app.route('/api/admin/whitelist/add', methods=['POST'])
@login_required
def add_to_whitelist():
    """Add email to whitelist."""
    user = auth.get_user()

    if not auth.is_admin(user['email']):
        return jsonify({'success': False, 'error': 'Admin only'}), 403

    email = request.json.get('email', '').strip()

    if not email:
        return jsonify({'success': False, 'error': 'Email required'}), 400

    whitelist = auth.load_whitelist()

    if email.lower() in [e.lower() for e in whitelist['allowed_emails']]:
        return jsonify({'success': False, 'error': 'Email already exists'}), 400

    whitelist['allowed_emails'].append(email)
    whitelist['updated_at'] = datetime.utcnow().isoformat() + 'Z'
    whitelist['updated_by'] = user['email']

    auth.save_whitelist(whitelist)

    return jsonify({'success': True, 'email': email})

@app.route('/api/admin/whitelist/remove', methods=['POST'])
@login_required
def remove_from_whitelist():
    """Remove email from whitelist."""
    user = auth.get_user()

    if not auth.is_admin(user['email']):
        return jsonify({'success': False, 'error': 'Admin only'}), 403

    email = request.json.get('email', '').strip()

    whitelist = auth.load_whitelist()

    # Support both old and new format
    admin_emails = whitelist.get('admin_emails', [])
    if not admin_emails:
        admin_email = whitelist.get('admin_email', 'srinaths@gmail.com')
        admin_emails = [admin_email]

    # Can't remove admins
    if email.lower() in [a.lower() for a in admin_emails]:
        return jsonify({'success': False, 'error': 'Cannot remove admin'}), 400

    # Remove email
    whitelist['allowed_emails'] = [e for e in whitelist['allowed_emails'] if e.lower() != email.lower()]
    whitelist['updated_at'] = datetime.utcnow().isoformat() + 'Z'
    whitelist['updated_by'] = user['email']

    auth.save_whitelist(whitelist)

    return jsonify({'success': True})

@app.route('/api/admin/promote', methods=['POST'])
@login_required
def promote_to_admin():
    """Promote user to admin - Admin only."""
    user = auth.get_user()

    # Only admins can promote
    if not auth.is_admin(user['email']):
        return jsonify({'success': False, 'error': 'Admin only'}), 403

    email = request.json.get('email', '').strip()

    if not email:
        return jsonify({'success': False, 'error': 'Email required'}), 400

    whitelist = auth.load_whitelist()

    # Ensure admin_emails array exists
    if 'admin_emails' not in whitelist:
        old_admin = whitelist.get('admin_email', 'srinaths@gmail.com')
        whitelist['admin_emails'] = [old_admin]
        if 'admin_email' in whitelist:
            del whitelist['admin_email']

    # Check if already admin
    if email.lower() in [a.lower() for a in whitelist['admin_emails']]:
        return jsonify({'success': False, 'error': 'Already an admin'}), 400

    # Add to admin list
    whitelist['admin_emails'].append(email)

    # Ensure they're also in allowed_emails
    if email.lower() not in [e.lower() for e in whitelist['allowed_emails']]:
        whitelist['allowed_emails'].append(email)

    whitelist['updated_at'] = datetime.utcnow().isoformat() + 'Z'
    whitelist['updated_by'] = user['email']

    auth.save_whitelist(whitelist)

    return jsonify({'success': True, 'email': email})

@app.route('/api/attractions/<attraction_id>/comments', methods=['GET'])
@login_required
def get_comments(attraction_id):
    """Get comments for an attraction."""
    comments_data = load_data('comments.json')
    if not comments_data:
        return jsonify({'success': False, 'error': 'Comments data not found'}), 404

    attraction_comments = comments_data.get('attractions', {}).get(attraction_id, [])
    return jsonify({'success': True, 'comments': attraction_comments})

@app.route('/api/attractions/<attraction_id>/comments', methods=['POST'])
@login_required
def add_comment(attraction_id):
    """Add a comment to an attraction."""
    user = auth.get_user()
    comment_text = request.json.get('comment', '').strip()

    if not comment_text:
        return jsonify({'success': False, 'error': 'Comment text required'}), 400

    comments_data = load_data('comments.json') or {'attractions': {}}

    if 'attractions' not in comments_data:
        comments_data['attractions'] = {}

    if attraction_id not in comments_data['attractions']:
        comments_data['attractions'][attraction_id] = []

    new_comment = {
        'id': len(comments_data['attractions'][attraction_id]) + 1,
        'user': user['name'],
        'email': user['email'],
        'text': comment_text,
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }

    comments_data['attractions'][attraction_id].append(new_comment)
    save_data('comments.json', comments_data)

    return jsonify({'success': True, 'comment': new_comment})

# =====================
# ERROR HANDLERS
# =====================

if __name__ == '__main__':
    app.run(debug=True, port=5000)
