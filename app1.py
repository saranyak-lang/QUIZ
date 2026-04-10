import streamlit as st
import pandas as pd

# 🔗 Your Google Sheets CSV link
url = "https://docs.google.com/spreadsheets/d/1oaAdVDkGm8JXiVT2DT05NH_hMj9GOhHqqgONmKyNDxg/export?format=csv"

# Load data
df = pd.read_csv(url)

# Page setup
st.set_page_config(page_title="Quiz Dashboard", layout="wide")

st.title("📊 QUIZ DASHBOARD")

# Sidebar menu
menu = st.sidebar.selectbox("Choose Page", ["Dashboard", "Start Quiz"])

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0

if "index" not in st.session_state:
    st.session_state.index = 0

total = len(df)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.subheader("Welcome 👋")
    st.metric("Total Questions", total)
    st.write("Click **Start Quiz** from sidebar")

# ---------------- QUIZ ----------------
elif menu == "Start Quiz":

    i = st.session_state.index

    if i < total:

        st.subheader(f"Q{i+1}: {df.iloc[i,0]}")

        options = [
            df.iloc[i,1],
            df.iloc[i,2],
            df.iloc[i,3],
            df.iloc[i,4]
        ]

        answer = st.radio("Choose answer:", options, key=i)

        if st.button("Submit"):

            if answer == df.iloc[i,5]:
                st.success("Correct ✅")
                st.session_state.score += 1
            else:
                st.error("Wrong ❌")

            st.session_state.index += 1
            st.rerun()

    else:
        st.success("Quiz Completed 🎉")
        st.write("Score:", st.session_state.score, "/", total)
