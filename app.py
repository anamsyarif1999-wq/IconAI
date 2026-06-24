import streamlit as st
import google.generativeai as genai

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
# CEK API KEY GEMINI
# =====================================
try:
    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    model = genai.GenerativeModel("gemini-1.5-flash")

except Exception as e:
    st.error(f"Gagal membaca GEMINI_API_KEY di Secrets: {e}")
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
    placeholder="Contoh: Anam"
)

# =====================================
# GENERATE BALASAN
# =====================================
if st.button("Generate Balasan"):

    if not chat.strip():
        st.warning("Silakan isi chat pelanggan terlebih dahulu.")
        st.stop()

    sapaan = "Kak" if not nama.strip() else f"Kak {nama.strip()}"

    prompt = f"""
Anda adalah Customer Service ICONNET.

ATURAN WAJIB:

- Gunakan sapaan "{sapaan}"
- Jangan menggunakan Bapak/Ibu
- Gunakan bahasa sopan dan profesional
- Berikan empati terlebih dahulu
- Fokus pada solusi dan tindak lanjut
- Jangan mengarang informasi
- Balasan singkat seperti agent customer service
- Gunakan bahasa Indonesia

Chat pelanggan:
{chat}
"""

    try:

        with st.spinner("Sedang membuat balasan..."):

            response = model.generate_content(prompt)

            hasil = response.text

        st.success("Balasan berhasil dibuat")

        st.text_area(
            "Balasan AI",
            value=hasil,
            height=250
        )

    except Exception as e:
        st.error(f"Terjadi error: {str(e)}")
