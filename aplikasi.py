import streamlit as st

# =====================================================================
# 1. PROTEKSI GOOGLE TRANSLATE & CUSTOM CSS TEMA PREMIUM (HIJAU DAUN)
# =====================================================================
st.markdown("""
<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>
<style>
    .stApp {
        background-color: #F8F9FA;
    }
    h1, h2, h3, h4 {
        color: #1E3A1E !important;
        font-family: 'Inter', sans-serif;
    }
    .kartu-kandang {
        background-color: #FFFFFF;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
        margin-bottom: 16px;
        border-left: 5px solid #2E7D32;
    }
    .stButton>button {
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="KandangKu App", page_icon="🐔", layout="centered")

# =====================================================================
# 2. INISIALISASI DATABASE SEMENTARA (MEMORI BROWSER HP)
# =====================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "status_bisnis" not in st.session_state:
    st.session_state.status_bisnis = ""

# --- DATA LOGISTIK GUDANG & KEUANGAN BARU ---
if "stok_pakan" not in st.session_state:
    st.session_state.stok_pakan = 500.0  # 500 kg pakan awal di gudang
if "saldo_kas" not in st.session_state:
    st.session_state.saldo_kas = 5000000  # Rp 5.000.000 saldo awal peternakan
if "tugas_pakan_done" not in st.session_state:
    st.session_state.tugas_pakan_done = False

if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"nama": "Pembesaran Timur", "tipe": "Ayam KUB Pembesaran (Daging)", "umur": 35, "populasi": 190, "mortalitas": 1},
        {"nama": "Indukan Omega", "tipe": "Ayam KUB Petelur / Indukan", "umur": 120, "populasi": 250, "mortalitas": 0},
        {"nama": "Pembesaran Barat", "tipe": "Ayam KUB Pembesaran (Daging)", "umur": 20, "populasi": 160, "mortalitas": 0}
    ]

# =====================================================================
# ALUR HALAMAN 1: GERBANG LOGIN CEPAT
# =====================================================================
if st.session_state.halaman_aktif == "MENU_LOGIN":
    st.markdown("<h1 style='text-align: center;'>🟢 KandangKu</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555555; font-size:15px;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.rerun()

# =====================================================================
# ALUR HALAMAN 2: SETUP PROFIL PETERNAK
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.markdown("<h2>👤 Profil Pemilik</h2>", unsafe_allow_html=True)
    nama_input = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    status_bisnis_input = st.radio("Pilih Sistem Tata Kelola:", ["Peternak Mandiri", "Peternak Kemitraan"])
    
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
# ALUR HALAMAN 3: DASHBOARD UTAMA MULTI-KANDANG (DENGAN TUGAS & GUDANG)
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_MULTI_KANDANG":
    # 1. Header Sambutan
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); padding: 20px; border-radius: 16px; margin-bottom: 20px;'>
        <h3 style='margin: 0; color: #1B5E20;'>☀️ Selamat Pagi, {st.session_state.nama_peternak}!</h3>
        <p style='margin: 5px 0 0 0; color: #2E7D32; font-size: 14px;'>Semangat hari ini, panen sukses menanti 🌾</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. SEKTOR TUGAS HARI INI (BARU - REPLIKA GAMBAR CONSEP)
    st.markdown("### 📋 Tugas Hari Ini")
    with st.container(border=True):
        # Hitung kebutuhan pakan otomatis berdasarkan total populasi (Asumsi: 0.1 kg pakan per ekor ayam)
        total_pop = sum(k['populasi'] for k in st.session_state.daftar_kandang)
        pakan_dibutuhkan = total_pop * 0.1
        harga_pakan_per_kg = 8500  # Asumsi harga pakan Rp 8.500/kg
        total_biaya_pakan = pakan_dibutuhkan * harga_pakan_per_kg
        
        st.markdown(f"**Sistem Menghitung:** Total populasi {total_pop} ekor membutuhkan **{pakan_dibutuhkan:.1f} Kg** pakan hari ini.")
        
        # Checkbox interaktif tugas pakan
        tugas_pakan = st.checkbox("🟢 Beri Pakan Rutin Pagi", value=st.session_state.tugas_pakan_done)
        
        # Logika otomatisasi logistik dan keuangan di latar belakang
        if tugas_pakan and not st.session_state.tugas_pakan_done:
            st.session_state.stok_pakan -= pakan_dibutuhkan
            st.session_state.saldo_kas -= total_biaya_pakan
            st.session_state.tugas_pakan_done = True
            st.success(f"➡️ Sukses! Stok pakan berkurang {pakan_dibutuhkan:.1f} Kg & Biaya pakan otomatis tercatat di kas keuangan!")
            st.rerun()
        elif not tugas_pakan and st.session_state.tugas_pakan_done:
            st.session_state.stok_pakan += pakan_dibutuhkan
            st.session_state.saldo_kas += total_biaya_pakan
            st.session_state.tugas_pakan_done = False
            st.rerun()
            
        st.checkbox("💧 Cek Air Minum & Kebersihan", value=False)
        st.checkbox("📝 Input Pencatatan Kematian Harian", value=False)
        st.checkbox("⚖️ Sampling Bobot Mingguan", value=False)

    # 3. KOTAK STATUS MONITORING GUDANG & UANG (LATAR BELAKANG)
    with st.expander("👁️ Intip Status Gudang & Uang Real-time (Latar Belakang)"):
        st.metric(label="📦 Sisa Stok Pakan di Gudang", value=f"{st.session_state.stok_pakan:.1f} Kg")
        st.metric(label="💰 Sisa Anggaran Kas Keuangan", value=f"Rp {st.session_state.saldo_kas:,}")

    # 4. RINGKASAN DATA (BADGE WARNA DI GAMBAR)
    st.markdown("### 📊 Ringkasan Hari Ini")
    total_kand = len(st.session_state.daftar_kandang)
    total_mort = sum(k['mortalitas'] for k in st.session_state.daftar_kandang)
    
    st.markdown(f"""
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 25px;'>
        <div style='background-color: #E8F5E9; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #C8E6C9;'>
            <small style='color: #2E7D32; font-weight: bold;'>Kandang Aktif</small><br><b style='font-size: 18px; color: #1B5E20;'>{total_kand}</b>
        </div>
        <div style='background-color: #E3F2FD; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #BBDEFB;'>
            <small style='color: #1565C0; font-weight: bold;'>Total Populasi</small><br><b style='font-size: 18px; color: #0D47A1;'>{total_pop:,}</b>
        </div>
        <div style='background-color: #FFF3E0; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #FFE0B2;'>
            <small style='color: #EF6C00; font-weight: bold;'>Produksi Telur</small><br><b style='font-size: 18px; color: #E65100;'>320 Butir</b>
        </div>
        <div style='background-color: #FFEBEE; padding: 12px; border-radius: 12px; text-align: center; border: 1px solid #FFCDD2;'>
            <small style='color: #C62828; font-weight: bold;'>Mortalitas</small><br><b style='font-size: 18px; color: #B71C1C;'>{total_mort} Ekor</b>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 5. LIST KANDANG AKTIF KOTAK MELENGKUNG
    st.markdown("### 🛖 Bangunan Kandang Aktif")
    for idx, kandang in enumerate(st.session_state.daftar_kandang):
        warna_badge = "#2E7D32" if "Pembesaran" in kandang['tipe'] else "#EF6C00"
        nama_badge = "Pembesaran" if "Pembesaran" in kandang['tipe'] else "Petelur"
        
        st.markdown(f"""
        <div class='kartu-kandang'>
            <span style='background-color: {warna_badge}; color: white; padding: 3px 8px; border-radius: 8px; font-size: 11px; font-weight: bold;'>{nama_badge}</span>
            <h4 style='margin: 8px 0 4px 0;'>{kandang['nama']}</h4>
            <small style='color: gray;'>🧬 {kandang['tipe']}</small><br>
            <p style='margin: 8px 0 0 0; font-size: 14px;'>
                📅 <b>Umur:</b> {kandang['umur']} Hari | 📊 <b>Populasi:</b> {kandang['populasi']} Ekor | ❌ <b>Mortalitas:</b> {kandang['mortalitas']} Ekor
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 6. TOMBOL RESET
    st.divider()
