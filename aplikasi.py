import streamlit as st

# PROTEKSI UTAMA DARI ERROR TERJEMAHAN OTOMATIS BROWSER HP
st.markdown("<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>", unsafe_allow_html=True)

# KONFIGURASI HALAMAN AGAR MERAPAT DI LAYAR HP (MENUTUP RUANG KOSONG)
st.markdown("<style>.block-container {padding: 12px !important; max-width: 460px !important; margin: 0 auto;}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="KandangKu App", page_icon="🐔")

# =====================================================================
# DATABASE SIMULASI (MEMORI BROWSER HP)
# =====================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "stok_pakan" not in st.session_state:
    st.session_state.stok_pakan = 85.0
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
    st.markdown("<h2 style='text-align: center; margin-bottom:0;'>🐔 KandangKu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; font-size:14px; margin-top:0;'>Asisten Manajemen Unggas Berbasis AI & IoT</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Masuk ke Simulasi Aplikasi ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.rerun()

# =====================================================================
# ALUR HALAMAN 2: PROFILE INPUT
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.markdown("<h3>👤 Data Peternak</h3>", unsafe_allow_html=True)
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
    # Header Kotak Rapat Berwarna Hijau Daun
    st.markdown(f"<div style='background-color: #1B5E20; padding: 12px; border-radius: 12px; color: white; margin-bottom: 12px;'><h4 style='margin: 0; color: white;'>☀️ Selamat Pagi, {st.session_state.nama_peternak}!</h4><small>Semangat hari ini, panen sukses menanti 🌾 ({st.session_state.lokasi_peternak})</small></div>", unsafe_allow_html=True)
    
    # PERINGATAN SISTEM (PADAT)
    st.markdown("<h4 style='margin-bottom:4px; margin-top:10px;'>⚠️ Peringatan</h4>", unsafe_allow_html=True)
    st.markdown("<div style='background-color: #FFF3E0; padding: 10px; border-radius: 10px; margin-bottom: 6px; border-left: 4px solid #EF6C00; font-size: 13px; color: #E65100;'>💉 <b>Vaksinasi:</b> Jadwal Vaksin ND Pembesaran Timur hari ini!</div>", unsafe_allow_html=True)
    
    if st.session_state.stok_pakan < 100:
        st.markdown(f"<div style='background-color: #FFEBEE; padding: 10px; border-radius: 10px; margin-bottom: 6px; border-left: 4px solid #C62828; font-size: 13px; color: #C62828;'>🚨 <b>Kritis:</b> Stok pakan menipis, sisa <b>{st.session_state.stok_pakan:.1f} Kg</b>!</div>", unsafe_allow_html=True)

    # TUGAS CHECKLIST (RAPAT)
    st.markdown("<h4 style='margin-bottom:4px;'>📋 Tugas Hari Ini</h4>", unsafe_allow_html=True)
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

    # RINGKASAN DATA (AKAN MENGIKUTI MODEL HP KARENA SUDAH DIKUNCI DI ATAS)
    st.markdown("<h4 style='margin-top:10px; margin-bottom:4px;'>📊 Ringkasan Sektor</h4>", unsafe_allow_html=True)
    total_kand = len(st.session_state.daftar_kandang)
    total_mort = sum(k['mortalitas'] for k in st.session_state.daftar_kandang)
    
    # Membuat 4 Indikator Data Padat
    st.info(f"🛖 Kandang Aktif: {total_kand} Sektor")
    st.info(f"👥 Total Populasi: {total_pop:,} Ekor")
    st.warning("🥚 Produksi Telur: 320 Butir")
    st.error(f"❌ Total Kematian: {total_mort} Ekor")

    # KARTU BANGUNAN KANDANG (KOTAK MELENGKUNG YANG IKUT BACKGROUND HP)
    st.markdown("<h4 style='margin-top:10px; margin-bottom:4px;'>🛖 Daftar Kandang KUB</h4>", unsafe_allow_html=True)
    for idx, kandang in enumerate(st.session_state.daftar_kandang):
        with st.container(border=True):
            st.markdown(f"<b>🛖 {kandang['nama']}</b>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin:0; font-size:13px; opacity:0.8;'>🧬 {kandang['tipe']}<br>📅 Umur: {kandang['umur']} Hari | 📊 Pop: {kandang['populasi']} Ekor | ❌ Mati: {kandang['mortalitas']} Ekor</p>", unsafe_allow_html=True)

    st.write("")
    if st.button("⬅️ Keluar / Reset Akun", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_LOGIN"
        st.rerun()
