import streamlit as st
import pandas as pd

st.title("📊 Quiz Dashboard System")

# Correct Answers
correct = {"Q1": "Delhi", "Q2": "8"}

# Quiz Form
name = st.text_input("Enter your name")

q1 = st.radio("Q1: Capital of India?", ["Delhi", "Mumbai", "Chennai", "Kolkata"])
q2 = st.radio("Q2: 5 + 3 = ?", ["6", "7", "8", "9"])

if st.button("Submit"):
    score = 0
    
    if q1 == correct["Q1"]:
        score += 1
    if q2 == correct["Q2"]:
        score += 1

    data = {"Name": name, "Q1": q1, "Q2": q2, "Score": score}
    df = pd.DataFrame([data])

    try:
        old = pd.read_csv("responses.csv")
        df = pd.concat([old, df], ignore_index=True)
    except:
        pass

    df.to_csv("responses.csv", index=False)
    st.success(f"Submitted! Your Score: {score}")

# Dashboard
st.header("📊 Dashboard")

try:
    df = pd.read_csv("responses.csv")

    df = df.sort_values(by="Score", ascending=False)
    df["Rank"] = range(1, len(df) + 1)

    st.subheader("🏆 Leaderboard")
    st.write(df[["Rank", "Name", "Score"]])

    topper = df.iloc[0]
    st.success(f"🥇 Topper: {topper['Name']} (Score: {topper['Score']})")

    st.subheader("Q1 Analysis")
    st.bar_chart(df["Q1"].value_counts())

    st.subheader("Q2 Analysis")
    st.bar_chart(df["Q2"].value_counts())

except:
    st.warning("No data yet")
