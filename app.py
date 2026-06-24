import streamlit as st
from openai import OpenAI

# Ambil API Key dari Streamlit Secrets

client = OpenAI(
api_key=st.secrets["OPENAI_API_KEY"]
)

st.set_page_config(page_title="AI CS ICONNET")

st.title("AI Customer Service ICONNET")

chat = st.text_area("Chat Pelanggan", height=200)

nama = st.text_input("Nama pelanggan (opsional)", "")

if st.button("Generate Balasan"):

```
if nama.strip() == "":
    sapaan = "Kak"
else:
    sapaan = f"Kak {nama.strip()}"

prompt = f"""
```

Anda adalah Customer Service ICONNET.

ATURAN:

* Gunakan sapaan "{sapaan}"
* Jangan gunakan Bapak/Ibu
* Gunakan bahasa sopan dan profesional
* Berikan empati terlebih dahulu
* Fokus pada solusi dan tindak lanjut
* Jangan membuat informasi yang tidak pasti

Chat pelanggan:
{chat}
"""

```
with st.spinner("Sedang membuat balasan..."):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

hasil = response.choices[0].message.content

st.text_area(
    "Balasan AI",
    hasil,
    height=250
)
