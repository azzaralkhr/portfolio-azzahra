import streamlit as st
import os
import base64

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Sertifikat | Az Zahra", 
    page_icon="📜", 
    layout="wide"
)

# Fungsi pemuatan gambar format Base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            ext = image_path.split('.')[-1].lower()
            mime_type = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"
            return f"data:{mime_type};base64,{encoded}"
    return None

# Fungsi pemuatan PDF format Base64 untuk link tautan tombol
def get_pdf_base64(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            encoded = base64.b64encode(pdf_file.read()).decode()
            return f"data:application/pdf;base64,{encoded}"
    return "#"

# 2. Styling CSS Kustom Presisi & Proporsional
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] { 
    font-family: 'Plus Jakarta Sans', sans-serif !important; 
}

.stApp { 
    background-color: #F4F7FE !important; 
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
    align-items: center;
    gap: 20px;
}

.hero-pill-badge {
    background-color: #DBEAFE;
    color: #1D4ED8;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 16px;
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
    font-size: 32px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 6px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 18px !important;
    color: #64748B !important;
    font-weight: 500 !important;
    line-height: 1.5;
}

.hero-right-quote {
    font-size: 24px !important;
    font-weight: 800 !important;
    font-style: italic;
    color: #1E40AF !important;
    text-align: right;
    line-height: 1.3;
    max-width: 280px;
}

/* Header Sub-Judul & Counter Badge */
.section-header-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}

