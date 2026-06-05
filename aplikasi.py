import streamlit as st
import pandas as pd
from datetime import datetime

# PROTEKSI UTAMA DARI ERROR TERJEMAHAN OTOMATIS BROWSER HP
st.markdown("<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>", unsafe_allow_html=True)
st.markdown("<style>.block-container {padding: 12px !important; max-width: 460px !important; margin: 0 auto;} h2, h3, h4, h5 {color: #1B5E20 !important; font-family: 'Inter', sans-serif;}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="KandangKu App", page_icon="🐔")

# =====================================================================
# DATABASE SIMULASI PATEN (MEMORI BROWSER HP)
# =====================================================================
if "halaman_aktif" not in st.session_state: st.session_state.halaman_aktif = "LOGIN"
if "nama_peternak" not in st.session_state: st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state: st.session_state.lokasi_peternak = ""
if "jenis_unggas" not in st.session_state: st.session_state.jenis_unggas = ""
if "status_bisnis" not in st.session_state: st.session_state.status_bisnis = ""
if "tab_aktif" not in st.session_state: st.session_state.tab_aktif = "🏠 Beranda"

# Logistik & Keuangan Global
if "stok_pakan" not in st.session_state: st.session_state.stok_pakan = 500.0
if "sisa_uang" not in st.session_state: st.session_state.sisa_uang = 5000000

# JURNAL RIWAYAT PATEN (Pusat Data Evaluasi & AI)
if "jurnal_riwayat" not in st.session_state:
    st.session_state.jurnal_riwayat = [
        {"Tanggal": "2026-06-04", "Kandang": "Kandang Blok A", "Pakan (Kg)": 20.0, "Ayam Mati": 0, "Panen Telur": 150},
        {"Tanggal": "2026-06-05", "Kandang": "Kandang Blok A", "Pakan (Kg)": 20.0, "Ayam Mati": 1, "Panen Telur": 148}
    ]

# Daftar Kandang Bawaan
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"id": 0, "nama": "Kandang Blok A", "tipe": "Ayam KUB Pembesaran", "umur": 35, "populasi": 200},
        {"id": 1, "nama": "Kandang Blok B", "tipe": "Ayam KUB Petelur", "umur": 120, "populasi": 300}
    ]

