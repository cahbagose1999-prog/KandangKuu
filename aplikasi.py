import streamlit as st

# =====================================================================
# 1. MOBILE-FIRST INJECTION (MENGIKUTI BACKGROUND HP & MENUTUP RUANG KOSONG)
# =====================================================================
st.markdown("""
<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>
<style>
    /* Menghapus padding bawaan Streamlit agar aplikasi rapat penuh ke ujung layar HP */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 12px !important;
        padding-right: 12px !important;
        max-width: 480px !important; /* Mengunci lebar agar pas seperti aplikasi HP asli */
        margin: 0 auto;
    }
    
    /* Mengikuti sistem tema bawaan HP (Dark Mode / Light Mode otomatis) */
    @media (prefers-color-scheme: dark) {
        .kartu-kandang, .kartu-tugas { background-color: #1E293B !important; color: #F8FAFC !important; }
        .teks-judul { color: #F8FAFC !important; }
        .sub-teks { color: #94A3B8 !important; }
    }
    @media (prefers-color-scheme: light) {
        .kartu-kandang, .kartu-tugas { background-color: #FFFFFF !important; color: #0F172A !important; }
        .teks-judul { color: #0F172A !important; }
        .sub-teks { color: #64748B !important; }
    }

    /* Kartu Melengkung Padat Ringkas (Tanpa Jarak Kosong Besar) */
    .kartu-kandang {
        padding: 14px;
        border-radius: 14px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04);
        margin-bottom: 10px;
        border-left: 4px solid #2E7D32;
    }
    
    /* Kartu Peringatan Oranye Tipis */
    .kartu-peringatan {
        background-color: #FFF3E0;
        padding: 10px 14px;
        border-radius: 10px;
        margin-bottom: 8px;
        border-left: 4px solid #EF6C00;
        font-size: 13px;
        color: #E65100;
    }

    /* Grid Khusus HP untuk Ringkasan Data (Samping-Sampingan, Bukan Kebawah) */
    .grid-ringkasan {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-bottom: 15px;
    }
    .badge-ringkasan {
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        font-size: 13px;
    }

    /* Merapikan Tombol */
    .stButton>button {
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 6px 12px !important;
        font-size: 14px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="KandangKu App", page_icon="🐔")

# =====================================================================
# 2. DATABASE SIMULASI (MEMORI HP)
# =====================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "stok_pakan" not in st.session_state:
    st.session_state.stok_pakan = 85.0  # Memicu notifikasi pakan kritis
if "tugas_pakan_done" not in st.session_state:
    st.session_state.tugas_pakan_done = False

if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"nama": "Pembesaran Timur", "tipe": "Ayam KUB Pembesaran", "umur": 35, "populasi": 190, "mortalitas": 1},
        {"nama": "Indukan Omega", "tipe": "Ayam KUB Petelur / Indukan", "umur": 120, "populasi": 250, "mortalitas": 0},
        {"nama": "Pembesaran Barat", "tipe": "Ayam KUB Pembesaran", "umur": 20, "populasi": 160, "mortalitas": 0}
    ]

# =====================================================================
# ALUR HALAMAN 1: GERBANG LOGIN
# =====================================================================
if st.session_state.halaman_aktif == "MENU_LOGIN":
    st.markdown("<h2 class='teks-judul' style='text-align: center; margin-bottom:2px;'>🐔 KandangKu</h2>", unsafe_allow_html=True)
    st.markdown("<p class='sub-teks' style='text-align: center; font-size:14px; margin-top:0;'>Asisten Manajemen Unggas Berbasis AI & IoT</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Masuk ke Simulasi Aplikasi ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.rerun()

# =====================================================================
# ALUR HALAMAN 2: PROFILE INPUT
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.markdown("<h3 class='teks-judul'>👤 Data Peternak</h3>", unsafe_allow_html=True)
    nama_input = st.text_input("Nama Lengkap:", placeholder="Contoh: Pak Budi")
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    if st.button("Buka Dashboard Kandang 🔓", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Kolom wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}"
            st.session_state.halaman_aktif = "MENU_MULTI_KANDANG"
            st.rerun()

# =====================================================================
# ALUR HALAMAN 3: DASHBOARD KHUSUS HP (RAPAT & PADAT)
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_MULTI_KANDANG":
    # Header Rapat
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%); padding: 14px; border-radius: 12px; color: white; margin-bottom: 12px;'>
        <h4 style='margin: 0; color: white !important;'>☀️ Selamat Pagi, {st.session_state.nama_peternak}!</h4>
        <small style='opacity: 0.9;'>Semangat hari ini, panen sukses menanti 🌾 ({st.session_state.lokasi_peternak})</small>
    </div>
    """, unsafe_allow_html=True)
    
    # PERINGATAN SISTEM (PADAT)
    st.markdown("<h4 class='teks-judul' style='margin-bottom:6px;'>⚠️ Peringatan</h4>", unsafe_allow_html=True)
    st.markdown("<div class='kartu-peringatan'>💉 <b>Vaksinasi:</b> Jadwal Vaksin ND Pembesaran Timur hari ini!</div>", unsafe_allow_html=True)
    if st.session_state.stok_pakan < 100:
        st.markdown(f"<div class='kartu-peringatan' style='background-color:#FFEBEE; border-left:4px solid #C62828; color:#C62828;'>🚨 <b>Kritis:</b> Stok pakan menipis, sisa <b>{st.session_state.stok_pakan:.1f} Kg</b>!</div>", unsafe_allow_html=True)

    # TUGAS CHECKLIST (RAPAT)
    st.markdown("<h4 class='teks-judul' style='margin-bottom:6px;'>📋 Tugas Hari Ini</h4>", unsafe_allow_html=True)
    with st.container(border=True):
        total_pop = sum(k['populasi'] for k in st.session_state.daftar_kandang)
        pakan_dibutuhkan = total_pop * 0.1
        
        tugas_pakan = st.checkbox(f"🟢 Beri Pakan Pagi ({pakan_dibutuhkan:.1f} Kg)", value=st.session_state.tugas_pakan_done)
        if tugas_pakan and not st.session_state.tugas_pakan_done:
            st.session_state.stok_pakan -= pakan_dibutuhkan
            st.session_state.tugas_pakan_done = True
            st.rerun()
        elif not tugas_pakan and st.session_state.tugas_pakan_done:
            st.session_state.stok_pakan += pakan_dibutuhkan
            st.session_state.tugas_pakan_done = False
            st.rerun()
        st.checkbox("💧 Cek Air Minum & Sanitasi", value=False)

    # RINGKASAN DATA (2 KOLOM JAJAR KANAN-KIRI BIAR TIDAK KOSONG)
    st.markdown("<h4 class='teks-judul' style='margin-top:10px; margin-bottom:6px;'>📊 Ringkasan Sektor</h4>", unsafe_allow_html=True)
    total_kand = len(st.session_state.daftar_kandang)
    total_mort = sum(k['mortalitas'] for k in st.session_state.daftar_kandang)
    
    st.markdown(f"""
    <div class='grid-ringkasan'>
        <div class='badge-ringkasan' style='background-color: #E8F5E9; border: 1px solid #C8E6C9; color: #2E7D32;'>
            <b>Kandang Aktif</b><br><span style='font-size:16px; font-weight:bold;'>{total_kand} Sektor</span>
        </div>
        <div class='badge-ringkasan' style='background-color: #E3F2FD; border: 1px solid #BBDEFB; color: #1565C0;'>
            <b>Total Populasi</b><br><span style='font-size:16px; font-weight:bold;'>{total_pop:,} Ekor</span>
        </div>
        <div class='badge-ringkasan' style='background-color: #FFF3E0; border: 1px solid #FFE0B2; color: #EF6C00;'>
            <b>Produksi Telur</b><br><span style='font-size:16px; font-weight:bold;'>320 Butir</span>
        </div>
        <div class='badge-ringkasan' style='background-color: #FFEBEE; border: 1px solid #FFCDD2; color: #C62828;'>
            <b>Mortalitas</b><br><span style='font-size:16px; font-weight:bold;'>{total_mort} Ekor</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KARTU BANGUNAN KANDANG (PADAT MERAPAT KEBANTING)
    st.markdown("<h4 class='teks-judul' style='margin-bottom:6px;'>🛖 Daftar Kandang KUB</h4>", unsafe_allow_html=True)
    for idx, kandang in enumerate(st.session_state.daftar_kandang):
        st.markdown(f"""
        <div class='kartu-kandang'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <b style='font-size:15px;'>{kandang['nama']}</b>
                <span style='background-color:#E8F5E9; color:#2E7D32; font-size:10px; padding:2px 6px; border-radius:6px; font-weight:bold;'>Active</span>
            </div>
            <p style='margin:4px 0 0 0; font-size:13px; opacity:0.8;'>
                🧬 {kandang['tipe']} <br>
                📅 Umur: {kandang['umur']} Hari | 📊 Pop: {kandang['populasi']} Ekor | ❌ Mati: {kandang['mortalitas']}
            </p>
