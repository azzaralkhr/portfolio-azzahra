import streamlit as st
import os
import base64

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Projects | Az Zahra", 
    page_icon="🚀", 
    layout="wide"
)

# Fungsi pemuatan gambar format Base64 agar menyatu sempurna dalam kartu HTML
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            ext = image_path.split('.')[-1].lower()
            mime_type = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"
            return f"data:{mime_type};base64,{encoded}"
    return None

# 2. Styling CSS Kustom Presisi
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
}

.stApp { 
    background-color: #F4F7FE !important; 
}

/* Trik khusus membuat tinggi kolom Streamlit otomatis sama (Equal Height) */
[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}

[data-testid="column"] {
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="column"] > div {
    height: 100% !important;
}

/* Hero Banner Atas */
.hero-container {
    background: linear-gradient(135deg, #EBF2FF 0%, #E6EEFE 100%);
    border-radius: 24px;
    padding: 32px 40px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid #DCE6F9;
    box-shadow: 0 4px 20px rgba(0,0,0,0.02);
}

.hero-left {
    display: flex;
    align-items: flex-start;
    gap: 20px;
}

.hero-pill-badge {
    background-color: #DBEAFE;
    color: #1D4ED8;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 20px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 12px;
}

.hero-icon-bg {
    width: 64px;
    height: 64px;
    background-color: #2563EB;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 30px;
    color: white;
    box-shadow: 0 8px 16px rgba(37, 99, 235, 0.2);
    flex-shrink: 0;
}

.hero-title {
    font-size: 35px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 8px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 30px !important;
    color: #64748B !important;
    font-weight: 500 !important;
    line-height: 1.5;
}

.hero-right-quote {
    font-size: 26px !important;
    font-weight: 800 !important;
    font-style: italic;
    color: #1E40AF !important;
    text-align: right;
    line-height: 1.3;
    max-width: 280px;
}

/* Card Proyek Main Container */
.project-card {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 30px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.03);
    margin-bottom: 24px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-sizing: border-box;
}

.card-title-group {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 16px;
}

.card-icon {
    width: 56px;
    height: 56px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 26px;
    flex-shrink: 0;
}

