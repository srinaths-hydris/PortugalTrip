# Portugal 2026 Family Trip Planner

Web app for managing family trip itinerary, reservations, and checklist.

## Features
- 📅 Day-by-day itinerary with activities
- 🎫 Reservations tracker (hotels, cars, tickets, flights)
- ✅ Pre-trip checklist with progress tracking
- 🍽️ Dining recommendations
- 🏰 Attractions library (scheduled + optional)
- 🌤️ Live weather updates
- 💰 Budget tracker (admin-only)
- 🔐 Google OAuth login with email whitelist

## Setup

### 1. Clone and Install
```bash
git clone https://github.com/srinaths-hydris/PortugalTrip.git
cd PortugalTrip
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your values:
# - GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET (from Google Cloud Console)
# - SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_hex(32))")
# - WEATHER_API_KEY (sign up at https://openweathermap.org/api - free tier)
# - ALLOWED_EMAILS (comma-separated list of authorized users)
```

### 3. Run Locally
```bash
flask run
# Open http://localhost:5000
```

## Deployment to Heroku

### Option 1: Heroku CLI (Manual Push)
```bash
# Login to Heroku
heroku login

# Push to Heroku
git push heroku main

# Set environment variables on Heroku
heroku config:set GOOGLE_CLIENT_ID=your-id
heroku config:set GOOGLE_CLIENT_SECRET=your-secret
heroku config:set SECRET_KEY=your-key
heroku config:set WEATHER_API_KEY=your-weather-key
heroku config:set ALLOWED_EMAILS=email1@gmail.com,email2@gmail.com
heroku config:set FLASK_ENV=production
```

### Option 2: GitHub Auto-Deploy (Recommended)
1. Go to Heroku dashboard → https://dashboard.heroku.com/apps/portugal2026
2. Click **Deploy** tab
3. Under "Deployment method", select **GitHub**
4. Connect your GitHub account and select the `PortugalTrip` repo
5. Enable **Automatic deploys** from the `main` branch
6. Click **Deploy Branch** to trigger initial deploy

**With auto-deploy enabled:** Every `git push origin main` will automatically deploy to Heroku!

### Set Environment Variables on Heroku
Go to **Settings** tab → **Config Vars** → Add:
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `SECRET_KEY`
- `WEATHER_API_KEY`
- `ALLOWED_EMAILS`
- `FLASK_ENV=production`

## Weather API Setup

1. Sign up at https://openweathermap.org/api (free tier: 1,000 calls/day)
2. Get your API key from https://home.openweathermap.org/api_keys
3. Add to `.env` locally or Heroku config vars:
   ```
   WEATHER_API_KEY=your-api-key-here
   ```

Without the API key, weather will show "N/A" but the app will still work.

## Tech Stack
- **Backend:** Flask + Python
- **Auth:** Google OAuth 2.0 (Authlib)
- **Deployment:** Heroku (gunicorn)
- **Weather:** OpenWeatherMap API
- **Data:** JSON files (no database needed for this small app)

## Project Structure
```
PortugalTrip/
├── app.py                 # Main Flask app
├── auth.py                # Google OAuth logic
├── config.py              # App configuration
├── data/                  # JSON data files
│   ├── itinerary.json     # Full trip itinerary
│   ├── reservations.json  # Hotels, cars, tickets
│   ├── checklist.json     # Pre-trip tasks
│   ├── budget.json        # Budget tracker
│   └── whitelist.json     # Authorized users
├── templates/             # Jinja2 HTML templates
├── static/                # CSS, JS, images
├── Procfile               # Heroku process file
└── requirements.txt       # Python dependencies
```

## Admin Access
Budget page is restricted to admin emails configured in `data/whitelist.json`:
```json
{
  "admin_emails": [
    "srinaths@gmail.com",
    "nirupa61@gmail.com"
  ]
}
```

## Live Site
🌐 https://portugal2026-7f6200f7237c.herokuapp.com/

## Support
For issues, check the [GitHub repo](https://github.com/srinaths-hydris/PortugalTrip/issues).
