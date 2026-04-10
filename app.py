import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI Quiz", page_icon="🧠")

st.title("🧠 AI Quiz")

# ---------- Student ID ----------
student_id = st.text_input("Enter Your ID")

if student_id == "":
    st.warning("Please enter ID before attempting")
    st.stop()

# ---------- Questions ----------
questions = {
"Q1": ("Which of the following is a linear data structure?", ["Graph","Tree","Array","Hash Table"]),
"Q2": ("Which SQL command is used to remove a table permanently?", ["DELETE","DROP","REMOVE","ERASE"]),
"Q3": ("Which algorithm is commonly used for shortest path in graphs?", ["Kruskal’s","Dijkstra’s","Prim’s","Bellman-Ford"]),
"Q4": ("Which of the following is a supervised learning algorithm?", ["K-Means","PCA","Linear Regression","Apriori"]),
"Q5": ("Which activation function helps reduce vanishing gradient issues?", ["Sigmoid","Tanh","ReLU","Softmax"]),
"Q6": ("Which metric is best for imbalanced classification problems?", ["Accuracy","Precision","Recall","F1-Score"]),
"Q7": ("Which of the following is NOT a neural network type?", ["CNN","RNN","GAN","Decision Tree"]),
"Q8": ("In machine learning, an ‘epoch’ refers to:", ["One batch update","One forward pass","One backward pass","One complete pass through dataset"]),
"Q9": ("Which loss function is commonly used for binary classification?", ["Mean Squared Error","Cross-Entropy","Huber Loss","Hinge Loss"]),
"Q10": ("Which algorithm is used for dimensionality reduction?", ["Naive Bayes","PCA","Random Forest","SVM"]),
"Q11": ("Which concept is central to reinforcement learning?", ["Reward","Dropout","Overfitting","Gradient Descent"]),
"Q12": ("Which technique prevents overfitting in neural networks?", ["Gradient Clipping","Dropout","Batch Normalization","Learning Rate Scheduling"]),
"Q13": ("Which optimizer uses momentum and adaptive learning rates?", ["SGD","RMSProp","Adagrad","Adam"]),
"Q14": ("Which of the following is an unsupervised learning algorithm?", ["Logistic Regression","Decision Tree","K-Means","Linear Regression"]),
"Q15": ("Which metric is commonly used for regression tasks?", ["Precision","Recall","F1-Score","Mean Absolute Error"]),
"Q16": ("What is Artificial Intelligence?", ["Human intelligence","Machine intelligence","Natural language","Programming language"]),
"Q17": ("Which of the following is an example of AI?", ["Calculator","Washing machine","Chatbot","Keyboard"]),
"Q18": ("Which AI field deals with understanding human language?", ["Computer Vision","NLP","Robotics","Data Mining"]),
"Q19": ("Which AI technique is used in self-driving cars?", ["Machine Learning","Networking","Compiler Design","DBMS"]),
"Q20": ("Which company developed ChatGPT?", ["Google","Microsoft","OpenAI","IBM"]),
"Q21": ("Which of the following is a type of AI agent?", ["Simple Reflex Agent","Random Agent","Passive Agent","Static Agent"]),
"Q22": ("What is the main goal of AI?", ["Replace humans","Solve complex problems","Store data","Design hardware"]),
"Q23": ("Which language is widely used in AI?", ["C","Java","Python","HTML"]),
"Q24": ("Which AI concept allows machines to learn from data?", ["Networking","Machine Learning","Compilation","Encryption"]),
"Q25": ("Which of the following is a real-world AI application?", ["Email spam filter","Printer","Keyboard","Monitor"])
}

correct = {
"Q1":"Array","Q2":"DROP","Q3":"Dijkstra’s","Q4":"Linear Regression","Q5":"ReLU",
"Q6":"F1-Score","Q7":"Decision Tree","Q8":"One complete pass through dataset","Q9":"Cross-Entropy","Q10":"PCA",
"Q11":"Reward","Q12":"Dropout","Q13":"Adam","Q14":"K-Means","Q15":"Mean Absolute Error",
"Q16":"Machine intelligence","Q17":"Chatbot","Q18":"NLP","Q19":"Machine Learning","Q20":"OpenAI",
"Q21":"Simple Reflex Agent","Q22":"Solve complex problems","Q23":"Python","Q24":"Machine Learning","Q25":"Email spam filter"
}

# ---------- Prevent duplicate ----------
file = "data.csv"
if os.path.exists(file):
    df = pd.read_csv(file)
    if student_id in df["ID"].values:
        st.error("You have already submitted!")
        st.stop()

# ---------- Answers ----------
answers[q] = st.radio(
    q + ": " + questions[q][0],
    questions[q][1],
    index=None,
    key=q
)

# ---------- Submit ----------
if st.button("Submit"):

    if None in answers.values():
        st.warning("Please answer all questions before submitting!")
        st.stop()

    score = 0
    for q in correct:
        if answers[q] == correct[q]:
            score += 1

    st.success(f"Your Score: {score}/25")

# ---------- Dashboard ----------
if os.path.exists(file):
    st.subheader("📊 Dashboard")

    df = pd.read_csv(file)
    df = df.sort_values(by="Score", ascending=False)
    df["Rank"] = range(1, len(df)+1)

    st.write(df[["Rank","ID","Score"]])
    st.bar_chart(df.set_index("ID")["Score"])