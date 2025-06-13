import streamlit as st
from utilities import load_medication, load_user, check_medication #Getting stuff from utilities

st.title("Medicine Reminder AI")

schedule = load_medication("data/medication_schedule.json")
user_logs = load_user("data/user_samples.csv")

user_id = "user_001" #Only works with 1 user :/
time_window = 30 #Minutes

due_meds = check_medication(schedule, user_logs, user_id=user_id, time_window=time_window)

if due_meds: #Is this a boolean
  st.subheader("Medications you need to take immediately:")
  for med in due_meds:
    st.markdown(f"- **{med}**")
else:
  st.success("You're all caught up on your medications for now :)")
