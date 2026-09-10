import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Keahlian & Skill | Az Zahra", 
    page_icon="🛠️", 
    layout="wide"
)

# 2. Styling CSS Kustom (Diperbesar Ukuran Font & Element)
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
    gap: 24px;
}

.hero-icon-bg {
    width: 72px;
    height: 72px;
    background-color: #2563EB;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 36px;
    color: white;
    box-shadow: 0 8px 16px rgba(37, 99, 235, 0.2);
}

.hero-welcome {
    font-size: 16px !important;
    color: #64748B !important;
    font-weight: 600 !important;
    margin-bottom: 4px;
}

.hero-title {
    font-size: 36px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 6px;
}

.hero-subtitle {
    font-size: 16px !important;
    color: #475569 !important;
    font-weight: 500 !important;
}

.hero-right-badge {
    font-size: 22px !important;
    font-weight: 800 !important;
    font-style: italic;
    color: #2563EB !important;
    text-align: right;
    line-height: 1.3;
}

/* Card Utama */
.skill-card {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 36px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.03);
    min-height: 520px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.card-header-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 28px;
}

.card-title-group {
    display: flex;
    align-items: center;
    gap: 20px;
}

.card-icon-blue {
    width: 60px;
    height: 60px;
    background-color: #2563EB;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.card-icon-green {
    width: 60px;
    height: 60px;
    background-color: #10B981;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 26px;
}

.card-main-title {
    font-size: 26px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 4px;
}

.card-main-desc {
    font-size: 15px !important;
    color: #64748B !important;
    font-weight: 500 !important;
}

.cat-badge-blue {
    background-color: #EFF6FF !important;
    color: #2563EB !important;
    padding: 8px 18px !important;
    border-radius: 14px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

.cat-badge-green {
    background-color: #ECFDF5 !important;
    color: #059669 !important;
    padding: 8px 18px !important;
    border-radius: 14px !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

/* Pill/Badge Grid Layout */
.pill-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 24px;
}

.skill-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 22px !important;
    border-radius: 9999px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    transition: all 0.2s ease;
}

.skill-pill:hover {
    transform: translateY(-2px);
}

/* Variasi Warna Pill Hard Skill */
.pill-blue-light { background-color: #EBF3FF; color: #1D4ED8; }
.pill-cyan { background-color: #E0F2FE; color: #0284C7; }
.pill-purple { background-color: #F3E8FF; color: #7E22CE; }
.pill-pink { background-color: #FCE7F3; color: #BE185D; }
.pill-green-light { background-color: #DCFCE7; color: #15803D; }
.pill-emerald { background-color: #D1FAE5; color: #047857; }
.pill-orange { background-color: #FFEDD5; color: #C2410C; }
.pill-amber { background-color: #FEF3C7; color: #B45309; }
.pill-sky { background-color: #E0F2FE; color: #0369A1; }
.pill-fuchsia { background-color: #FAE8FF; color: #A21CAF; }

/* Variasi Warna Pill Soft Skill */
.pill-soft-green { background-color: #D1FAE5; color: #047857; }
.pill-soft-blue { background-color: #DBEAFE; color: #1D4ED8; }
.pill-soft-purple { background-color: #F3E8FF; color: #6B21A8; }
.pill-soft-yellow { background-color: #FEF3C7; color: #D97706; }

/* Quote Box di Bawah Soft Skill */
.quote-box {
    background: #F8FAFC;
    border-radius: 16px;
    padding: 20px 28px;
    border-left: 5px solid #10B981;
    font-size: 15px !important;
    color: #475569 !important;
    font-style: italic;
    line-height: 1.6;
    margin-top: auto;
}
</style>
""", unsafe_allow_html=True)

# 3. Hero Banner Atas
st.markdown("""<div class="hero-container"><div class="hero-left"><div class="hero-icon-bg">💡</div><div><div class="hero-welcome">Selamat Datang di Halaman</div><div class="hero-title">Keahlian & Skill</div><div class="hero-subtitle">Berikut adalah daftar keahlian dan keterampilan yang saya miliki sebagai bekal untuk masa depan.</div></div></div><div class="hero-right-badge">Skills Today<br><span style="color:#0F172A; font-weight:400;">Better Tomorrow</span></div></div>""", unsafe_allow_html=True)

# 4. Layout Main (Hard Skills & Soft Skills)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""<div class="skill-card"><div><div class="card-header-wrapper"><div class="card-title-group"><div class="card-icon-blue">&lt;/&gt;</div><div><div class="card-main-title">Hard Skills</div><div class="card-main-desc">Keterampilan atau pengetahuan khusus yang dibutuhkan untuk sebuah pekerjaan</div></div></div><div class="cat-badge-blue">🖥️ Teknis</div></div><div class="pill-grid"><div class="skill-pill pill-blue-light">🐍 Pemrograman Python</div><div class="skill-pill pill-cyan">🗄️ Data Processing</div><div class="skill-pill pill-purple">📈 Data Analyst</div><div class="skill-pill pill-pink">📊 Data Analysis</div><div class="skill-pill pill-fuchsia">🖼️ Image Processing</div><div class="skill-pill pill-green-light">📋 Rekapitulasi Data</div><div class="skill-pill pill-emerald">✳️ Microsoft Excel</div><div class="skill-pill pill-orange">📙 Microsoft Office</div><div class="skill-pill pill-sky">🗃️ SQL</div><div class="skill-pill pill-amber">🎨 HTML & CSS</div><div class="skill-pill pill-purple">🐘 PHP (CodeIgniter)</div><div class="skill-pill pill-emerald">🌐 Jaringan Dasar (LAN/IP)</div></div></div></div>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="skill-card"><div><div class="card-header-wrapper"><div class="card-title-group"><div class="card-icon-green">👥</div><div><div class="card-main-title">Soft Skills</div><div class="card-main-desc">Kemampuan Interpersonal & Manajerial</div></div></div><div class="cat-badge-green">👤 Non-Teknis</div></div><div class="pill-grid"><div class="skill-pill pill-soft-green">💬 Communication Skills</div><div class="skill-pill pill-soft-blue">🔄 Adaptability / Adaptabilitas</div><div class="skill-pill pill-soft-purple">👥 Kerja Sama Tim / Teamwork</div><div class="skill-pill pill-soft-yellow">💡 Problem Solving</div><div class="skill-pill pill-soft-blue">🕒 Manajemen Waktu</div><div class="skill-pill pill-soft-purple">👤 Kepemimpinan (Leadership)</div></div></div><div class="quote-box">“Keterampilan teknis membuka peluang, namun soft skill yang membuat kita bertahan dan berkembang.”</div></div>""", unsafe_allow_html=True)

# 5. Footer
st.markdown("<br><hr style='border: 0.5px solid #E2E8F0;'><center style='color:#94A3B8; font-size: 15px !important;'>© 2026 Az Zahra Putri Al Khoiri. Crafted with ❤️ using Python & Streamlit.</center>", unsafe_allow_html=True)
