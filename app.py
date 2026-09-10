import streamlit as st
import os
import base64

# ---------------------------------------------------------
# 1. KONFIGURASI HALAMAN
# ---------------------------------------------------------
st.set_page_config(
    page_title="Portofolio | Az Zahra Putri Al Khoiri",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function konversi gambar lokal ke base64 untuk CSS
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

bg_base64 = get_base64_image("Khia Avery.jpg")
profile_base64 = get_base64_image("foto_profil.png")

bg_css = f"data:image/jpeg;base64,{bg_base64}" if bg_base64 else ""
profile_src = f"data:image/png;base64,{profile_base64}" if profile_base64 else ""

# ---------------------------------------------------------
# 2. STYLING CSS KUSTOM GLOBAL & NAVBAR KAPSUL BIRU MUDA
# ---------------------------------------------------------
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    .stApp {{
        background-color: #F8FAFC !important;
    }}

    /* HAPUS SIDEBAR STREAMLIT TOTAL */
    [data-testid="stSidebar"], section[data-testid="stSidebar"], [data-testid="collapsedControl"] {{
        display: none !important;
    }}

    /* CONTAINER NAVBAR KAPSUL UTAMA - PERBAIKAN UKURAN HEADER */
    .capsule-navbar {{
        background-color: #38BDF8; /* Warna background biru muda */
        border-radius: 50px;
        padding: 12px 24px;
        margin: 10px auto 35px auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
        max-width: 100%;
        box-shadow: 0 8px 20px rgba(56, 189, 248, 0.25);
    }}

    /* ITEM LINK NAVIGASI IN-LINE - UKURAN TULISAN DIPERBESAR */
    .nav-item {{
        color: #FFFFFF !important;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 17px;
        padding: 10px 24px;
        border-radius: 30px;
        transition: all 0.25s ease;
        display: inline-block;
        white-space: nowrap;
    }}

    .nav-item:hover {{
        background-color: rgba(255, 255, 255, 0.25);
        color: #FFFFFF !important;
    }}

    /* TAMPILAN AKTIF TOMBOL HOME */
    .nav-item.active {{
        background-color: #FFFFFF !important;
        color: #0284C7 !important;
        font-weight: 700;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    }}

    /* LOGO DI TENGAH NAVBAR - DIPERBESAR */
    .navbar-logo {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 800;
        font-size: 20px;
        color: #FFFFFF;
        padding: 6px 16px;
        letter-spacing: 0.5px;
    }}

    /* About Hero Card */
    .about-hero-card {{
        background: url('{bg_css}') no-repeat center center;
        background-size: cover;
        padding: 40px 50px;
        border-radius: 24px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.08);
        margin-top: 10px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        gap: 40px;
        position: relative;
        overflow: hidden;
    }}

    .hero-left-content {{ flex: 1.8; z-index: 2; }}
    .hero-right-content {{ flex: 1; display: flex; justify-content: center; align-items: center; z-index: 2; }}

    .profile-img-styled {{
        width: 100%;
        max-width: 250px;
        height: auto;
        object-fit: contain;
        filter: drop-shadow(0px 8px 16px rgba(0, 0, 0, 0.15));
    }}

    .hero-badge {{
        background: #1E3A2B;
        color: #F3F4F6;
        padding: 8px 18px;
        border-radius: 50px;
        font-size: 25px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 16px;
    }}
    
    .hero-title {{
        font-size: 60px;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.2;
        margin-bottom: 10px;
    }}
    
    .hero-subtitle {{
        font-size: 30px;
        font-weight: 700;
        color: #D97706;
        margin-bottom: 20px;
    }}
    
    .hero-desc {{
        font-size: 30px;
        color: #1E293B;
        font-weight: 450;
        line-height: 1.7;
        margin-bottom: 24px;
    }}

    .social-btn {{
        display: inline-block;
        padding: 20px 30px;
        margin-right: 15px;
        margin-bottom: 15px;
        border-radius: 15px;
        font-weight: 700;
        font-size: 20px;
        text-decoration: none !important;
    }}
    .btn-linkedin {{ background-color: #0A66C2; color: white !important; }}
    .btn-github {{ background-color: #181717; color: white !important; }}
    .btn-instagram {{ background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%); color: white !important; }}
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. HEADER NAVIGASI KAPSUL (Tautan Navigasi Diperbaiki)
# ---------------------------------------------------------
st.markdown("""
<div class="capsule-navbar">
    <a href="./" target="_self" class="nav-item active">Home</a>
    <a href="./Education" target="_self" class="nav-item">Education</a>
    <a href="./Technical_Skills" target="_self" class="nav-item">Skills</a>
    <div class="navbar-logo">✨ AZ ZAHRA</div>
    <a href="./Experience" target="_self" class="nav-item">Experience</a>
    <a href="./Project2" target="_self" class="nav-item">Projects</a>
    <a href="./Sertifikat" target="_self" class="nav-item">Certificates</a>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. KONTEN UTAMA (HOME / ABOUT ME)
# ---------------------------------------------------------
if profile_src:
    profile_html = f'<img src="{profile_src}" class="profile-img-styled" alt="Foto Profil">'
else:
    profile_html = '<div style="background:#E2E8F0; padding:20px; border-radius:12px; text-align:center;">📷 [Foto Profil]</div>'

st.markdown(f"""
<div class="about-hero-card">
    <div class="hero-left-content">
        <div class="hero-badge">🎓 Graduated with Honors — IPK 3.85 / 4.00</div>
        <div class="hero-title">Az Zahra Putri Al Khoiri, S.Kom.</div>
        <div class="hero-subtitle">IT Support, Data Analyst & Administrasi Support</div>
        <div class="hero-desc">
            Fresh Graduate S1 Teknik Informatika dari STT Wastukancana yang meraih predikat Pujian (IPK 3,85). Berfokus pada bidang analisis data, IT support, dan administrative support. Memiliki pengalaman kerja dan organisasi sebagai Asisten Dosen dalam penginputan dan rekapitulasi data akademik, Guru Teknik Informatika selama empat bulan, fasilitator kegiatan GTS (Goes to School) yang mendampingi peserta saat praktik, serta aktif dalam kepanitiaan organisasi Humanika pada divisi acara. Selain itu, berpengalaman mengembangkan proyek machine learning untuk deteksi performa belajar siswa serta pengolahan citra digital untuk klasifikasi sampah organik dan anorganik, mulai dari tahap business understanding untuk memetakan masalah, data understanding dan data preparation melalui pembersihan data, modeling, evaluasi hingga tahap deployment yang diimplementasikan menggunakan website Streamlit. Terampil dalam pengolahan data, administrasi, penggunaan Microsoft Office terutama Microsoft Excel, serta pemrograman Python. Saya merupakan pribadi yang adaptif, teliti, bertanggung jawab, dan memiliki komunikasi yang baik untuk bekerja secara mandiri maupun berkolaborasi dalam tim, dan siap berkembang melalui kesempatan magang ini untuk meningkatkan kompetensi profesional. 
        </div>
        <div style="font-weight:700; color:#0F172A; margin-bottom:12px; font-size:16px;">🔗 Let's Connect</div>
        <div>
            <a href="https://www.linkedin.com/in/az-zahra-putri-al-khoiri-9ab264385/" target="_blank" class="social-btn btn-linkedin">👔 LinkedIn</a>
            <a href="https://github.com/azzaralkhr" target="_blank" class="social-btn btn-github">💻 GitHub</a>
            <a href="https://instagram.com/" target="_blank" class="social-btn btn-instagram">📸 Instagram</a>
        </div>
    </div>
    <div class="hero-right-content">
        {profile_html}
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. FOOTER
# ---------------------------------------------------------
st.markdown("<br><hr style='border: 0.5px solid #E2E8F0;'><center style='color:#94A3B8; font-size: 13px;'>© 2026 Az Zahra Putri Al Khoiri. Crafted with Python & Streamlit.</center>", unsafe_allow_html=True)
