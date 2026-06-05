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
if "kandang_dipilih" not in st.session_state:
    st.session_state.kandang_dipilih = None

# Gudang Keuangan Global yang Mudah Dipahami
if "stok_pakan" not in st.session_state:
    st.session_state.stok_pakan = 500.0  # Kg
if "sisa_uang" not in st.session_state:
    st.session_state.sisa_uang = 5000000  # Rp 5.000.000

# Daftar Kandang KUB Aktif
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"id": 0, "nama": "Kandang Pembesaran (Blok A)", "tipe": "Ayam KUB Daging", "umur": 35, "populasi": 200, "mati": 0, "pakan_done": False},
        {"id": 1, "nama": "Kandang Petelur (Blok B)", "tipe": "Ayam KUB Telur", "umur": 120, "populasi": 300, "mati:0": 0, "pakan_done": False}
    ]

# =====================================================================
# HALAMAN 1: GERBANG LOGIN
# =====================================================================
if st.session_state.halaman_aktif == "LOGIN":
    st.markdown("<h2 style='text-align: center; color: #2E7D32;'>🟢 KandangKu</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; font-size:14px; margin-top:0;'>Asisten Pintar Peternakan Ayam KUB</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Masuk Cepat Ke Aplikasi ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "PROFIL"
        st.rerun()

# =====================================================================
# HALAMAN 2: BIODATA PETERNAK
# =====================================================================
elif st.session_state.halaman_aktif == "PROFIL":
    st.markdown("<h3 style='color: #2E7D32;'>👤 Selamat Datang!</h3>", unsafe_allow_html=True)
    st.write("Silakan isi nama dan lokasi Anda terlebih dahulu:")
    
    nama_input = st.text_input("Nama Anda (Pemilik):", placeholder="Contoh: Pak Budi")
    lokasi_input = st.text_input("Lokasi Kandang (Kecamatan/Kota):", placeholder="Contoh: Kesambi, Cirebon")
    
    if st.button("Buka Kandang Saya 🔓", use_container_width=True):
        if not nama_input or not lokasi_input:
            st.error("⚠️ Nama dan lokasi tidak boleh kosong!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = lokasi_input
            st.session_state.halaman_aktif = "BERANDA_KANDANG"
            st.rerun()

# =====================================================================
# HALAMAN 3: BERANDA UTAMA (DAFTAR KANDANG)
# =====================================================================
elif st.session_state.halaman_aktif == "BERANDA_KANDANG":
    st.markdown(f"<div style='background-color: #2E7D32; padding: 12px; border-radius: 12px; color: white; margin-bottom: 12px;'><h4 style='margin: 0; color: white;'>☀️ Selamat Pagi, {st.session_state.nama_peternak}!</h4><small>📍 {st.session_state.lokasi_peternak}</small></div>", unsafe_allow_html=True)
    
    # KOTAK INFO KANTONG UANG & PAKAN (BAHASA PASAR)
    st.markdown("<div style='display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 15px;'><div style='background-color: #E8F5E9; padding: 10px; border-radius: 10px; text-align: center;'><b>💰 Sisa Uang Kas</b><br><span style='color:#2E7D32; font-weight:bold;'>Rp "+f"{st.session_state.sisa_uang:,}"+"</span></div><div style='background-color: #FFF3E0; padding: 10px; border-radius: 10px; text-align: center;'><b>🌾 Stok Pakan</b><br><span style='color:#EF6C00; font-weight:bold;'>"+f"{st.session_state.stok_pakan:.1f} Kg"+"</span></div></div>", unsafe_allow_html=True)

    st.markdown("### 🛖 Pilih Kandang yang Mau Diurus:")
    st.write("Ketuk salah satu blok kandang di bawah ini untuk mengisi laporan atau melihat saran AI:")
    
    # Menampilkan daftar kandang berupa kotak besar yang mudah diklik orang awam
    for kandang in st.session_state.daftar_kandang:
        with st.container(border=True):
            st.markdown(f"#### 🛖 {kandang['nama']}")
            st.markdown(f"<p style='margin:0; font-size:13px; opacity:0.8;'>🧬 Jenis: {kandang['tipe']} | 📅 Umur: {kandang['umur']} Hari<br>📊 Jumlah Ayam: <b>{kandang['populasi']} Ekor</b></p>", unsafe_allow_html=True)
            st.write("")
            
            # Tombol klik masuk kandang
            if st.button(f"Urus {kandang['nama']} ➡️", key=f"knd_{kandang['id']}", use_container_width=True):
                st.session_state.kandang_dipilih = kandang
                st.session_state.halaman_aktif = "DETAIL_TUGAS"
                st.rerun()

    st.divider()
    if st.button("⬅️ Keluar / Ganti Akun", use_container_width=True):
        st.session_state.halaman_aktif = "LOGIN"
        st.rerun()

# =====================================================================
# HALAMAN 4: LAPORAN HARIAN & ASISTEN AI PER KANDANG (SETELAH KANDANG DIKLIK)
# =====================================================================
elif st.session_state.halaman_aktif == "DETAIL_TUGAS":
    kandang = st.session_state.kandang_dipilih
    
    st.markdown(f"### 🛖 Urus: {kandang['nama']}")
    st.caption(f"🧬 Kategori: {kandang['tipe']} | 📅 Umur: {kandang['umur']} Hari")
    
    # TOMBOL KEMBALI KE BERANDA KANDANG UTAMA
    if st.button("⬅️ Kembali ke Daftar Semua Kandang", use_container_width=True):
        st.session_state.halaman_aktif = "BERANDA_KANDANG"
        st.rerun()
        
    st.divider()

    # 🟢 SUB-MENU 1: TUGAS DAN PENCATATAN HARIAN (SANGAT MUDAH)
    st.markdown("#### 📋 Tugas & Catatan Hari Ini")
    with st.container(border=True):
        # Hitung kebutuhan pakan otomatis (0.1 kg pakan x jumlah ayam di kandang tersebut)
        kebutuhan_pakan = kandang['populasi'] * 0.1
        biaya_pakan = kebutuhan_pakan * 8500  # Rp 8.500 per Kg
        
        # Checkbox Beri Pakan
        cek_pakan = st.checkbox(f"Sudah Beri Pakan Hari Ini ({kebutuhan_pakan:.1f} Kg)", value=kandang['pakan_done'])
        
        if cek_pakan and not kandang['pakan_done']:
            st.session_state.stok_pakan -= kebutuhan_pakan
            st.session_state.sisa_uang -= biaya_pakan
            kandang['pakan_done'] = True
            st.success("✅ Terpangkas! Stok pakan berkurang & pengeluaran uang tercatat otomatis di latar belakang.")
            st.rerun()
        elif not cek_pakan and kandang['pakan_done']:
            st.session_state.stok_pakan += kebutuhan_pakan
            st.session_state.sisa_uang += biaya_pakan
            kandang['pakan_done'] = False
            st.rerun()

        st.write("")
        # Input pencatatan angka kematian oleh peternak awam
        ayam_mati_hari_ini = st.number_input("Jumlah Ayam Mati Hari Ini (Ekor):", min_value=0, value=kandang['mati'], step=1)
        if ayam_mati_hari_ini != kandang['mati']:
            kandang['populasi'] -= (ayam_mati_hari_ini - kandang['mati'])
            kandang['mati'] = ayam_mati_hari_ini
            st.success("Data kematian diperbarui!")
            st.rerun()

    # 🤖 SUB-MENU 2: ASISTEN PINTAR AI YANG MENYATU
    st.markdown("#### 🤖 Saran dari Asisten Pintar AI")
    
    # AI otomatis mendeteksi kondisi kandang spesifik ini dan langsung bicara bahasa awam
    st.markdown(f"""
    <div style='background-color: #E3F2FD; padding: 12px; border-radius: 10px; border-left: 4px solid #1565C0; color: #1565C0; font-size:14px;'>
        <b>Saran AI untuk {kandang['nama']}:</b><br>
        Halo {st.session_state.nama_peternak}, ayam KUB Anda saat ini berumur {kandang['umur']} hari. <br><br>
        💡 <b>Instruksi Hari Ini:</b> Campurkan <b>60 gram vitamin unggas</b> ke dalam bak air minum utama karena cuaca di wilayah {st.session_state.lokasi_peternak} diprediksi agak mendung sore nanti. Ini penting untuk mencegah ayam terserang stres suhu!
    </div>
    """, unsafe_allow_html=True)
