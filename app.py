import streamlit as st
import joblib
import numpy as np

model = joblib.load("love_model.pkl")

st.title("💘 Love Compatibility Predictor")

a_age = st.number_input("อายุคุณ", 18, 60)
b_age = st.number_input("อายุคนที่คุณชอบ", 18, 60)

a_open = st.slider("Openness คุณ", 0.0, 1.0, 0.5)
b_open = st.slider("Openness เขา", 0.0, 1.0, 0.5)

a_extra = st.slider("Extraversion คุณ", 0.0, 1.0, 0.5)
b_extra = st.slider("Extraversion เขา", 0.0, 1.0, 0.5)

a_agree = st.slider("Agreeableness คุณ", 0.0, 1.0, 0.5)
b_agree = st.slider("Agreeableness เขา", 0.0, 1.0, 0.5)

a_con = st.slider("Conscientiousness คุณ", 0.0, 1.0, 0.5)
b_con = st.slider("Conscientiousness เขา", 0.0, 1.0, 0.5)

a_amb = st.slider("Career Ambition คุณ", 0.0, 1.0, 0.5)
b_amb = st.slider("Career Ambition เขา", 0.0, 1.0, 0.5)

a_edu = st.selectbox("การศึกษา คุณ", [1,2,3,4,5])
b_edu = st.selectbox("การศึกษา เขา", [1,2,3,4,5])

if st.button("ทำนาย ❤️"):
    data = np.array([[a_age,b_age,
                      a_open,b_open,
                      a_extra,b_extra,
                      a_agree,b_agree,
                      a_con,b_con,
                      a_amb,b_amb,
                      a_edu,b_edu]])
    
    prediction = model.predict(data)
    prob = model.predict_proba(data)
    
    if prediction[0] == 1:
        st.success(f"💖 เข้ากันได้! ({prob[0][1]*100:.2f}%)")
        st.balloons()
    else:
        st.error(f"💔 อาจจะยังไม่เข้ากัน ({prob[0][1]*100:.2f}%)")