.section-title {
    font-size: 26px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-subtitle {
    font-size: 16px;
    color: #64748B;
    margin-top: 4px;
}

.counter-badge {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 700;
    color: #1E293B;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}

/* Card Sertifikat Utama */
.cert-card {
    background: #FFFFFF;
    border-radius: 20px;
    padding: 24px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.02);
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 24px;
}

.cert-number {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    color: white;
    font-size: 18px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.num-blue { background-color: #3B82F6; }
.num-green { background-color: #10B981; }
.num-purple { background-color: #8B5CF6; }

/* Wadah Foto Sertifikat Dibuat Lebih Besar & Jelas */
.cert-img-box {
    width: 280px;
    min-width: 280px;
    height: 190px;
    border-radius: 14px;
    overflow: hidden;
    border: 2px dashed #CBD5E1;
    flex-shrink: 0;
    background-color: #F8FAFC;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
}

.cert-img-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 12px;
}

.cert-img-placeholder {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #64748B;
    text-align: center;
    padding: 12px;
}

.cert-content {
    flex: 1;
}

.cert-title {
    font-size: 24px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 6px;
}

.cert-validity {
    font-size: 16px;
    color: #64748B;
    font-weight: 600;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.cert-bullet-list {
    margin: 0;
    padding-left: 20px;
    font-size: 25px !important;
    color: #334155;
    line-height: 1.6;
}

.cert-bullet-list li {
    margin-bottom: 6px;
}

/* Sisi Kanan Kartu (Badge & Tombol) */
.cert-right-side {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: flex-end;
    min-width: 200px;
    height: 100%;
}

.category-tag {
    font-size: 20px;
    font-weight: 700;
    padding: 6px 14px;
    border-radius: 8px;
    margin-bottom: 10px;
    display: inline-block;
}

.tag-program { background-color: #EFF6FF; color: #2563EB; }
.tag-pelatihan { background-color: #ECFDF5; color: #059669; }
.tag-magang { background-color: #F3E8FF; color: #7C3AED; }

.skills-wrapper {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    justify-content: flex-end;
    margin-bottom: 20px;
}

.skill-pill {
    background-color: #F1F5F9;
    color: #475569;
    font-size: 17px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
}

.btn-cert-action {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: #2563EB;
    color: #FFFFFF !important;
    padding: 10px 20px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 700;
    text-decoration: none !important;
    box-shadow: 0 4px 10px rgba(37, 99, 235, 0.2);
    transition: all 0.2s ease;
}

.btn-cert-action:hover {
    background-color: #1D4ED8;
}

.btn-green-action {
    background-color: #059669;
    box-shadow: 0 4px 10px rgba(5, 150, 105, 0.2);
}
.btn-green-action:hover {
    background-color: #047857;
}

.btn-purple-action {
    background-color: #7C3AED;
    box-shadow: 0 4px 10px rgba(124, 58, 237, 0.2);
}
.btn-purple-action:hover {
    background-color: #6D28D9;
}
</style>
""", unsafe_allow_html=True)

# 3. Hero Banner Atas
st.markdown("""
<div class="hero-container">
    <div class="hero-left">
        <div class="hero-icon-bg">🏅</div>
        <div>
            <div class="hero-pill-badge">Dokumentasi Prestasi</div>
            <div class="hero-title">Sertifikat Resmi & Achievements</div>
            <div class="hero-subtitle">Kumpulan sertifikat yang telah Anda raih selama perjalanan belajar dan pengembangan diri di Az Zahra.</div>
        </div>
    </div>
    <div class="hero-right-quote">
        Terus Belajar,<br>Raih Lebih Banyak<br>Prestasi!
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Section Sub-Title & Counter
st.markdown("""
<div class="section-header-box">
    <div>
        <div class="section-title">📂 Daftar Sertifikat</div>
        <div class="section-subtitle">Berikut adalah sertifikat yang telah Anda peroleh selama mengikuti program dan kegiatan di Az Zahra.</div>
    </div>
    <div class="counter-badge">
        <span>🥇</span> 3 Sertifikat
    </div>
</div>
""", unsafe_allow_html=True)

# Pemuatan Gambar Masing-Masing Sertifikat
img1 = get_image_base64("sertifikat_dicoding.jpeg")
img2 = get_image_base64("sertifikat_pelatihan.jpeg")
img3 = get_image_base64("sertifikat_magang.jpeg")

# Pemuatan File PDF Masing-Masing Sertifikat
pdf1 = get_pdf_base64("sertifikat_1.pdf")
pdf2 = get_pdf_base64("sertifikat_2.pdf")
pdf3 = get_pdf_base64("sertifikat_3.pdf")

# Tag HTML untuk tempat foto
img_tag_1 = f'<img src="{img1}">' if img1 else '<div class="cert-img-placeholder"><span style="font-size:30px;">📷</span><b style="font-size:13px; margin-top:6px;">[Foto Sertifikat 1]</b><span style="font-size:11px;">sertifikat_dicoding.jpg</span></div>'
img_tag_2 = f'<img src="{img2}">' if img2 else '<div class="cert-img-placeholder"><span style="font-size:30px;">📷</span><b style="font-size:13px; margin-top:6px;">[Foto Sertifikat 2]</b><span style="font-size:11px;">sertifikat_pelatihan.jpg</span></div>'
img_tag_3 = f'<img src="{img3}">' if img3 else '<div class="cert-img-placeholder"><span style="font-size:30px;">📷</span><b style="font-size:13px; margin-top:6px;">[Foto Sertifikat 3]</b><span style="font-size:11px;">sertifikat_magang.jpg</span></div>'

# 5. Kartu Sertifikat 1 (Dicoding)
st.markdown(f"""
<div class="cert-card">
    <div class="cert-number num-blue">1</div>
    <div class="cert-img-box">
        {img_tag_1}
    </div>
    <div class="cert-content">
        <div class="cert-title">Sertifikat Memulai Pemrograman dengan Python</div>
        <div class="cert-validity">🗓️ Masa Berlaku: Sep 2026 – Sep 2029</div>
        <ul class="cert-bullet-list">
           Sertifikat kelulusan kelas Memulai Pemrograman dengan Python dari Dicoding Indonesia yang mencakup data, control flow, fungsi, hingga pengenalan library Python.
        </ul>
    </div>
    <div class="cert-right-side">
        <div style="text-align: right;">
            <span class="category-tag tag-program">📚 Program</span>
            <div class="skills-wrapper">
                <span class="skill-pill">Python</span>
            </div>
        </div>
        <a href="{pdf1}" target="_blank" download="sertifikat_python.pdf" class="btn-cert-action">👁️ Lihat Sertifikat ➔</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Kartu Sertifikat 2 (Pelatihan AI & Machine Learning)
st.markdown(f"""
<div class="cert-card">
    <div class="cert-number num-green">2</div>
    <div class="cert-img-box">
        {img_tag_2}
    </div>
    <div class="cert-content">
        <div class="cert-title">Sertifikat Belajar Dasar Structured Query Language (SQL)</div>
        <div class="cert-validity">🗓️ Masa Berlaku: Jul 2025 – Nov 2025</div>
        <ul class="cert-bullet-list">
            Sertifikat kelulusan kelas Belajar Dasar SQL dari Dicoding Indonesia yang mencakup konsep basis data relasional, DBMS, DDL, DML, serta eksekusi basic query.
        </ul>
    </div>
    <div class="cert-right-side">
        <div style="text-align: right;">
            <span class="category-tag tag-pelatihan">📚 Program</span>
            <div class="skills-wrapper">
                <span class="skill-pill">Structured Query Language (SQL)</span>
            </div>
        </div>
        <a href="{pdf2}" target="_blank" download="sertifikat_sql.pdf" class="btn-cert-action btn-green-action">👁️ Lihat Sertifikat ➔</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 7. Kartu Sertifikat 3 (Magang / Praktik Kerja)
st.markdown(f"""
<div class="cert-card">
    <div class="cert-number num-purple">3</div>
    <div class="cert-img-box">
        {img_tag_3}
    </div>
    <div class="cert-content">
        <div class="cert-title">Sertifikat Memulai Pemrograman Dengan C</div>
        <div class="cert-validity">🗓️ Masa Berlaku: Jan 2025 – Jun 2025</div>
        <ul class="cert-bullet-list">
            Sertifikat kelulusan kelas Memulai Pemrograman Dengan C dari Dicoding Indonesia yang mempelajari dasar logika pemrograman, variabel, fungsi, serta struktur data C..
        </ul>
    </div>
    <div class="cert-right-side">
        <div style="text-align: right;">
            <span class="category-tag tag-magang">📚 Program</span>
            <div class="skills-wrapper">
                <span class="skill-pill">Bahasa Pemrograman C</span>
            </div>
        </div>
        <a href="{pdf3}" target="_blank" download="sertifikat_c.pdf" class="btn-cert-action btn-purple-action">👁️ Lihat Sertifikat ➔</a>
    </div>
</div>
""", unsafe_allow_html=True)

# 8. Footer
st.markdown("<br><hr style='border: 0.5px solid #E2E8F0;'><center style='color:#94A3B8; font-size: 14px !important;'>© 2026 Az Zahra Putri Al Khoiri. Crafted with ❤️ using Python & Streamlit.</center>", unsafe_allow_html=True)
