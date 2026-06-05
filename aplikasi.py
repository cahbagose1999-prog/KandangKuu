import streamlit as st

# PROTEKSI UTAMA: Anti Gagal Muat dari Browser HP
st.markdown("<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>", unsafe_allow_html=True)
st.markdown("<style>.block-container {padding: 12px !important; max-width: 460px !important; margin: 0 auto;}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="KandangKu App", page_icon="🐔")

# =====================================================================
# DATABASE SIMULASI (MEMORI BROWSER HP)
# =====================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "jenis_unggas" not in st.session_state:
    st.session_state.jenis_unggas = ""
if "status_bisnis" not in st.session_state:
    st.session_state.status_bisnis = ""
if "kandang_dipilih" not in st.session_state:
    st.session_state.kandang_dipilih = None

# Memori Logistik
if "stok_pakan" not in st.session_state:
    st.session_state.stok_pakan = 85.0
if "tugas_pakan_done" not in st.session_state:
    st.session_state.tugas_pakan_done = False

# Daftar Kandang Bawaan
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"id": 0, "nama": "Kandang Blok A", "tipe": "Pembesaran", "umur": 35, "populasi": 190, "mortalitas": 1, "pakan_done": False},
        {"id": 1, "nama": "Kandang Blok B", "tipe": "Indukan/Petelur", "umur": 120, "populasi": 250, "mortalitas": 0, "pakan_done": False}
    ]