# =====================================================================
# HALAMAN 1: GERBANG LOGIN
# =====================================================================
if st.session_state.halaman_aktif == "LOGIN":
    st.markdown("<h2 style='text-align: center;'>🐔 KandangKu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; font-size:14px; margin-top:0;'>Asisten Manajemen Unggas Berbasis AI & IoT</p>", unsafe_allow_html=True)
    st.write("")
    st.link_button("🟢 Masuk Cepat via WhatsApp", "https://wa.me", use_container_width=True)
    st.link_button("🔴 Masuk Cepat via Akun Google", "https://google.com", use_container_width=True)
    st.divider()
    if st.button("Lanjutkan ke Pengisian Data ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "PROFIL"
        st.rerun()

# =====================================================================
# HALAMAN 2: SETUP DATA AWAL KOMODITAS
# =====================================================================
elif st.session_state.halaman_aktif == "PROFIL":
    st.markdown("<h3>👤 Setup Awal Peternakan</h3>", unsafe_allow_html=True)
    nama_input = st.text_input("Nama Lengkap Pemilik:", placeholder="Contoh: Pak Budi")
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    unggas_input = st.selectbox("Pilih Jenis Komoditas Ternak:", ["Ayam Kampung Unggul Balitbangtan (Ayam KUB)", "Ayam Broiler", "Bebek"])
    status_bisnis_input = st.radio("Sistem Tata Kelola Bisnis:", ["Peternak Mandiri", "Peternak Kemitraan"])
    
    if st.button("Simpan & Buka Aplikasi 🔓", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Seluruh data wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}"
            st.session_state.jenis_unggas = unggas_input
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "APLIKASI_UTAMA"
            st.rerun()

# =====================================================================
# HALAMAN 3: SATU LAYAR UTAMA (SINGLE PAGE WITH 5 BOTTOM NAV)
# =====================================================================
elif st.session_state.halaman_aktif == "APLIKASI_UTAMA":
    st.markdown(f"<small>👤 {st.session_state.nama_peternak} | 📍 {st.session_state.lokasi_peternak}</small>", unsafe_allow_html=True)
    st.write("")

    # -----------------------------------------------------------------
    # NAV MENU 1: BERANDA
    # -----------------------------------------------------------------
    if st.session_state.tab_aktif == "🏠 Beranda":
        st.markdown(f"<div style='background-color: #1B5E20; padding: 12px; border-radius: 12px; color: white; margin-bottom: 12px;'><h4 style='margin: 0; color: white !important;'>☀️ Selamat Pagi, {st.session_state.nama_peternak}!</h4><small>🧬 Komoditas: {st.session_state.jenis_unggas}</small></div>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='margin-bottom:4px;'>⚠️ Peringatan Sistem</h5>", unsafe_allow_html=True)
        st.markdown("<div style='background-color: #FFF3E0; padding: 8px 12px; border-radius: 8px; font-size: 13px; color: #E65100;'>💉 <b>Vaksinasi:</b> Jadwal Vaksin ND Kandang Blok A hari ini!</div>", unsafe_allow_html=True)
        
        st.markdown("<h5 style='margin-top:12px; margin-bottom:4px;'>🛖 Blok Kandang Aktif</h5>", unsafe_allow_html=True)
        for kandang in st.session_state.daftar_kandang:
            with st.container(border=True):
                st.markdown(f"<b>🛖 {kandang['nama']}</b> ({kandang['tipe']})", unsafe_allow_html=True)
                st.markdown(f"<p style='margin:0; font-size:13px; opacity:0.8;'>📅 Umur: {kandang['umur']} Hari | 📊 Populasi: {kandang['populasi']} Ekor</p>", unsafe_allow_html=True)
        
        # Pemicu Chat AI On-Demand (Bila ada yang ingin diobrolkan)
        st.divider()
        st.markdown("##### 🤖 Tanya Asisten AI")
        if st.button("💡 Aktifkan Asisten AI untuk Analisis Kandang", use_container_width=True):
            st.markdown(f"<div style='background-color: #E3F2FD; padding: 12px; border-radius: 10px; border-left: 4px solid #1565C0; color: #1565C0; font-size:13px;'>🤖 <b>Analisis AI:</b> Halo {st.session_state.nama_peternak}, saya sudah membaca data sensor IoT dan buku Riwayat Anda. Perubahan suhu kelembapan malam hari berisiko membuat ayam stres. Saran saya, campurkan <b>60 gram vitamin unggas</b> di bak air minum sekarang!</div>", unsafe_allow_html=True)

    # -----------------------------------------------------------------
    # NAV MENU 2: URUS KANDANG (INPUT BEBAS KAPAN SAJA)
    # -----------------------------------------------------------------
    elif st.session_state.tab_aktif == "📋 Urus":
        st.markdown("<h3>📋 Lembar Catatan Hari Ini</h3>", unsafe_allow_html=True)
        st.write("Isi laporan di bawah kapan saja secara bebas. Data langsung tersimpan permanen.")
        
        kandang_pilihan = st.selectbox("Pilih Kandang yang Mau Diisi:", ["Kandang Blok A", "Kandang Blok B"])
        
        with st.form("form_pencatatan_bebas"):
            st.markdown(f"##### ✍️ Laporan untuk {kandang_pilihan}")
            input_pakan = st.number_input("Jumlah Pakan yang Diberikan (Kg):", min_value=0.0, value=20.0, step=1.0)
            input_mati = st.number_input("Jumlah Ayam Mati Hari Ini (Ekor):", min_value=0, value=0, step=1)
            input_panen = st.number_input("Hasil Panen Telur Hari Ini (Butir):", min_value=0, value=0, step=1)
            
            simpan_laporan = st.form_submit_button("🔒 Simpan & Kirim Laporan", use_container_width=True)
            
            if simpan_laporan:
                # 1. Potong Stok Gudang & Uang Kas Global secara otomatis
                st.session_state.stok_pakan -= input_pakan
                st.session_state.sisa_uang -= (input_pakan * 8500) # Biaya pakan otomatis tercatat
                
                # 2. Kurangi populasi kandang jika ada yang mati
                for k in st.session_state.daftar_kandang:
                    if k['nama'] == kandang_pilihan:
                        k['populasi'] -= input_mati
                
                # 3. Masukkan data secara PATEN ke Jurnal Riwayat
                hari_ini = datetime.now().strftime("%Y-%m-%d")
                st.session_state.jurnal_riwayat.append({
                    "Tanggal": hari_ini, "Kandang": list(kandang_pilihan)[-6:], "Pakan (Kg)": input_pakan, "Ayam Mati": input_mati, "Panen Telur": input_panen
                })
                st.success(f"🎉 Sukses! Data dikunci ke buku Riwayat & Stok otomatis terpotong!")
                st.rerun()

    # -----------------------------------------------------------------
    # NAV MENU 3: SENSOR IOT (LAMPU LALU LINTAS)
    # -----------------------------------------------------------------
    elif st.session_state.tab_aktif == "🌐 IoT":
        st.markdown("<h3>🌐 Pemantauan Sensor IoT</h3>", unsafe_allow_html=True)
        st.write("Terhubung dengan aplikasi pihak ke-3. Cukup pantau warna indikator keselamatan.")
        st.write("")
        
        # Simulasi Sensor 1: Suhu (HIJAU/IDEAL)
        st.markdown("<div style='background-color: #E8F5E9; padding: 12px; border-radius: 10px; border-left: 5px solid #2E7D32; color: #2E7D32;'>🟢 <b>Suhu Udara Kandang: 27.5 °C</b><br>Status: Sangat Nyaman & Ideal untuk Ayam KUB.</div>", unsafe_allow_html=True)
