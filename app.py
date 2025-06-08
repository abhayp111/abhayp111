import streamlit as st
from utils import generate_quiz

import streamlit as st

st.set_page_config(page_title="edu24.ai", layout="centered")

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
            border: none
            font-weight: bold;
            border-radius: 10px;
            padding: 0.5em 1.5em;
        }

        body {
            background-color: black;
        }
        .stApp {
            background-color: black;
        }
    </style>
    <div class="title">📚 Edu24 - AI Quiz Generator</div>
    """,
    unsafe_allow_html=True
)



#st.title("🎓 edu24.ai – Smart Quiz Generator")

st.markdown("Select the subject and number of questions to generate your quiz:")

user_prompt = st.text_area(
    "Enter your quiz prompt", 
    "Generate a quiz on the topic 'Photosynthesis' with 3 multiple-choice questions."
)


# ✅ 1. Subject Selection
subjects = ["Python", "SQL", "Math", "Science", "History", "Cybersecurity", "JavaScript"]
subject = st.selectbox("📘 Select a subject", subjects)

# ✅ 2. Question Count
num_questions = st.slider("🔢 Number of Questions", 1, 10, 5)

custom_prompt = st.text_area("Or enter a custom prompt (will override above):")
quiz=None

# ✅ 3. Generate Quiz
if st.button("Generate Quiz"):
    with st.spinner("Generating quiz..."):
        if custom_prompt.strip():  # If user provided a prompt, use that
            quiz = generate_quiz(custom_prompt)
        else:
            # Use subject and number of questions if no custom prompt
            quiz = generate_quiz(subject, num_questions)
        #quiz = generate_quiz(subject, num_questions)
        st.success("✅ Quiz Generated!")

        for i, q in enumerate(quiz, 1):
            st.markdown(f"**Q{i}. {q['question']}**")
            for opt in q['options']:
                st.markdown(f"- {opt}")
            st.markdown(f"🟢 **Answer:** {q['answer']}")
