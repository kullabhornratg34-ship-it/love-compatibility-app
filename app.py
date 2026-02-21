import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Love Matcher", page_icon="💘", layout="centered")

# ===== CSS ธีมชมพู + ตัวหนังสือสีดำทั้งหมด =====
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;500;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Kanit', sans-serif;
        color: black !important;
    }

    /* พื้นหลังชมพู */
    .stApp {
        background-color: #ffd6e8;
    }

    /* กล่องด้านในสีขาว */
    .block-container {
        background-color: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    }

    /* บังคับตัวหนังสือทุกตัวให้ดำ */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: black !important;
    }

    /* ปุ่ม */
    .stButton>button {
        background-color: #ff4b91;
        color: white !important;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #ff1f75;
        color: white !important;
    }

    /* กล่องแจ้งเตือน */
    div[data-baseweb="notification"],
    div.stAlert {
        background-color: #ffe6f2 !important;
        color: black !important;
    }

    div[data-baseweb="notification"] *,
    div.stAlert * {
        color: black !important;
    }

    </style>
""", unsafe_allow_html=True)

# โหลดโมเดล
model = joblib.load("love_model.pkl")

st.markdown("<h1>💘 LOVE COMPATIBILITY MATCHER 💘</h1>", unsafe_allow_html=True)
st.markdown("## 👩‍❤️‍👨 กรอกข้อมูลของคุณและคนที่คุณชอบ")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🌸 คุณ")
    a_age = st.number_input("อายุของคุณ", 18, 60, 22)
    a_openness = st.slider("เปิดรับประสบการณ์ใหม่", 0.0, 1.0, 0.5)
    a_extraversion = st.slider("ความเป็นคนเปิดเผย", 0.0, 1.0, 0.5)
    a_agreeableness = st.slider("ความเป็นมิตร", 0.0, 1.0, 0.5)
    a_conscientiousness = st.slider("ความมีวินัย", 0.0, 1.0, 0.5)
    a_career = st.slider("ความทะเยอทะยานด้านอาชีพ", 0.0, 1.0, 0.5)
    a_edu = st.selectbox("ระดับการศึกษา", [1,2,3,4])

with col2:
    st.markdown("### 💖 คนที่คุณชอบ")
    b_age = st.number_input("อายุของเขา", 18, 60, 22)
    b_openness = st.slider("เปิดรับประสบการณ์ใหม่ ", 0.0, 1.0, 0.5)
    b_extraversion = st.slider("ความเป็นคนเปิดเผย ", 0.0, 1.0, 0.5)
    b_agreeableness = st.slider("ความเป็นมิตร ", 0.0, 1.0, 0.5)
    b_conscientiousness = st.slider("ความมีวินัย ", 0.0, 1.0, 0.5)
    b_career = st.slider("ความทะเยอทะยานด้านอาชีพ ", 0.0, 1.0, 0.5)
    b_edu = st.selectbox("ระดับการศึกษา ", [1,2,3,4])

st.markdown("---")

if st.button("💘 วิเคราะห์ความรักเลยยย"):
    input_data = np.array([[a_age,b_age,
                            a_openness,b_openness,
                            a_extraversion,b_extraversion,
                            a_agreeableness,b_agreeableness,
                            a_conscientiousness,b_conscientiousness,
                            a_career,b_career,
                            a_edu,b_edu]])
    
    probability = model.predict_proba(input_data)[0][1]

    st.markdown(f"## 💫 ความเข้ากันได้: {probability*100:.2f}%")

    if probability >= 0.7:
        st.balloons()
        st.success("💖 เคมีแรงมาก! นี่แฟนค่ะ ไม่ใช่เพื่อนแล้ว 😍")
    elif probability >= 0.4:
        st.info("✨ มีลุ้นนะ แต่ต้องปรับตัวกันอีกนิด 💕")
    else:
        st.snow()
        st.error("😭 ยังไม่ค่อยเข้ากัน แต่ความรักพัฒนาได้เสมอ")
