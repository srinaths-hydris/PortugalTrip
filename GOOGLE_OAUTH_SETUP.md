# Google Cloud OAuth Setup Instructions

Follow these steps to create a Google Cloud project and get OAuth credentials for the Portugal Trip web app.

---

## Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Click **"Select a project"** dropdown at the top → **"New Project"**
4. Enter project details:
   - **Project name:** `PortugalTrip2026` (or any name you like)
   - **Organization:** Leave as default (No organization)
5. Click **"Create"**
6. Wait a few seconds for the project to be created
7. Make sure the new project is selected in the top dropdown

---

## Step 2: Enable Google+ API

1. In the left sidebar, click **"APIs & Services"** → **"Library"**
2. Search for: **"Google+ API"**
3. Click on **"Google+ API"** from the results
4. Click the blue **"Enable"** button
5. Wait for it to enable (takes a few seconds)

---

## Step 3: Configure OAuth Consent Screen

1. In the left sidebar, click **"OAuth consent screen"**
2. Select **"External"** (unless you have a Google Workspace organization)
3. Click **"Create"**
4. Fill out the required fields:

### App Information
- **App name:** `Portugal Trip 2026`
- **User support email:** (select your email from dropdown)
- **App logo:** (optional, skip for now)

### App Domain (optional - can skip all)
- Leave blank for now

### Developer Contact Information
- **Email addresses:** (enter your email)

5. Click **"Save and Continue"**

### Scopes Page
6. Click **"Add or Remove Scopes"**
7. Filter/search for these scopes and check them:
   - `userinfo.email`
   - `userinfo.profile`
   - `openid`
8. Click **"Update"** at the bottom
9. Click **"Save and Continue"**

### Test Users Page
10. Click **"+ Add Users"**
11. Add all 5 email addresses that should have access:
    ```
    your-email@example.com
    nirupa-email@example.com
    darshan-email@example.com
    rika-email@example.com
    another-email@example.com
    ```
12. Click **"Add"**
13. Click **"Save and Continue"**

### Summary Page
14. Review and click **"Back to Dashboard"**

---

## Step 4: Create OAuth Credentials

1. In the left sidebar, click **"Credentials"**
2. Click **"+ Create Credentials"** at the top → Select **"OAuth client ID"**
3. If prompted to configure consent screen again, ignore (you already did it)
4. Fill out the form:

### Application Type
- Select: **"Web application"**

### Name
- **Name:** `Portugal Trip Web App`

### Authorized JavaScript Origins
- Click **"+ Add URI"**
- Add: `http://localhost:5000` (for local testing)

### Authorized Redirect URIs
- Click **"+ Add URI"**
- Add: `http://localhost:5000/auth/callback` (for local testing)

5. Click **"Create"**

---

## Step 5: Get Your Credentials

A popup will appear with your credentials:

1. **Copy the Client ID** - it looks like:
   ```
   123456789-abcdefghijklmnop.apps.googleusercontent.com
   ```

2. **Copy the Client Secret** - it looks like:
   ```
   GOCSPX-abcdefghijklmnopqrstuvwxyz
   ```

3. **IMPORTANT:** Save these somewhere safe! You'll need them in the next step.

4. Click **"OK"** to close the popup

---

## Step 6: Download Credentials (Optional Backup)

1. On the Credentials page, you'll see your new OAuth 2.0 Client ID listed
2. Click the **download icon** (⬇️) on the right side of your client
3. This downloads a JSON file - keep it safe as a backup

---

## Step 7: Update Redirect URI for Heroku (Production)

**IMPORTANT:** Your Heroku app is deployed at: `https://portugal2026-7f6200f7237c.herokuapp.com/`

You MUST add this redirect URI to Google Cloud Console:

1. Go back to **"Credentials"** in Google Cloud Console
2. Click on your **"Portugal Trip Web App"** OAuth client
3. Under **"Authorized redirect URIs"**, click **"+ Add URI"**
4. Add EXACTLY this (no trailing slash):
   ```
   https://portugal2026-7f6200f7237c.herokuapp.com/auth/callback
   ```
5. Under **"Authorized JavaScript Origins"**, click **"+ Add URI"**
6. Add:
   ```
   https://portugal2026-7f6200f7237c.herokuapp.com
   ```
7. Click **"Save"**
8. Wait 5-10 minutes for the changes to propagate

---

## What's Next?

Once you have your **Client ID** and **Client Secret**, send them to me and I'll:
1. Add them to the Flask app configuration
2. Set up the `.env` file for local testing
3. Show you how to configure them as environment variables in Heroku

---

## Troubleshooting

### "Access blocked: This app's request is invalid"
- Make sure you added yourself as a Test User in Step 3
- Make sure the redirect URI exactly matches what's in the code

### "Error 400: redirect_uri_mismatch"
- Check that the redirect URI in Google Cloud matches exactly: `http://localhost:5000/auth/callback`
- No trailing slash, exact match including http vs https

### Can't find Google+ API
- It might be deprecated - alternatively enable "Google Identity Services" or just proceed without it. The OAuth will still work.

---

**Ready to proceed?** Once you have your Client ID and Client Secret, paste them here and I'll continue with the Flask app setup!
