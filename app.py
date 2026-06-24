import streamlit as st
import google.generativeai as genai

# =========================
# CONFIG GEMINI
# =========================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-flash")

st.set_page_config(page_title="AI CS ICONNET")

st.title("AI Customer Service ICONNET")

chat = st.text_area("Chat Pelanggan", height=200)
nama = st.text_input("Nama pelanggan (opsional)", "")

if st.button("Generate Balasan"):

    if nama.strip() == "":
        sapaan = "Kak"
    else:
        sapaan = f"Kak {nama.strip()}"

    prompt = f"""
Anda adalah Customer Service ICONNET.

ATURAN:
- Gunakan sapaan "{sapaan}"
- Bahasa sopan dan profesional
- Berikan empati terlebih dahulu
- Fokus solusi
- Jangan mengarang informasi

Chat pelanggan:
{chat}
"""

    with st.spinner("Sedang membuat balasan..."):
        response = model.generate_content(prompt)
        hasil = response.text

    st.text_area("Balasan AI", hasil, height=250)
