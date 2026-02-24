import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Love Matcher", page_icon="💘", layout="centered")

# ===== โหลดโมเดลแบบปลอดภัย =====
saved = joblib.load("love_model.pkl")
model = saved["model"]
features = saved["features"]

st.markdown("<h1 style='text-align:center;'>💘 LOVE COMPATIBILITY MATCHER 💘</h1>", unsafe_allow_html=True)
st.markdown("## 👩‍❤️‍👨 กรอกข้อมูลของคุณและคนที่คุณชอบ")

col1, col2 = st.columns(2)

edu_dict = {
    1: "มัธยม",
    2: "ปวช.",
    3: "ปริญญาตรี",
    4: "ปริญญาโท",
    5: "ปริญญาเอก"
}

love_languages = [
    "Words of Affirmation",
    "Acts of Service",
    "Receiving Gifts",
    "Quality Time",
    "Physical Touch"
]

# ===============================
# INPUT
# ===============================

with col1:
    st.markdown("### 🌸 คุณ")
    a_age = st.number_input("อายุของคุณ", 18, 60, 22)
    a_openness = st.slider("Openness", 0.0, 1.0, 0.5)
    a_extraversion = st.slider("Extraversion", 0.0, 1.0, 0.5)
    a_agreeableness = st.slider("Agreeableness", 0.0, 1.0, 0.5)
    a_conscientiousness = st.slider("Conscientiousness", 0.0, 1.0, 0.5)
    a_career = st.slider("Career Ambition", 0.0, 1.0, 0.5)
    a_chronotype = st.slider("Morning ↔ Night Owl", 0.0, 1.0, 0.5)
    a_spontaneity = st.slider("Planner ↔ Free Spirit", 0.0, 1.0, 0.5)
    a_express = st.slider("Emotional Expressiveness", 0.0, 1.0, 0.5)
    a_edu = st.selectbox("Education Level", list(edu_dict.keys()), format_func=lambda x: edu_dict[x])
    a_love = st.selectbox("Love Language", love_languages)

with col2:
    st.markdown("### 💖 คนที่คุณชอบ")
    b_age = st.number_input("อายุของเขา", 18, 60, 22)
    b_openness = st.slider("Openness ", 0.0, 1.0, 0.5)
    b_extraversion = st.slider("Extraversion ", 0.0, 1.0, 0.5)
    b_agreeableness = st.slider("Agreeableness ", 0.0, 1.0, 0.5)
    b_conscientiousness = st.slider("Conscientiousness ", 0.0, 1.0, 0.5)
    b_career = st.slider("Career Ambition ", 0.0, 1.0, 0.5)
    b_chronotype = st.slider("Morning ↔ Night Owl ", 0.0, 1.0, 0.5)
    b_spontaneity = st.slider("Planner ↔ Free Spirit ", 0.0, 1.0, 0.5)
    b_express = st.slider("Emotional Expressiveness ", 0.0, 1.0, 0.5)
    b_edu = st.selectbox("Education Level ", list(edu_dict.keys()), format_func=lambda x: edu_dict[x])
    b_love = st.selectbox("Love Language ", love_languages)

st.markdown("---")

# ===============================
# PREDICTION
# ===============================

if st.button("💘 วิเคราะห์ความรักเลยยย"):

    # ===== Feature Engineering =====

    age_gap = abs(a_age - b_age)

    personality_similarity = 1 - np.mean([
        abs(a_openness - b_openness),
        abs(a_extraversion - b_extraversion),
        abs(a_agreeableness - b_agreeableness),
        abs(a_conscientiousness - b_conscientiousness)
    ])

    career_synergy_score = 1 - abs(a_career - b_career)

    chronotype_match = int(a_chronotype == b_chronotype)

    spontaneity_gap = abs(a_spontaneity - b_spontaneity)

    emotional_gap = abs(a_express - b_express)

    love_language_match = int(a_love == b_love)

    education_gap = abs(a_edu - b_edu)

    # ===== Build input ตามลำดับ features ตอน train =====

    input_dict = {
        "age_gap": age_gap,
        "personality_similarity": personality_similarity,
        "career_synergy_score": career_synergy_score,
        "chronotype_match": chronotype_match,
        "spontaneity_gap": spontaneity_gap,
        "emotional_gap": emotional_gap,
        "love_language_match": love_language_match,
        "education_gap": education_gap
    }

    input_data = np.array([[input_dict[f] for f in features]])

    probability = model.predict_proba(input_data)[0][1]

    st.markdown(f"## 💫 ความเข้ากันได้: {probability*100:.2f}%")

    # ใช้ threshold 0.4 ตาม confusion matrix ที่วิเคราะห์
    if probability >= 0.4:
        st.balloons()
        st.success("💖 มีแนวโน้มเข้ากันได้ดีเลย!")
    else:
        st.snow()
        st.error("😭 ยังไม่ค่อยเข้ากัน แต่ความรักพัฒนาได้เสมอ")
