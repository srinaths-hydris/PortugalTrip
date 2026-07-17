# Portugal 2026 Family Trip

## What this is
Family trip itinerary: Porto > Tomar > Lisbon > Algarve > Lisbon Airport (fly home).
Jul 27 - Aug 11, 2026. 2 adults + 2 kids (ages 7 and 3).
Brother-in-law Darshan & sister-in-law Rika join in Algarve Aug 6-9 (fly into Faro from London).

## Files
- `app.py` — Main Flask application with Google OAuth
- `itinerary.md` — Full day-by-day itinerary in markdown
- `data/` — JSON files (itinerary, reservations, checklist, budget, whitelist)
- `templates/` — Jinja2 HTML templates for all pages

## Deployment
- **Production (Heroku):** https://portugal2026-7f6200f7237c.herokuapp.com/
- **Local Dev:** http://localhost:5000 (run `flask run` in venv)
- **GitHub Repo:** github.com/srinaths-hydris/PortugalTrip (PERSONAL — do NOT use git.soma)
- Push with: `git push origin main`

## Key decisions made
- Split car rental: Car 1 Porto>Lisbon (€600, 3 days), Car 2 Lisbon Airport round-trip via Algarve (€950, 5 days)
- Car 2 returned EVENING of Aug 10 (not 5 AM Aug 11) — eliminates flight-morning risk
- Algarve base: Armacao de Pera (Casa Margarida, €1,000, 3 bed)
- Porto: VIVA Miragaia Airbnb (€440)
- Lisbon + Airport hotels: on points
- Tomar: still needs booking
- Benagil catamaran on Day 12 (Fri Aug 7)
- Lagos + Sagres combined loop on Day 13 (Sat Aug 8)
- Day 15 leaves Algarve at 2-3 PM (not 9 AM), hits Belem at golden hour
- Oceanario added to Day 7 arrival afternoon

## Style
- Keep costs inconspicuous (inline with their sections, not a separate budget box)
- Itinerary-only page (no picks/activity selector — removed)
- Collapsible day cards with toggleDay() function
