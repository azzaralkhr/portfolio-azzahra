import streamlit as st
import os
import base64

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Experience | Az Zahra", 
    page_icon="💼", 
    layout="wide"
)

# Fungsi untuk memuat gambar dalam format Base64 agar menyatu dalam HTML
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            ext = image_path.split('.')[-1].lower()
            mime_type = "image/jpeg" if ext in ["jpg", "jpeg"] else f"image/{ext}"
            return f"data:{mime_type};base64,{encoded}"
    return None

# 2. Styling CSS Kustom
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
    font-size: 34px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 6px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 23px !important;
    color: #64748B !important;
    font-weight: 500 !important;
}

.hero-right-quote {
    font-size: 18px !important;
    font-weight: 700 !important;
    font-style: italic;
    color: #334155 !important;
    text-align: right;
    line-height: 1.4;
    max-width: 250px;
}

/* Card Pengalaman */
.exp-card {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 30px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.03);
    margin-bottom: 24px;
    height: 100%;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
}

.card-header-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 16px;
}

.card-title-group {
    display: flex;
    align-items: flex-start;
    gap: 16px;
}

.card-icon {
    width: 52px;
    height: 52px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 24px;
    flex-shrink: 0;
}

.icon-purple { background-color: #8B5CF6; }
.icon-green { background-color: #10B981; }
.icon-pink { background-color: #F43F5E; }

.card-main-title {
    font-size: 35px !important;
    font-weight: 800 !important;
    color: #0F172A !important;
    margin-bottom: 4px;
}

.card-sub-info {
    font-size: 25px !important;
    color: #64748B !important;
    font-weight: 600 !important;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Tag Badge Kategori */
.tag-badge {
    padding: 6px 16px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.tag-purple { background-color: #F3E8FF; color: #7E22CE; }
.tag-green { background-color: #ECFDF5; color: #047857; }
.tag-pink { background-color: #FFE4E6; color: #BE123C; }

/* List Poin Deskripsi (Diperbesar) */
.exp-list {
    margin: 0;
    padding-left: 20px;
    color: #334155;
    font-size: 30px !important;
    line-height: 1.7;
}

.exp-list li {
    margin-bottom: 8px;
}

/* Kartu Pembungkus Foto Sejajar - Disesuaikan agar fleksibel memanjang ke bawah */
.image-card-container {
    background: #FFFFFF;
    border-radius: 24px;
    padding: 16px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.03);
    margin-bottom: 24px;
    height: 100%;
    min-height: 250px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    box-sizing: border-box;
}

.image-card-container img {
    border-radius: 16px;
    object-fit: contain;
    width: 100%;
    max-height: 100%;
    display: block;
}

/* Fallback Tampilan Foto Tidak Ditemukan */
.img-fallback-box {
    background: #F8FAFC;
    border: 2px dashed #CBD5E1;
    border-radius: 16px;
    width: 100%;
    height: 100%;
    min-height: 200px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
    box-sizing: border-box;
}

.img-fallback-title {
    font-size: 16px;
    font-weight: 700;
    color: #334155;
    margin-top: 8px;
}

.img-fallback-desc {
    font-size: 13px;
    color: #94A3B8;
}
</style>
""", unsafe_allow_html=True)

# 3. Hero Banner Atas
st.markdown("""
<div class="hero-container">
    <div class="hero-left">
        <div class="hero-icon-bg">💼</div>
        <div>
            <div class="hero-pill-badge">💼 Pengalaman Kerja & Kegiatan</div>
            <div class="hero-title">Riwayat Kerja & Pengalaman</div>
            <div class="hero-subtitle">Berikut adalah rangkuman pengalaman kerja, kegiatan, dan proyek yang pernah saya ikuti selama masa perkuliahan dan profesional.</div>
        </div>
    </div>
    <div class="hero-right-quote">
        “Setiap pengalaman adalah langkah menuju kesuksesan!”
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Item 1: Panitia divisi Seksi Acara
col1_t, col1_i = st.columns([2.2, 1], gap="medium")

with col1_t:
    st.markdown("""
    <div class="exp-card">
        <div class="card-header-wrapper">
            <div class="card-title-group">
                <div class="card-icon icon-purple">🧠</div>
                <div>
                    <div class="card-main-title">Panitia divisi Seksi Acara</div>
                    <div class="card-sub-info">🏛️ Humanika STT Wastukancana &nbsp;|&nbsp; Feb 2025 – Maret 2025</div>
                </div>
            </div>
             <div class="tag-badge tag-pink">🚩 Kegiatan</div>
        </div>
        <ul class="exp-list">
            Mengatur alur teknis dan rundown untuk kelancaran kegiatan Masa Bimbingan, mencakup koordinasi lapangan bagi 100+ peserta, pengisi acara, serta panitia lintas divisi. Tugas ini meliputi pengelolaan anggaran operasional acara menggunakan Microsoft Word dan Microsoft Excel guna memastikan seluruh rangkaian kegiatan berjalan tepat waktu, efisien, dan transparan.
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col1_i:
    img1_b64 = get_image_base64("seksiacara.jpeg")
    if img1_b64:
        st.markdown(f"""
        <div class="image-card-container">
            <img src="{img1_b64}" alt="Seksi Acara">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="image-card-container">
            <div class="img-fallback-box">
                <div style="font-size: 32px;">🖼️</div>
                <div class="img-fallback-title">Foto Skripsi</div>
                <div class="img-fallback-desc">Simpan gambar <code>seksiacara.jpeg</code> di folder utama.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 5. Item 2: Guru Teknik Informatika
col2_t, col2_i = st.columns([2.2, 1], gap="medium")

with col2_t:
    st.markdown("""
    <div class="exp-card">
        <div class="card-header-wrapper">
            <div class="card-title-group">
                <div class="card-icon icon-green">&lt;/&gt;</div>
                <div>
                    <div class="card-main-title">Guru Teknik Informatika</div>
                    <div class="card-sub-info">🏛️ SMP 2 Fullday Al Muhajirin &nbsp;|&nbsp; Jul 2025 – Nov 2025</div>
                </div>
            </div>
            <div class="tag-badge tag-green">🧰 Pekerjaan</div>
        </div>
        <ul class="exp-list">
Menyusun materi serta mengajar mata pelajaran Teknik Informatika dan kelas ICT untuk 7 kelas siswa SMP kelas 8, mencakup pembelajaran pemrograman dasar dan pengelolaan rekapitulasi nilai/kehadiran siswa, menggunakan HTML, CSS, Python, dan Microsoft Excel, guna memastikan proses belajar berjalan terstruktur, akurat, dan seluruh siswa menguasai praktik dasar pemrograman.
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2_i:
    img2_b64 = get_image_base64("exp_mengajar.jpeg")
    if img2_b64:
        st.markdown(f"""
        <div class="image-card-container">
            <img src="{img2_b64}" alt="Foto Mengajar">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="image-card-container">
            <div class="img-fallback-box">
                <div style="font-size: 32px;">👨‍🏫</div>
                <div class="img-fallback-title">Foto Mengajar</div>
                <div class="img-fallback-desc">Simpan gambar <code>exp_mengajar.jpeg</code> di folder utama.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 6. Item 3: Fasilitator Kegiatan GTS
col3_t, col3_i = st.columns([2.2, 1], gap="medium")

with col3_t:
    st.markdown("""
    <div class="exp-card">
        <div class="card-header-wrapper">
            <div class="card-title-group">
                <div class="card-icon icon-pink">👥</div>
                <div>
                    <div class="card-main-title">Fasilitator Kegiatan GTS (Goes to School)</div>
                    <div class="card-sub-info">🏛️ Panitia GTS STT Wastukancana &nbsp;|&nbsp; Mar 2025</div>
                </div>
            </div>
            <div class="tag-badge tag-pink">🚩 Kegiatan</div>
        </div>
        <ul class="exp-list">
           Membimbing dan mendampingi 30 peserta secara langsung dalam sesi praktik program GTS (Goes to School), mencakup bimbingan alur materi serta troubleshooting teknis dasar menggunakan PHP dan Framework CodeIgniter (CI), guna memastikan seluruh peserta mampu menyelesaikan modul pembelajaran dengan lancar, efektif, dan paham alur praktiknya.
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3_i:
    img3_b64 = get_image_base64("exp_gts.jpeg")
    if img3_b64:
        st.markdown(f"""
        <div class="image-card-container">
            <img src="{img3_b64}" alt="Foto GTS">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="image-card-container">
            <div class="img-fallback-box">
                <div style="font-size: 32px;">👥</div>
                <div class="img-fallback-title">Foto Fasilitator GTS</div>
                <div class="img-fallback-desc">Simpan gambar <code>exp_gts.jpg</code> di folder utama.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 7. Footer
st.markdown("<br><hr style='border: 0.5px solid #E2E8F0;'><center style='color:#94A3B8; font-size: 15px !important;'>© 2026 Az Zahra Putri Al Khoiri. Crafted with ❤️ using Python & Streamlit.</center>", unsafe_allow_html=True)
