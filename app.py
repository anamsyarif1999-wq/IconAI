import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="ISI_API_KEY_OPENAI_KAMU"
)

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

Gunakan sapaan {sapaan}.
Jawab sesuai SOP.
Bahasa sopan dan profesional.

Chat pelanggan:
{chat}
"""

    client = OpenAI(api_key="sk-xxxxxxxxxxxxxxxx")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    hasil = response.choices[0].message.content

    st.text_area("Hasil", hasil, height=250)