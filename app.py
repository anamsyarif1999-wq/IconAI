import streamlit as st
from openai import OpenAI

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="AI Customer Service ICONNET",
    page_icon="💬",
    layout="centered"
)

st.title("💬 AI Customer Service ICONNET")

# =====================================
# CEK API KEY
# =====================================
try:
    client = OpenAI(
        api_key=st.secrets["DEEPSEEK_API_KEY"],
        base_url="https://api.deepseek.com"
    )
except Exception as e:
    st.error(f"Gagal membaca DEEPSEEK_API_KEY di Secrets: {e}")
    st.stop()

# =====================================
# INPUT
# =====================================
chat = st.text_area(
    "Chat Pelanggan",
    height=200,
    placeholder="Contoh: Internet saya link loss sejak pagi."
)

nama = st.text_input(
    "Nama pelanggan (opsional)",
    placeholder="Contoh: Budi"
)

# =====================================
# TOMBOL GENERATE
# =====================================
if st.button("Generate Balasan"):

    if not chat.strip():
        st.warning("Silakan isi chat pelanggan terlebih dahulu.")
        st.stop()

    sapaan = "Kak" if not nama.strip() else f"Kak {nama.strip()}"

    prompt = f"""
Anda adalah Customer Service ICONNET.

ATURAN:
- Gunakan sapaan "{sapaan}"
- Jangan menggunakan Bapak/Ibu.
- Gunakan bahasa Indonesia yang sopan dan profesional.
- Berikan empati terlebih dahulu.
- Fokus pada solusi dan tindak lanjut.
- Jangan mengarang informasi yang tidak diketahui.
- Buat balasan singkat seperti agent customer service.

Chat pelanggan:
{chat}
"""

    try:
        with st.spinner("Sedang membuat balasan..."):

            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {
                        "role": "system",
                        "content": "Anda adalah Customer Service ICONNET yang profesional."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.5,
                max_tokens=500
            )

            hasil = response.choices[0].message.content

        st.success("Balasan berhasil dibuat")

        st.text_area(
            "Balasan AI",
            value=hasil,
            height=250
        )

    except Exception as e:
        st.error(f"Terjadi error: {str(e)}")
