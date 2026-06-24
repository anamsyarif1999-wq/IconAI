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
# KONEKSI GEMINI
# =====================================

try:
    genai.configure(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    # Model Gemini terbaru
    model = genai.GenerativeModel("gemini-2.0-flash")

except Exception as e:
    st.error(f"Gagal membaca API Key Gemini: {e}")
    st.stop()

# =====================================
# INPUT
# =====================================

nama = st.text_input(
    "Nama Pelanggan (Opsional)",
    placeholder="Contoh: Anam"
)

chat = st.text_area(
    "Chat Pelanggan",
    height=200,
    placeholder="Paste chat pelanggan di sini..."
)

# =====================================
# GENERATE
# =====================================

if st.button("Generate Balasan"):

    if not chat.strip():
        st.warning("Silakan isi chat pelanggan terlebih dahulu.")
        st.stop()

    sapaan = "Kak"

    if nama.strip():
        sapaan = f"Kak {nama.strip()}"

    prompt = f"""
Anda adalah Customer Service ICONNET.

ATURAN WAJIB:

1. Gunakan sapaan "{sapaan}"
2. Jangan gunakan Bapak/Ibu.
3. Gunakan bahasa Indonesia yang sopan.
4. Berikan empati terlebih dahulu.
5. Fokus pada solusi.
6. Jangan mengarang informasi yang tidak ada.
7. Balasan singkat dan profesional.
8. Gaya bahasa customer service ICONNET.
9. Jika pelanggan marah tetap tenang dan profesional.

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

        st.error(str(e))
