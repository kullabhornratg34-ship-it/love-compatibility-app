import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Love Matcher", page_icon="💘", layout="centered")

# โหลดโมเดล
model = joblib.load("love_model.pkl")

st.markdown("<h1>💘 LOVE COMPATIBILITY MATCHER 💘</h1>", unsafe_allow_html=True)
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

# ===== Encode Love Language =====
def encode_love(lang):
    return [1 if lang == l else 0 for l in love_languages]

if st.button("💘 วิเคราะห์ความรักเลยยย"):
    
    a_love_encoded = encode_love(a_love)
    b_love_encoded = encode_love(b_love)

    input_data = np.array([[
        a_age,b_age,
        a_openness,b_openness,
        a_extraversion,b_extraversion,
        a_agreeableness,b_agreeableness,
        a_conscientiousness,b_conscientiousness,
        a_career,b_career,
        a_chronotype,b_chronotype,
        a_spontaneity,b_spontaneity,
        a_express,b_express,
        a_edu,b_edu
    ] + a_love_encoded + b_love_encoded])

    probability = model.predict_proba(input_data)[0][1]

    st.markdown(f"## 💫 ความเข้ากันได้: {probability*100:.2f}%")

    if probability >= 0.7:
        st.balloons()
        st.success("💖 เคมีแรงมาก! นี่แฟนค่ะ 😍")
    elif probability >= 0.4:
        st.info("✨ มีลุ้นนะ 💕")
    else:
        st.snow()
        st.error("😭 ยังไม่ค่อยเข้ากัน แต่พัฒนาได้เสมอ")
