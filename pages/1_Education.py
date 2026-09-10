import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Riwayat Pendidikan | Az Zahra",
    page_icon="🎓",
    layout="wide"
)

# 2. Styling CSS Kustom (Ukuran Font Diperbesar & Paksa !important)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .stApp {
        background-color: #F3F6FC;
    }

    /* Container Header Pendidikan */
    .edu-hero-card {
        background: linear-gradient(135deg, #EBF3FF 0%, #E0ECFF 100%);
        border: 2px solid #D0E1FD;
        border-radius: 20px;
        padding: 32px 40px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.08);
    }

    .edu-hero-left {
        display: flex;
        align-items: center;
        gap: 24px;
    }

    .edu-icon-bg {
        width: 80px;
        height: 80px;
        background-color: #2563EB;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 40px !important;
        color: white;
        box-shadow: 0 8px 16px rgba(37, 99, 235, 0.25);
    }

    .edu-title-main {
        font-size: 45px !important;
        font-weight: 800 !important;
        color: #1E293B !important;
        margin-bottom: 6px;
    }

    .edu-subtitle-main {
        font-size: 30px !important;
        font-weight: 700 !important;
        color: #2563EB !important;
        margin-bottom: 6px;
    }

    .edu-location-text {
        font-size: 18px !important;
        color: #475569 !important;
        font-weight: 500 !important;
    }

    .edu-hero-right {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 20px 28px;
        border: 1px solid #CBD5E1;
        text-align: right;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }

    .ipk-label {
        font-size: 16px !important;
        color: #64748B !important;
        font-weight: 700 !important;
    }

    .ipk-value {
        font-size: 40px !important;
        font-weight: 800 !important;
        color: #1E293B !important;
        line-height: 1.1;
    }

    .ipk-sub {
        font-size: 15px !important;
        color: #64748B !important;
        margin-top: 4px;
        font-weight: 600 !important;
    }

    /* Deskripsi Paragraf Card */
    .desc-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 32px 36px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        margin-bottom: 32px;
    }

    .desc-text {
        font-size: 25px !important; /* Ukuran paragraf diperbesar */
        line-height: 1.8 !important;
        color: #1E293B !important;
        margin-bottom: 18px !important;
    }

    /* Section Title */
    .section-title-box {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 20px;
    }

    .section-icon {
        width: 52px;
        height: 52px;
        background-color: #2563EB;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 26px !important;
    }

    .section-title {
        font-size: 30px !important;
        font-weight: 800 !important;
        color: #0F172A !important;
    }

    /* Grid Layout untuk Kegiatan Sosial */
    .org-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 24px;
        margin-bottom: 32px;
    }

    .org-card-item {
        background: #FFFFFF;
        border: 1.5px solid #E2E8F0;
        border-radius: 18px;
        padding: 26px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        transition: all 0.2s ease;
    }

    .org-card-item:hover {
        border-color: #2563EB;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.1);
    }

    .org-card-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 14px;
    }

    .org-card-icon {
        width: 48px;
        height: 48px;
        background-color: #EFF6FF;
        color: #2563EB;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px !important;
        flex-shrink: 0;
    }

    .org-title {
        font-size: 30px !important; /* Judul Kegiatan */
        font-weight: 800 !important;
        color: #0F172A !important;
        line-height: 1.3;
    }

    .org-sub-title {
        color: #2563EB !important;
        font-weight: 700 !important;
        font-size: 20px !important; /* Subtitle Divisi */
    }

    .org-list {
        margin: 0;
        padding-left: 20px;
    }

    /* Teks Poin-Poin di Dalam Kartu */
    .org-list li {
        font-size: 25px !important; /* Ukuran teks poin diperbesar */
        line-height: 1.7 !important;
        color: #334155 !important;
        margin-bottom: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header Pendidikan
st.markdown("""
<div class="edu-hero-card">
    <div class="edu-hero-left">
        <div class="edu-icon-bg">🎓</div>
        <div>
            <div class="edu-title-main">Riwayat Pendidikan</div>
            <div class="edu-title-main" style="font-size:26px !important; color:#1E293B;">STT Wastukancana</div>
            <div class="edu-subtitle-main">S1 - Teknik Informatika</div>
            <div class="edu-location-text">📍 Mulyamekar, Babakancikao, Kab. Purwakarta, Jawa Barat (Dalam Negeri)</div>
        </div>
    </div>
    <div class="edu-hero-right">
        <div class="ipk-label">IPK Terakhir</div>
        <div class="ipk-value">3,85</div>
        <div class="ipk-sub">Masa Studi 2022 - 2026</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Paragraf Deskripsi
st.markdown("""
<div class="desc-card">
    <p class="desc-text">
        Selama masa kuliah, saya aktif terlibat dalam berbagai kegiatan akademik, organisasi, dan pengabdian yang melatih kemampuan teknis maupun koordinasi tim. Saya pernah dipercaya menjadi <b>Asisten Dosen Kalkulus</b> yang bertugas mendampingi proses pembelajaran kelas serta mengelola penginputan nilai mahasiswa. Selain itu, saya juga membantu dosen dalam mengarahkan dan mendampingi peserta secara langsung pada kegiatan GTS (Goes to School).
    </p>
    <p class="desc-text">
        Di luar aktivitas akademik, saya memiliki pengalaman kerja sebagai <b>Guru Teknik Informatika di SMP Fullday Al Muhajirin 2</b>, di mana saya mengajar dan menyusun materi pembelajaran dasar IT. Saya juga aktif dalam kepanitiaan kampus, di antaranya sebagai Seksi Acara untuk kegiatan Masa Bimbingan, Seksi PDD pada Pelantikan Ketua Humanika, serta Sekretaris dalam penyelenggaraan acara workshop. Selama perkuliahan, saya konsisten menyelesaikan berbagai proyek berbasis teknologi dan pemrograman dengan baik.
    </p>
    <p class="desc-text" style="margin-bottom:0 !important;">
        Melalui seluruh pengalaman tersebut, saya terbiasa bekerja secara terorganisir, berkomunikasi dengan baik, dan siap berkontribusi secara aktif serta profesional dalam tim.
    </p>
</div>
""", unsafe_allow_html=True)

# 5. Section Aktivitas dan Kegiatan Sosial
st.markdown("""
<div class="section-title-box">
    <div class="section-icon">👥</div>
    <div>
        <div class="section-title">Aktivitas dan Kegiatan Sosial</div>
        <div style="font-size:17px !important; color:#64748B; font-weight:500;">Berbagai kegiatan dan kepanitiaan yang pernah diikuti selama masa perkuliahan.</div>
    </div>
</div>

<div class="org-grid">
    <div class="org-card-item">
        <div class="org-card-header">
            <div class="org-card-icon">📌</div>
            <div class="org-title">Panitia Pelantikan Ketua Humanika<br><span class="org-sub-title">(Divisi PDD)</span></div>
        </div>
        <ul class="org-list">
            <li>Mengelola kebutuhan visual, desain materi promosi, dan publikasi acara.</li>
            <li>Bertanggung jawab atas dokumentasi kegiatan dan bekerja sama dalam tim lintas divisi.</li>
        </ul>
    </div>
    <div class="org-card-item">
        <div class="org-card-header">
            <div class="org-card-icon">📌</div>
            <div class="org-title">Panitia Masa Bimbingan / MARIM<br><span class="org-sub-title">(Seksi Acara)</span></div>
        </div>
        <ul class="org-list">
            <li>Menyusun rundown dan alur teknis keberlangsungan acara untuk peserta.</li>
            <li>Mengkoordinasikan jalannya kegiatan di lapangan agar tepat waktu dan teratur.</li>
        </ul>
    </div>
    <div class="org-card-item">
        <div class="org-card-header">
            <div class="org-card-icon">📌</div>
            <div class="org-title">Fasilitator Kegiatan GTS<br><span class="org-sub-title">(Goes to School)</span></div>
        </div>
        <ul class="org-list">
            <li>Mendorong dan mendampingi siswa secara langsung saat praktik materi teknis.</li>
            <li>Membantu pemecahan masalah (troubleshooting) teknis dasar bagi peserta selama kegiatan.</li>
        </ul>
    </div>
    <div class="org-card-item">
        <div class="org-card-header">
            <div class="org-card-icon">📌</div>
            <div class="org-title">Panitia Workshop Kampus<br><span class="org-sub-title">(Sekretaris)</span></div>
        </div>
        <ul class="org-list">
            <li>Mengelola administrasi, surat-menyurat, serta dokumentasi berkas acara.</li>
            <li>Menyusun laporan pertanggungjawaban dan mencatat jalannya kegiatan.</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)

# 6. Section Lokasi Kampus
st.markdown("""
<div class="section-title-box" style="margin-top: 10px;">
    <div class="section-icon">📍</div>
    <div>
        <div class="section-title">Lokasi Kampus</div>
        <div style="font-size:17px !important; color:#64748B; font-weight:500;">STT Wastukancana — Mulyamekar, Babakancikao, Kab. Purwakarta, Jawa Barat</div>
    </div>
</div>
""", unsafe_allow_html=True)

map_data = [{
    "lat": -6.5165,
    "lon": 107.4478
}]
st.map(map_data, zoom=14)

st.markdown("<br><hr style='border: 0.5px solid #E2E8F0;'><center style='color:#94A3B8; font-size: 15px !important;'>© 2026 Az Zahra Putri Al Khoiri. Crafted with Python & Streamlit.</center>", unsafe_allow_html=True)