# =====================================================================
# HALAMAN 1: GERBANG LOGIN (PRIORITAS UTAMA)
# =====================================================================
if st.session_state.halaman_aktif == "LOGIN":
    st.markdown("<h2 style='text-align: center; color: #2E7D32;'>🟢 KandangKu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; font-size:14px; margin-top:0;'>Asisten Manajemen Unggas Berbasis AI & IoT</p>", unsafe_allow_html=True)
    st.divider()
    
    # Tombol Akses Utama
    link_wa = "https://wa.me"
    st.link_button("🟢 Masuk Cepat via WhatsApp", link_wa, use_container_width=True)
    
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google", link_google, use_container_width=True)
    
    st.divider()
    st.caption("⚙️ **Simulasi Pengujian Blueprint:**")
    if st.button("Lanjutkan ke Pengisian Data ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "PROFIL"
        st.rerun()

# =====================================================================
# HALAMAN 2: PENDAFTARAN & KONFIRMASI KOMODITAS UNGGAS
# =====================================================================
elif st.session_state.halaman_aktif == "PROFIL":
    st.markdown("<h3 style='color: #2E7D32;'>👤 Setup Awal Peternakan</h3>", unsafe_allow_html=True)
    st.write("Lengkapi profil data dasar Anda dan komoditas unggas:")
    st.write("")
    
    # Bagian A: Biodata
    nama_input = st.text_input("Nama Lengkap Pemilik:", placeholder="Contoh: Pak Budi")
    
    st.markdown("<b>📍 Wilayah Cakupan Kandang</b>", unsafe_allow_html=True)
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    # Bagian B: Konfirmasi Jenis Ternak Unggas (Koreksi Penting Anda!)
    st.markdown("<b>🧬 Konfirmasi Komoditas Unggas Utama</b>", unsafe_allow_html=True)
    unggas_input = st.selectbox(
        "Pilih Jenis Komoditas Ternak Anda:",
        [
            "Ayam Kampung Unggul Balitbangtan (Ayam KUB)",
            "Ayam Broiler (Pedaging Industri)",
            "Ayam Layer (Petelur Ras)",
            "Bebek (Petelur / Pedaging)",
            "Burung Puyuh Petelur"
        ]
    )
    
    st.divider()
    # Bagian C: Status Kelola
    status_bisnis_input = st.radio("Sistem Tata Kelola Bisnis:", ["Peternak Mandiri (Kelola Sendiri)", "Peternak Kemitraan (Ikut SOP Perusahaan/PT)"])
    
    st.write("")
    if st.button("Simpan & Buka Dashboard 🔓", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Seluruh data identitas lokasi wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}"
            st.session_state.jenis_unggas = unggas_input
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "DASHBOARD"
            st.rerun()

# =====================================================================
# HALAMAN 3: DASHBOARD RINGKAS (KESIMPULAN PENTING & WIDGET CUACA)
# =====================================================================
elif st.session_state.halaman_aktif == "DASHBOARD":
    # Header Ringkas Berwarna Hijau
    st.markdown(f"<div style='background-color: #1B5E20; padding: 12px; border-radius: 12px; color: white; margin-bottom: 12px;'><h4 style='margin: 0; color: white;'>☀️ {st.session_state.nama_peternak} Dashboard</h4><small>🧬 Komoditas: {st.session_state.jenis_unggas}</small></div>", unsafe_allow_html=True)
    
    # WIDGET CUACA LOKAL REAL-TIME (BARU - REPLIKA PERMINTAAN)
    st.markdown("##### 🌤️ Kondisi Lingkungan Kandang Saat Ini")
    st.markdown(f"<div style='background-color: #E3F2FD; padding: 10px; border-radius: 10px; border: 1px solid #BBDEFB; font-size:13px; color:#1565C0;'>📍 Wilayah: <b>{st.session_state.lokasi_peternak}</b><br>🌡️ Suhu Udara: <b>27.5 °C</b> (Ideal) | 💧 Kelembapan: <b>65%</b><br>🔮 Prediksi: Berpotensi hujan ringan sore nanti.</div>", unsafe_allow_html=True)

    # PERINGATAN DARURAT PENDEK
    st.markdown("<h5 style='margin-bottom:4px; margin-top:12px;'>⚠️ Peringatan Sistem</h5>", unsafe_allow_html=True)
    st.markdown("<div style='background-color: #FFF3E0; padding: 8px 12px; border-radius: 8px; margin-bottom: 6px; border-left: 4px solid #EF6C00; font-size: 13px; color: #E65100;'>💉 <b>Vaksin:</b> Jadwal Vaksin ND Blok A hari ini!</div>", unsafe_allow_html=True)
    if st.session_state.stok_pakan < 100:
        st.markdown(f"<div style='background-color: #FFEBEE; padding: 8px 12px; border-radius: 8px; margin-bottom: 6px; border-left: 4px solid #C62828; font-size: 13px; color: #C62828;'>🚨 <b>Kritis:</b> Stok pakan gudang menipis ({st.session_state.stok_pakan:.1f} Kg)!</div>", unsafe_allow_html=True)

    # KESIMPULAN REKAP SEKTOR
    st.markdown("<h5 style='margin-bottom:4px; margin-top:12px;'>📊 Ringkasan Sektor</h5>", unsafe_allow_html=True)
    total_pop = sum(k['populasi'] for k in st.session_state.daftar_kandang)
    st.info(f"🛖 Kandang Aktif: {len(st.session_state.daftar_kandang)} Sektor | 👥 Total Populasi: {total_pop:,} Ekor")

    # DAFTAR BLOK KANDANG AKTIF
    st.markdown("<h5 style='margin-bottom:4px; margin-top:12px;'>🛖 Pilih Blok Kandang:</h5>", unsafe_allow_html=True)
    for kandang in st.session_state.daftar_kandang:
        with st.container(border=True):
            st.markdown(f"<b>🛖 {kandang['nama']} ({kandang['tipe']})</b>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin:0; font-size:13px; opacity:0.8;'>📅 Umur: {kandang['umur']} Hari | 📊 Pop: {kandang['populasi']} Ekor</p>", unsafe_allow_html=True)
            st.write("")
            if st.button(f"Buka Lembar Tugas {kandang['nama']} ➡️", key=f"btn_{kandang['id']}", use_container_width=True):
                st.session_state.kandang_dipilih = kandang
                st.session_state.halaman_aktif = "LEMBAR_TUGAS"
                st.rerun()

    st.divider()
    if st.button("⬅️ Keluar / Ganti Akun", use_container_width=True):
        st.session_state.halaman_aktif = "LOGIN"
        st.rerun()

# =====================================================================
# HALAMAN 4: LEMBAR TUGAS HARIAN & ASISTEN AI PASIF (ON-DEMAND)
# =====================================================================
elif st.session_state.halaman_aktif == "LEMBAR_TUGAS":
    kandang = st.session_state.kandang_dipilih
    
    st.markdown(f"### 🛖 Urus: {kandang['nama']}")
    st.caption(f"🧬 Komoditas: {st.session_state.jenis_unggas} | 📅 Umur: {kandang['umur']} Hari")
    
    if st.button("⬅️ Kembali ke Dashboard Utama", use_container_width=True):
        st.session_state.halaman_aktif = "DASHBOARD"
        st.rerun()
        
    st.divider()

    # LEMBAR TUGAS HARIAN SANGAT MUDAH
    st.markdown("##### 📋 Lembar Tugas Hari Ini")
    with st.container(border=True):
        kebutuhan_pakan = kandang['populasi'] * 0.1
        cek_pakan = st.checkbox(f"Sudah Beri Pakan Hari Ini ({kebutuhan_pakan:.1f} Kg)", value=kandang['pakan_done'])
        
        if cek_pakan and not kandang['pakan_done']:
            st.session_state.stok_pakan -= kebutuhan_pakan
            kandang['pakan_done'] = True
            st.success("✅ Stok pakan otomatis terpotong di gudang latar belakang!")
            st.rerun()
        elif not cek_pakan and kandang['pakan_done']:
            st.session_state.stok_pakan += kebutuhan_pakan
            kandang['pakan_done'] = False
            st.rerun()

        st.write("")
        ayam_mati = st.number_input("Catat Ayam Mati Hari Ini (Ekor):", min_value=0, value=kandang['mortalitas'], step=1)
        if ayam_mati != kandang['mortalitas']:
            kandang['populasi'] -= (ayam_mati - kandang['mortalitas'])
            kandang['mortalitas'] = ayam_mati
            st.success("Data populasi diperbarui!")
