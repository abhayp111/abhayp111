import streamlit as st
from utils import generate_quiz,my_prompt

st.set_page_config(page_title="edu24.ai", layout="centered")

# 💄 Styling and Title
st.markdown(
    """
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 20px;
        }
        .footer {
            font-size: 14px;
            text-align: center;
            color: gray;
            margin-top: 50px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: black;
            border: none;
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1.5em;
        }
        .stApp {
            background-color: black;
        }
    </style>
    <div class="title">📚 Edu24 - AI Quiz Generator</div>
    """,
    unsafe_allow_html=True
)

quiz = None

# =====================
# Option 1: Subject-based Quiz
# =====================
st.markdown("### Generate Quiz from Subject")

subjects = ["Python", "SQL", "Math", "Science", "History", "Cybersecurity", "JavaScript","Hindi"]
subject = st.selectbox("📘 Select a subject", subjects)
num_questions = st.slider("🔢 Number of Questions", 1, 10, 5)

if st.button("Generate from Subject"):
    with st.spinner("Generating quiz from subject..."):
        quiz = generate_quiz(subject, num_questions)
    st.success("✅ Quiz Generated from Subject!")

# =====================
# Option 2: Prompt-based Quiz
# =====================
st.markdown("---")
st.markdown("### Generate Quiz from Custom Prompt")

custom_prompt = st.text_area("Enter your full prompt here:", "Generate a quiz on the topic 'Photosynthesis' with 3 questions.")

if st.button("Generate from Prompt"):
    with st.spinner("Generating quiz from custom prompt..."):
        response = my_prompt(custom_prompt)
        print(response)
    st.success("✅ Answer")
    st.markdown("### 📄 Generated Response:")
    st.code(response, language='json') 

# =====================
# Show quiz if available
# =====================
if quiz:
    for i, q in enumerate(quiz, 1):
        st.markdown(f"**Q{i}. {q['question']}**")
        for opt in q['options']:
            st.markdown(f"- {opt}")
        st.markdown(f"🟢 **Answer:** {q['answer']}")


if 'quiz' in st.session_state:
    st.markdown("### 📋 Take the Quiz:")
    user_answers = []

    for i, q in enumerate(st.session_state['quiz'], 1):
        st.markdown(f"**Q{i}. {q['question']}**")
        selected = st.radio(
            f"Select your answer:",
            q['options'],
            key=f"question_{i}"
        )
        user_answers.append((selected, q['answer']))

    if st.button("🧪 Submit Answers"):
        correct_count = 0
        for i, (user_ans, correct_ans) in enumerate(user_answers, 1):
            if user_ans == correct_ans:
                st.success(f"✅ Q{i}: Correct!")
                correct_count += 1
            else:
                st.error(f"❌ Q{i}: Incorrect! Correct answer: {correct_ans}")

        st.markdown(f"### 🏁 Your Score: `{correct_count} / {len(user_answers)}`")

