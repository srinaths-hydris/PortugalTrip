# Portugal Trip 2026 - Web Application

A secure, feature-rich web app for managing our Portugal family trip.

## ✅ What's Been Set Up

### Core Infrastructure
- ✅ Flask web framework
- ✅ Google OAuth authentication
- ✅ Email whitelist security
- ✅ Session management
- ✅ Heroku deployment configuration

### Project Structure
```
PortugalTrip/
├── app.py                    # Main Flask application
├── auth.py                   # Google OAuth logic
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku dyno configuration
├── runtime.txt               # Python version
├── .env.example              # Environment variables template
├── .gitignore                # Git exclusions
│
├── static/                   # CSS, JS, images
├── templates/                # HTML templates
└── data/                     # JSON data files
```

## 🔐 Security Features

- **Google OAuth**: Only whitelisted emails can access
- **Session-based auth**: Stay logged in for 7 days
- **HTTPS enforced** (on Heroku)
- **Email whitelist**: Configured via environment variable

## 📋 Features (In Progress)

### Pages
- [x] Login page with Google OAuth
- [ ] Dashboard (overview, countdown, weather)
- [ ] Itinerary (15 days, calendar view, modal)
- [ ] Reservations (flights, hotels, cars, tours)
- [ ] Checklist (pre-trip todos)
- [ ] Attractions (searchable guide)
- [ ] Budget (cost breakdown)

## 🚀 Next Steps for You

### 1. Set Up Google OAuth

Follow the instructions in `GOOGLE_OAUTH_SETUP.md`:
1. Create Google Cloud project
2. Enable OAuth
3. Configure consent screen
4. Add 5 test user emails
5. Get Client ID and Client Secret

### 2. Provide Email Whitelist

Send me the 5 email addresses that should have access:
1. Your email
2. Nirupa's email
3. Darshan's email
4. Rika's email
5. Another email

### 3. I'll Complete the Build

Once you provide the emails and OAuth credentials, I'll:
- Create all remaining pages
- Convert your itinerary and reservations to JSON
- Build the interactive features
- Deploy to Heroku
- Give you the live URL

## 🛠️ Development Setup (Later)

Once deployed, if you want to run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your OAuth credentials

# Run locally
python app.py

# Visit http://localhost:5000
```

## 📦 Heroku Deployment (I'll Handle This)

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY="..."
heroku config:set GOOGLE_CLIENT_ID="..."
heroku config:set GOOGLE_CLIENT_SECRET="..."
heroku config:set ALLOWED_EMAILS="email1,email2,email3,email4,email5"

# Deploy
git push heroku main

# Open app
heroku open
```

## 🎯 Current Status

**Completed:**
- Flask app structure
- Google OAuth authentication
- Login/logout routes
- Email whitelist checking
- Session management
- Heroku configuration files

**In Progress:**
- Converting itinerary.md to JSON
- Building all page templates
- Creating interactive features
- Styling and responsiveness

**Next:** Waiting for your Google OAuth credentials and email whitelist!

---

**Questions?** Let me know once you've completed the Google OAuth setup!
