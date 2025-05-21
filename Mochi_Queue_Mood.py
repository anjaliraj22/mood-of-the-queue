
import pandas as pd
import streamlit as st
import datetime
import gspread
import plotly.express as px
from google.oauth2.service_account import Credentials

Sheet_Name = "Mood of the Queue" 

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

info = {key: value for key, value in st.secrets["google"].items()}
creds = Credentials.from_service_account_info(info, scopes=scope)
client = gspread.authorize(creds)
sheet = client.open(Sheet_Name).sheet1

#Streamlit UI
st.set_page_config(page_title="Mood of the Queue", layout="centered")
st.title("📊 Mood Logger")

st.markdown("Log the vibe of your ticket below:")

# Mood input form
with st.form("mood_form"):
    moods = [ "🎉 Joyful","😊 Happy","😐 Okay","😕 Confused","😠 Frustrated"]
    mood = st.selectbox("How does this ticket feel to you?", moods)
    note = st.text_input("Optional Note (e.g., 'Rx delays')", "")
    submitted = st.form_submit_button("Submit")

    if submitted:
        timestamp = str(datetime.datetime.now())
        try:
            sheet.append_row([timestamp, mood, note])
            st.success("Mood logged successfully!")
        except Exception as e:
            st.error(f"Failed to log mood: {e}")

# Mood Visualization
st.header("📈 Mood of the Queue Summary")

st.sidebar.header("📆 Filter")
selected_date = st.sidebar.date_input("Choose a Date:", datetime.date.today())

try:
    records = sheet.get_all_records()
    df = pd.DataFrame(records)

    if df.empty:
        st.info("No moods logged yet.")
    else:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df_filtered = df[df['Timestamp'].dt.date == selected_date]

        if df_filtered.empty:
            st.info("No moods logged on this date.")
        else:
            mood_counts = df_filtered['Mood'].value_counts().reset_index()
            mood_counts.columns = ['Mood', 'Count']

            fig = px.bar(mood_counts, x='Mood', y='Count', title="Moods Logged on this Date")
            st.plotly_chart(fig)

except Exception as e:
    st.error(f"Error loading data: {e}")
    
