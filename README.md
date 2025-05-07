# 🎧 RevWrapped - Your Custom Spotify Wrapped

RevWrapped is a personal project that lets you generate your own Spotify Wrapped-style report using Python. It pulls your top tracks and artists using the Spotify Web API and visualizes your listening habits however you want.

---

## 🚀 Features

- 🔐 Secure Spotify authentication using OAuth2
- 🎵 Get your top artists and tracks (long, medium, or short term)
- 📊 Visualize listening data with Python (e.g., bar charts, timelines)
- 📁 Export results for fun sharing or archiving

---

## 🛠 Setup Instructions

### 1. Clone the Repo
```git clone https://github.com/yourusername/RevWrapped.git```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed.
```py -m pip install -r requirements.txt```

If there's no requirements.txt, you can install them manually:
```py -m pip install spotipy pandas matplotlib python-dotenv```

### 3. Set Up Spotify Developer App
Go to Spotify Developer Dashboard
Create a new app
Copy your Client ID and Client Secret

### 4. Create a .env file in the project root:
```SPOTIPY_CLIENT_ID=your_client_id```
```SPOTIPY_CLIENT_SECRET=your_client_secret```
```SPOTIPY_REDIRECT_URI=your_callback_url```

### 5. Run the Project
```py main.py```

