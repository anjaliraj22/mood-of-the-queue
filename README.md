# Mood of the Queue

This tool helps support agents log the overall "mood" of the patient ticket queue throughout the day and visualize emotional trends.

Streamlit App Link: https://mood-of-the-queue-nw6ngff6g6yes2mmztfm9x.streamlit.app/

## Features

- Log moods with optional notes
- Store entries in a Google Sheet
- Visualize mood counts for the day
- Filter by date
- Lightweight & easy-to-use UI

## Tech Stack

- Python
- Streamlit (UI)
- Google Sheets (Storage)
- Plotly (Visualization)
- gspread + google-auth (Google Sheets integration)

## Setup Instructions

1. Clone this repo
2. Create and download a Google Cloud service account key with access to Google Sheets
3. Share your Google Sheet with the service account email
4. Create a `.streamlit/secrets.toml` file to store your credentials. 

5. Install dependencies:
   ```bash
   pip install -r requirements.txt

