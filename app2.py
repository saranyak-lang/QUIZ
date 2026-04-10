import streamlit as st
import pandas as pd

# ---------------- GOOGLE SHEET (QUIZ DATA) ----------------
url = "https://docs.google.com/spreadsheets/d/1oaAdVDkGm8JXiVT2DT05NH_hMj9GOhHqqgONmKyNDxg/export?format=csv"
df = pd.read_csv(url)

st.set_page_config(page_title="Quiz System", layout="wide")

st.title("📊 MULTI-STUDENT QUIZ DASHBOARD")

# ---------------- SESSION STATE ----------------
if "index" not in st.session_state:
    st.session_state.index = 0

if "selected" not in st.session_state:
    st.session_state.selected = None

if "scores" not in st.session_state:
    st.session_state.scores = {}

# ---------------- SIDEBAR LOGIN ----------------
st.sidebar.subheader("👤 Student Login")

name = st.sidebar.text_input("Name")
roll = st.sidebar.text_input("Roll No")

key = f"{name}_{roll}"

menu = st.sidebar.selectbox("Menu", ["Dashboard", "Start Quiz", "Leaderboard"])

total = len(df)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.subheader("📊 Dashboard")
    st.metric("Total Questions", total)
    st.info("Enter Name & Roll No then start quiz")

# ---------------- QUIZ ----------------
elif menu == "Start Quiz":

    if not name or not roll:
        st.warning("Please enter Name and Roll No")
    else:

        i = st.session_state.index

        if i < total:

            st.subheader(f"Q{i+1}: {df.iloc[i,0]}")

            a = df.iloc[i,1]
            b = df.iloc[i,2]
            c = df.iloc[i,3]
            d = df.iloc[i,4]

            st.write(f"A. {a}")
            st.write(f"B. {b}")
            st.write(f"C. {c}")
            st.write(f"D. {d}")

            st.markdown("---")
            st.write("👉 Select Answer:")

            col1, col2, col3, col4 = st.columns(4)

            if col1.button("A"):
                st.session_state.selected = a
            if col2.button("B"):
                st.session_state.selected = b
            if col3.button("C"):
                st.session_state.selected = c
            if col4.button("D"):
                st.session_state.selected = d

            st.write("Selected:", st.session_state.selected)

            if st.button("Submit Answer"):

                correct = df.iloc[i,5]

                if key not in st.session_state.scores:
                    st.session_state.scores[key] = 0

                if st.session_state.selected == correct:
                    st.success("Correct ✅")
                    st.session_state.scores[key] += 1
                else:
                    st.error("Wrong ❌")

                st.session_state.index += 1
                st.session_state.selected = None
                st.rerun()

        else:
            st.success("Quiz Completed 🎉")

            score = st.session_state.scores.get(key, 0)

            st.write(f"### Final Score: {score} / {total}")

            percent = (score / total) * 100
            st.progress(percent / 100)

            if percent >= 80:
                st.success("Excellent 🌟")
            elif percent >= 50:
                st.warning("Good 👍")
            else:
                st.error("Try Again ❌")

# ---------------- LEADERBOARD ----------------
elif menu == "Leaderboard":

    st.subheader("🏆 Leaderboard (Rank 1 - 50)")

    if len(st.session_state.scores) == 0:
        st.info("No students have completed the quiz yet.")
    else:

        data = []

        for student, score in st.session_state.scores.items():
            name_, roll_ = student.split("_")
            percent = (score / total) * 100

            data.append([name_, roll_, score, percent])

        leaderboard = pd.DataFrame(data, columns=["Name", "Roll No", "Score", "Percentage"])

        leaderboard = leaderboard.sort_values(by="Score", ascending=False).reset_index(drop=True)

        leaderboard["Rank"] = leaderboard.index + 1

        st.dataframe(leaderboard[["Rank", "Name", "Roll No", "Score", "Percentage"]])
