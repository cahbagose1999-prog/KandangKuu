import streamlit as st

# =====================================================================
# 1. PROTEKSI GOOGLE TRANSLATE & CUSTOM CSS TEMA PREMIUM (HIJAU DAUN)
# =====================================================================
st.markdown("""
<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>
<style>
    /* Mengubah latar belakang utama menjadi putih bersih */
    .stApp {
        background-color: #F8F9FA;
    }
    /* Mengubah gaya teks judul utama */
    h1, h2, h3, h4 {
        color: #1E3A1E !important;
        font-family: 'Inter', sans-serif;
    }
    /* Membuat kotak kartu (Card) melengkung mirip di gambar */
    .kartu-kandang {
        background-color: #FFFFFF;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 16px;
        border-left: 5px solid #2E7D32;
    }
    /* Mengubah warna tombol Streamlit menjadi hijau daun modern */
    .stButton>button {
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1B5E20 !important;
        box-shadow: 0px 4px 10px rgba(46, 125, 50, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Konfigurasi halaman agar rapi di HP
st.set_page_config(page_title="KandangKu App", page_icon="🐔", layout="centered")

# =====================================================================
# 2. INISIALISASI MEMORI SEMENTARA (DATABASE SIMULASI AYAM KUB)
# =====================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "status_bisnis" not in st.session_state:
    st.session_state.status_bisnis = ""
    
# Data awal disesuaikan dengan tipe Ayam KUB di gambar referensi Anda
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"nama": "Pembesaran Timur", "tipe": "Ayam KUB Pembesaran (Daging)", "umur": 35, "populasi": 190, "mortalitas": 1},
        {"nama": "Indukan Omega", "tipe": "Ayam KUB Petelur / Indukan", "umur": 120, "populasi": 250, "mortalitas": 0},
        {"nama": "Pembesaran Barat", "tipe": "Ayam KUB Pembesaran (Daging)", "umur": 20, "populasi": 160, "mortalitas": 0}
    ]

# =====================================================================
# ALUR HALAMAN 1: GERBANG LOGIN CEPAT TEMA BARU
# =====================================================================
if st.session_state.halaman_aktif == "MENU_LOGIN":
    st.markdown("<h1 style='text-align: center;'>🟢 KandangKu</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555555; font-size:15px;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.write("")
    
    # Bungkus informasi dengan gaya kartu melengkung
    st.markdown("""
    <div class='kartu-kandang' style='border-left: 5px solid #0288D1;'>
        <b style='color:#0288D1;'>💡 LOGIN INSTAN LAPANGAN</b><br>
        Silakan pilih salah satu tombol masuk cepat di bawah untuk langsung terhubung ke akun KandangKu Anda.
    </div>
    """, unsafe_allow_html=True)
    
    link_wa = "https://wa.me"
    st.link_button("🟢 Masuk Cepat via WhatsApp", link_wa, use_container_width=True)
    
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google", link_google, use_container_width=True)
    
    st.divider()
    st.caption("⚙️ **Simulasi Akses Cepat:**")
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.rerun()

# =====================================================================
# ALUR HALAMAN 2: SETUP PROFIL PETERNAK TEMA BARU
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.markdown("<h2>👤 Profil Pemilik</h2>", unsafe_allow_html=True)
    st.write("Lengkapi data diri Anda untuk memulai kalibrasi data asisten AI.")
    st.write("")
    
    nama_input = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("<br><b>📍 Wilayah Cakupan Kandang</b>", unsafe_allow_html=True)
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.markdown("<br><b>💼 Model Pengelolaan Bisnis</b>", unsafe_allow_html=True)
    status_bisnis_input = st.radio(
        "Pilih Sistem Tata Kelola:", 
        ["Peternak Mandiri (Kelola Sendiri)", "Peternak Kemitraan (Ikut SOP Perusahaan/PT)"]
    )
    
    st.write("")
    if st.button("Simpan & Buka Dashboard Kandang 🔓", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Seluruh data identitas lokasi wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}"
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "MENU_MULTI_KANDANG"
            st.rerun()

# =====================================================================
# ALUR HALAMAN 3: DASHBOARD UTAMA MULTI-KANDANG (KONSEP GAMBAR REFERENSI)
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_MULTI_KANDANG":
    # Header Sambutan Selamat Pagi sesuai gambar referensi Anda
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); padding: 20px; border-radius: 16px; margin-bottom: 20px;'>
        <h3 style='margin: 0; color: #1B5E20;'>☀️ Selamat Pagi, {st.session_state.nama_peternak}!</h3>
        <p style='margin: 5px 0 0 0; color: #2E7D32; font-size: 14px;'>Semangat hari ini, panen sukses menanti 🌾</p>
        <small style='color: #4CAF50;'>📍 {st.session_state.lokasi_peternak} | {st.session_state.status_bisnis}</small>
    </div>
    """, unsafe_allow_html=True)
    
    # RINGKASAN HARI INI (REPLIKA BADGE WARNA DI GAMBAR)
    st.markdown("### 📊 Ringkasan Hari Ini")
    
    # Menghitung total data dari memori
    total_kand = len(st.session_state.daftar_kandang)
    total_pop = sum(k['populasi'] for k in st.session_state.daftar_kandang)
    total_mort = sum(k['mortalitas'] for k in st.session_state.daftar_kandang)
    
    # Desain visual badge 4 kolom memanjang ke bawah agar pas di layar HP
    st.markdown(f"""
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 25px;'>
        <div style='background-color: #E8F5E9; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #C8E6C9;'>
            <small style='color: #2E7D32; font-weight: bold;'>Kandang Aktif</small><br><b style='font-size: 18px; color: #1B5E20;'>{total_kand}</b>
        </div>
        <div style='background-color: #E3F2FD; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #BBDEFB;'>
            <small style='color: #1565C0; font-weight: bold;'>Total Populasi</small><br><b style='font-size: 18px; color: #0D47A1;'>{total_pop:,}</b>
        </div>
        <div style='background-color: #FFF3E0; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #FFE0B2;'>
            <small style='color: #EF6C00; font-weight: bold;'>Produksi Telur</small><br><b style='font-size: 18px; color: #E65100;'>Ready</b>
        </div>
        <div style='background-color: #FFEBEE; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #FFCDD2;'>
            <small style='color: #C62828; font-weight: bold;'>Mortalitas</small><br><b style='font-size: 18px; color: #B71C1C;'>{total_mort} Ekor</b>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # LIST KANDANG AKTIF (MENGGUNAKAN ELEMEN KARTU MELENGKUNG)
    st.markdown("### 🛖 Bangunan Kandang Aktif")
    
    for idx, kandang in enumerate(st.session_state.daftar_kandang):
        # Tentukan warna label badge berdasarkan tipenya
        warna_badge = "#2E7D32" if "Pembesaran" in kandang['tipe'] else "#EF6C00"
        nama_badge = "Pembesaran" if "Pembesaran" in kandang['tipe'] else "Petelur"
        
        st.markdown(f"""
        <div class='kartu-kandang'>
            <span style='background-color: {warna_badge}; color: white; padding: 3px 8px; border-radius: 8px; font-size: 11px; font-weight: bold;'>{nama_badge}</span>
            <h4 style='margin: 8px 0 4px 0;'>{kandang['nama']}</h4>
            <small style='color: gray;'>🧬 {kandang['tipe']}</small><br>
            <p style='margin: 8px 0 0 0; font-size: 14px;'>
                📅 <b>Umur:</b> {kandang['umur']} Hari <br>
                📊 <b>Populasi:</b> {kandang['populasi']} Ekor <br>
                ❌ <b>Kematian:</b> {kandang['mortalitas']} Ekor
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Buka Menu Tugas Harian: {kandang['nama']}", key=f"knd_{idx}", use_container_width=True):
            st.success(f"🎯 Membuka detail manajemen harian untuk {kandang['nama']}. Siap diintegrasikan ke halaman input tugas!")

    # FORMULIR PENAMBAHAN KANDANG BARU
    st.divider()
    st.markdown("### ➕ Daftarkan Bangunan Kandang Baru")
