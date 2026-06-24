from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/v1"
)

st.title("AI Customer Service ICONNET")

chat = st.text_area("Chat Pelanggan", height=200)
nama = st.text_input("Nama pelanggan (opsional)", "")

if st.button("Generate Balasan"):

    sapaan = "Kak" if nama.strip() == "" else f"Kak {nama.strip()}"

    prompt = f"""
Anda adalah Customer Service ICONNET.

Gunakan sapaan {sapaan}.
Jawab sesuai SOP.
Sopan dan profesional.

Chat pelanggan:
{chat}
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )

    hasil = response.choices[0].message.content

    st.text_area("Balasan AI", hasil, height=250)
