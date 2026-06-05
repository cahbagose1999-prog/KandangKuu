import streamlit as st

# PROTEKSI LEVEL TINGGI AGAR BROWSER HP TIDAK MENERJEMAHKAN OTOMATIS (PENYEBAB ERROR)
st.markdown("<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>", unsafe_allow_html=True)

# Konfigurasi dasar layar HP
st.set_page_config(page_title="Kandangku App", page_icon="🐔", layout="centered")

# =====================================================================
# INISIALISASI DATABASE SEMENTARA (MEMORI HP)
# =====================================================================
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""
if "status_bisnis" not in st.session_state:
    st.session_state.status_bisnis = ""
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"nama": "Kandang KUB Blok A", "tipe": "Ayam KUB Pembesaran (Daging)", "umur": 45, "populasi": 500},
        {"nama": "Kandang KUB Blok B", "tipe": "Ayam KUB Petelur Konsumsi", "umur": 120, "populasi": 300}
    ]

# =====================================================================
# FUNGSI HALAMAN 1: LOGIN CEPAT
# =====================================================================
def tampilkan_halaman_login():
    st.markdown("<h1 style='text-align: center;'>🐔 Kandangku</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.divider()
    
    st.info("💡 **Gerbang Masuk Instan:** Silakan pilih salah satu tombol masuk asli di bawah untuk terhubung tanpa password.")
    
    # Tombol WA Nyata
    link_wa = "https://wa.me"
    st.link_button("🟢 Masuk Cepat via WhatsApp (Buka WA Asli)", link_wa, use_container_width=True)
    
    # Tombol Google Nyata
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google (Pilih Akun HP)", link_google, use_container_width=True)
    
    st.divider()
    st.caption("⚙️ **Langkah Pengujian Blueprint:**")
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "PROFIL"
        st.rerun()

# =====================================================================
# FUNGSI HALAMAN 2: PROFIL PETERNAK
# =====================================================================
def tampilkan_halaman_profil():
    st.subheader("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk konfigurasi sistem AI.")
    
    nama_input = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("##### 📍 Wilayah Cakupan Kandang (Untuk Cuaca AI)")
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    status_bisnis_input = st.radio(
        "Sistem Tata Kelola Bisnis:", 
        ["Peternak Mandiri (Bebas/Kelola Sendiri)", "Peternak Kemitraan (Ikut SOP Perusahaan/PT)"]
    )
    
    st.divider()
    if st.button("Simpan Data Profil & Kunci 🔒", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Semua kolom lokasi wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}, {provinsi_input}"
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "MULTI_KANDANG"
            st.rerun()

# =====================================================================
# FUNGSI HALAMAN 3: MULTI KANDANG
# =====================================================================
def tampilkan_halaman_multi_kandang():
    st.subheader(f"👋 Selamat Datang, {st.session_state.nama_peternak}!")
    st.caption(f"📍 {st.session_state.lokasi_peternak} | {st.session_state.status_bisnis}")
    st.divider()
    
    st.markdown("### 🗂️ Daftar Kandang Anda")
    
    # Menampilkan daftar kandang
    for idx, kandang in enumerate(st.session_state.daftar_kandang):
        with st.container(border=True):
            st.markdown(f"#### 🛖 {kandang['nama']}")
            st.write(f"🧬 **Tipe:** {kandang['tipe']}")
            st.write(f"📅 **Umur:** {kandang['umur']} Hari | 📊 **Populasi:** {kandang['populasi']} Ekor")
            
            if st.button("Buka Dashboard Kandang", key=f"kndg_{idx}", use_container_width=True):
                st.info(f"Berhasil memicu dashboard harian untuk {kandang['nama']}!")
                
    st.divider()
    
    # Formulir Tambah Kandang KUB
    st.markdown("### ➕ Tambah Bangunan Kandang Baru")
    with st.form("form_baru"):
        nama_kand = st.text_input("Nama/Kode Kandang Baru:", placeholder="Contoh: Kandang Blok C")
        tipe_kand = st.selectbox(
            "Kategori Ayam KUB:",
            ["Ayam KUB Indukan (Breeder)", "Ayam KUB Pembesaran (Daging)", "Ayam KUB Petelur Konsumsi"]
        )
        pop_kand = st.number_input("Populasi Awal (Ekor):", min_value=1, value=100)
        umur_kand = st.number_input("Umur Awal (Hari):", min_value=0, value=0)
        
        tombol_submit = st.form_submit_button("Daftarkan Kandang", use_container_width=True)
        
        if tombol_submit:
            if not nama_kand:
                st.error("⚠️ Nama kandang tidak boleh kosong!")
            else:
                st.session_state.daftar_kandang.append({
                    "nama": nama_kand,
                    "tipe": tipe_kand,
                    "umur": umur_kand,
                    "populasi": pop_kand
                })
                st.success(f"🎉 {nama_kand} berhasil ditambahkan!")
                st.rerun()

    st.divider()
    if st.button("⬅️ Keluar ke Halaman Login", use_container_width=True):
        st.session_state.halaman_aktif = "LOGIN"
        st.rerun()

# =====================================================================
# LOGIKA UTAMA (PENGATUR NAVIGASI)
# =====================================================================
if st.session_state.halaman_aktif == "LOGIN":
    tampilkan_halaman_login()
elif st.session_state.halaman_aktif == "PROFIL":
    tampilkan_halaman_profil()
elif st.session_state.halaman_aktif == "MULTI_KANDANG":
    tampilkan_halaman_multi_kandang()
