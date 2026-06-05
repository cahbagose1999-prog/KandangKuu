import streamlit as st

# 1. PROTEKSI UTAMA DARI ERROR TERJEMAHAN OTOMATIS BROWSER HP
st.markdown("<html lang='en' translate='no'></html>", unsafe_allow_html=True)

# 2. KONFIGURASI HALAMAN AGAR NYAMAN DI LAYAR HP
st.set_page_config(page_title="Kandangku App", page_icon="🐔", layout="centered")

# Inisialisasi memori penyimpanan sementara aplikasi
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"

if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "status_bisnis" not in st.session_state:
    st.session_state.status_bisnis = ""

# Simulasi data database untuk daftar multi-kandang Ayam KUB
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"nama": "Kandang KUB Blok A", "tipe": "Ayam KUB Pembesaran (Daging)", "umur": 45, "populasi": 500},
        {"nama": "Kandang KUB Blok B", "tipe": "Ayam KUB Petelur Konsumsi", "umur": 120, "populasi": 300}
    ]

# =====================================================================
# ALUR HALAMAN 1: MENU LOGIN CEPAT
# =====================================================================
if st.session_state.halaman_aktif == "MENU_LOGIN":
    st.markdown("<h1 style='text-align: center;'>🐔 Kandangku</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.divider()
    
    st.info("💡 **Gerbang Masuk Instan:** Silakan pilih salah satu tombol integrasi asli di bawah untuk masuk ke sistem tanpa mengetik password.")
    
    # Integrasi Tautan WhatsApp Asli
    link_wa = "https://wa.me"
    st.link_button("🟢 Masuk Cepat via WhatsApp (Buka WA Asli)", link_wa, use_container_width=True)
    
    # Integrasi Tautan Google Login Asli
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google (Pilih Akun HP)", link_google, use_container_width=True)
    
    st.divider()
    st.warning("👉 **Langkah Simulasi:** Setelah mencoba salah satu tombol di atas, kembali ke halaman ini dan ketuk tombol di bawah untuk lanjut mengisi profil.")
    
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.rerun()

# =====================================================================
# ALUR HALAMAN 2: INPUT PROFIL PETERNAK
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.subheader("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk personalisasi sistem AI.")
    
    nama_input = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("##### 📍 Wilayah Cakurang Kandang (Akurasi Prediksi Cuaca AI)")
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    status_bisnis_input = st.radio(
        "Sistem Tata Kelola Bisnis Peternakan Anda:", 
        ["Peternak Mandiri (Bebas/Kelola Sendiri)", "Peternak Kemitraan (Ikut SOP Perusahaan/PT Mitra)"]
    )
    
    st.divider()
    if st.button("Simpan Data Profil & Kunci 🔒", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Semua kolom wajib diisi agar sistem AI tidak salah membaca lokasi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}, {provinsi_input}"
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "MENU_MULTI_KANDANG"
            st.rerun()

# =====================================================================
# ALUR HALAMAN 3: MENU MULTI-KANDANG (DAFTAR & TAMBAH KANDANG)
# =====================================================================
elif st.session_state.halaman_aktif == "MENU_MULTI_KANDANG":
    st.subheader(f"👋 Selamat Datang, {st.session_state.nama_peternak}!")
    st.caption(f"📍 Lokasi: {st.session_state.lokasi_peternak} | {st.session_state.status_bisnis}")
    st.divider()
    
    st.markdown("### 🗂️ Daftar Kandang Anda")
    st.write("Silakan pilih kandang yang ingin Anda kelola hari ini:")
    
    # Menampilkan daftar kandang dalam bentuk kartu list vertikal yang pas di HP
    for idx, kandang in enumerate(st.session_state.daftar_kandang):
        with st.container(border=True):
            st.markdown(f"#### 🛖 {kandang['nama']}")
            st.write(f"🧬 **Tipe Sektor:** {kandang['tipe']}")
            st.write(f"📅 **Umur Ternak:** {kandang['umur']} Hari")
            st.write(f"📊 **Populasi Aktif:** {kandang['populasi']} Ekor")
            
            # Tombol masuk ke detail harian masing-masing kandang
            if st.button(f"Masuk ke Dashboard {kandang['nama']}", key=f"btn_{idx}", use_container_width=True):
                st.info(f"Fungsi Masuk ke {kandang['nama']} berhasil dipicu! (Logika dashboard harian siap dikembangkan selanjutnya).")
    
    st.divider()
    
    # FORMULIR TAMBAH KANDANG BARU (Sesuai Kategori Ayam KUB)
    st.markdown("### ➕ Tambah Bangunan Kandang Baru")
    with st.form("form_tambah_kandang"):
        nama_kandang_baru = st.text_input("Nama / Kode Kandang Baru:", placeholder="Contoh: Kandang Blok C")
        
        tipe_kub_baru = st.selectbox(
            "Pilih Kategori Komoditas Ayam KUB:",
            [
                "Ayam KUB Indukan (Breeder - Fokus Telur Tetas Fertiil)", 
                "Ayam KUB Pembesaran (Fokus Daging/Pedaging)", 
                "Ayam KUB Petelur Konsumsi (Fokus Telur Konsumsi)"
            ]
        )
        
        populasi_baru = st.number_input("Jumlah Populasi Masuk Awal (Ekor):", min_value=1, value=100, step=10)
        umur_awal_baru = st.number_input("Umur Awal Ternak Saat Masuk (Hari):", min_value=0, value=0)
        
        # Tombol submit di dalam formulir
        submit_kandang = st.form_submit_button("Daftarkan Kandang Baru ke Sistem", use_container_width=True)
        
        if submit_kandang:
            if not nama_kandang_baru:
                st.error("⚠️ Nama kandang baru wajib diisi!")
            else:
                # Memasukkan data baru ke list memori daftar kandang
                st.session_state.daftar_kandang.append({
                    "nama": nama_kandang_baru,
                    "tipe": tipe_kub_baru,
                    "umur": umur_awal_baru,
                    "populasi": populasi_baru
                })
                st.success(f"🎉 {nama_kandang_baru} berhasil terdaftar dalam sistem!")
                st.rerun()

    st.divider()
    if st.button("⬅️ Keluar / Reset ke Halaman Login", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_LOGIN"
        st.rerun()