.icon-purple { background-color: #8B5CF6; }
.icon-green { background-color: #10B981; }

.card-main-title {
    font-size: 35px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 8px;
    line-height: 1.3;
}

/* Badges / Tech Stack Pill */
.tech-stack-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 16px;
}

.tech-badge {
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 18px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.badge-blue { background-color: #E0F2FE; color: #0369A1; }
.badge-purple { background-color: #F3E8FF; color: #6B21A8; }
.badge-green { background-color: #DCFCE7; color: #15803D; }
.badge-pink { background-color: #FCE7F3; color: #BE185D; }
.badge-orange { background-color: #FFEDD5; color: #C2410C; }

/* Status Jurnal / Publikasi */
.journal-info {
    font-size: 24px !important;
    color: #475569 !important;
    font-weight: 600 !important;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.project-desc {
    font-size: 25px !important;
    color: #334155 !important;
    line-height: 1.6;
    margin-bottom: 24px;
}

/* Tombol Akses Live */
.btn-live {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: #2563EB;
    color: #FFFFFF !important;
    padding: 12px 24px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: 700;
    text-decoration: none !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    transition: all 0.2s ease;
    width: fit-content;
}

.btn-live:hover {
    background-color: #1D4ED8;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
}

/* Kartu Pembungkus Gambar Kanan */
.image-card-container {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 16px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.03);
    margin-bottom: 24px;
    height: 100% !important;
    min-height: 100% !important;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    box-sizing: border-box;
}

.image-card-container img {
    border-radius: 16px;
    object-fit: cover;
    width: 100%;
    height: 100%;
    display: block;
}

.img-fallback-box {
    background: #F8FAFC;
    border: 2px dashed #CBD5E1;
    border-radius: 16px;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
}

.img-fallback-title {
    font-size: 18px;
    font-weight: 700;
    color: #334155;
    margin-top: 8px;
}

.img-fallback-desc {
    font-size: 14px;
    color: #94A3B8;
}
</style>
""", unsafe_allow_html=True)

# 3. Hero Banner Atas
st.markdown("""
<div class="hero-container">
    <div class="hero-left">
        <div class="hero-icon-bg">➕</div>
        <div>
            <div class="hero-pill-badge">Portofolio & Karya</div>
            <div class="hero-title">Proyek Unggulan & Hasil Karya</div>
            <div class="hero-subtitle">Berikut adalah beberapa proyek yang telah saya kerjakan selama perjalanan belajar dan pengembangan diri. Setiap proyek mencerminkan penerapan ilmu, kreativitas, dan semangat untuk terus berkembang.</div>
        </div>
    </div>
    <div class="hero-right-quote">
        Dari Ide<br>Menjadi<br>Karya Nyata
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Proyek 1: Sampedia
col1_t, col1_i = st.columns([2.2, 1], gap="medium")

with col1_t:
    st.markdown("""
<div class="project-card">
    <div>
        <div class="card-title-group">
            <div class="card-icon icon-purple">🖥️</div>
            <div>
                <div class="card-main-title">1. Sampedia – Klasifikasi & Edukasi Sampah (PCD)</div>
            </div>
        </div>
        <div class="tech-stack-wrapper">
            <span class="tech-badge badge-blue">⚙️ Python</span>
            <span class="tech-badge badge-purple">⚙️ OpenCV</span>
            <span class="tech-badge badge-green">⚙️ ResNet50</span>
            <span class="tech-badge badge-pink">⚙️ Streamlit</span>
            <span class="tech-badge badge-orange">⚙️ Bayesian Optimization</span>
        </div>
        <div class="journal-info">
            📄 Published on Jurnal Nasional Terakreditasi SINTA 4 (JINTEKS, 2026)
        </div>
        <div class="project-desc">
            Mengembangkan aplikasi berbasis Pengolahan Citra Digital (PCD) dan edukasi pengolahan sampah untuk mengklasifikasikan jenis sampah secara otomatis berdasarkan ekstraksi fitur citra gambar, mengolah dataset gambar sampah, menggunakan Python, OpenCV, dan Streamlit, guna menghasilkan platform edukasi interaktif yang memudahkan masyarakat memilah dan mengelola sampah secara tepat..
        </div>
    </div>
    <a href="https://sampedia.streamlit.app/" target="_blank" class="btn-live">
        🌐 Buka Aplikasi Sampedia Live ➔
    </a>
</div>
""", unsafe_allow_html=True)

with col1_i:
    img1_b64 = get_image_base64("project_sampedia.jpeg")
    if img1_b64:
        st.markdown(f"""
<div class="image-card-container">
    <img src="{img1_b64}" alt="Screenshot Sampedia">
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div class="image-card-container">
    <div class="img-fallback-box">
        <div style="font-size: 32px;">🖼️</div>
        <div class="img-fallback-title">[Screenshot Sampedia]</div>
        <div class="img-fallback-desc">Simpan gambar <code>project_sampedia.jpeg</code> di folder utama.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Proyek 2: Sistem Prediksi Performa Belajar Siswa
col2_t, col2_i = st.columns([2.2, 1], gap="medium")

with col2_t:
    st.markdown("""
<div class="project-card">
    <div>
        <div class="card-title-group">
            <div class="card-icon icon-green">🧠</div>
            <div>
                <div class="card-main-title">2. Sistem Prediksi Performa Belajar Siswa</div>
            </div>
        </div>
        <div class="tech-stack-wrapper">
            <span class="tech-badge badge-blue">⚙️ Python</span>
            <span class="tech-badge badge-purple">⚙️ Pandas</span>
            <span class="tech-badge badge-pink">⚙️ Streamlit</span>
            <span class="tech-badge badge-green">⚙️ Machine Learning</span>
        </div>
        <div class="journal-info">
            📄 Project uts dan uas Mesin Learning
        </div>
        <div class="project-desc">
            Mengembangkan aplikasi Machine Learning untuk memprediksi tingkat performa belajar siswa berdasarkan data demografis dan latar belakang akademis dari dataset Kaggle, mengolah dataset dengan beberapa variabel fitur pendukung, menggunakan Python, Neural Network (Keras/TensorFlow), dan Streamlit, guna menghasilkan model prediksi yang akurat serta antarmuka aplikasi interaktif yang dapat diakses pengguna secara real-time.
        </div>
    </div>
    <a href="https://uts-ml2-azzahraputri.streamlit.app/" target="_blank" class="btn-live">
        🌐 Buka Aplikasi Prediksi ML Live ➔
    </a>
</div>
""", unsafe_allow_html=True)

with col2_i:
    img2_b64 = get_image_base64("project_ml.jpeg")
    if img2_b64:
        st.markdown(f"""
<div class="image-card-container">
    <img src="{img2_b64}" alt="Screenshot Web ML">
</div>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<div class="image-card-container">
    <div class="img-fallback-box">
        <div style="font-size: 32px;">📊</div>
        <div class="img-fallback-title">[Screenshot Web ML]</div>
        <div class="img-fallback-desc">Simpan gambar <code>project_ml.jpg</code> di folder utama.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Footer
st.markdown("<br><hr style='border: 0.5px solid #E2E8F0;'><center style='color:#94A3B8; font-size: 16px !important;'>© 2026 Az Zahra Putri Al Khoiri. Crafted with ❤️ using Python & Streamlit.</center>", unsafe_allow_html=True)
