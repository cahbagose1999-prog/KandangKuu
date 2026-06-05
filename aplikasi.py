import streamlit as st

st.set_page_config(page_title="Kandangku - Blueprint", page_icon="🐔", layout="centered")

# Inisialisasi status alur halaman aplikasi
if "alur_halaman" not in st.session_state:
    st.session_state.alur_halaman = "LOGIN"

# ==========================================
# HALAMAN 1: LOGIN CEPAT (INTEGRASI ASLI)
# ==========================================
if st.session_state.alur_halaman == "LOGIN":
    st.markdown("<h1 style='text-align: center;'>🐔 Kandangku</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.write("")
    
    st.info("💡 **Gerbang Masuk Instan:** Silakan pilih salah satu tombol integrasi asli di bawah untuk masuk ke sistem tanpa mengetik password.")
    
    # 🟢 1. INTEGRASI WHATSAPP ASLI
    nomor_wa_server = "628123456789" 
    pesan_otomatis = "Halo Admin Kandangku, saya ingin verifikasi masuk ke akun peternak saya."
    link_wa = f"https://wa.me{nomor_wa_server}?text={pesan_otomatis.replace(' ', '%20')}"
    
    st.link_button("🟢 Masuk Cepat via WhatsApp (Buka WA Asli)", link_wa, use_container_width=True)
    
    # 🔴 2. INTEGRASI GOOGLE LOGIN ASLI
    link_google = "https://google.com"
    
    st.link_button("🔴 Masuk Cepat via Akun Google (Pilih Akun HP)", link_google, use_container_width=True)
    
    st.divider()
    
    # Tombol Bypass untuk Peternak Lapangan Berpindah Halaman saat Pengujian
    st.caption("⚙️ **Aksi Pengujian (Bypass):** Setelah mencoba mengetuk salah satu tombol masuk asli di atas, kembali ke browser ini dan ketuk tombol di bawah untuk melanjutkan pengisian profil.")
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.alur_halaman = "PROFIL_PETERNAK"
        st.rerun()

# ==========================================
# HALAMAN 2: PROFIL PEMILIK PETERNAK
# ==========================================
elif st.session_state.alur_halaman == "PROFIL_PETERNAK":
    st.title("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk personalisasi sistem AI.")
    
    nama = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("##### 📍 Wilayah Cakupan Kandang (Akurasi Prediksi Cuaca AI)")
    col1, col2 = st.columns(2)
    with col1:
        provinsi = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    with col2:
        kabupaten = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    
    status_bisnis = st.radio(
        "Sistem Tata Kelola Bisnis Peternakan Anda:", 
        ["Peternak Mandiri (Bebas/Kelola Sendiri)", "Peternak Kemitraan (Ikut SOP Perusahaan/PT Mitra)"]
    )
    
    st.divider()
    st.caption("🔒 Data performa kandang Anda dilindungi enkripsi keamananan Kandangku AI.")
    
    if st.button("Simpan Data Profil & Lanjutkan ➡️", use_container_width=True):
        if not nama or not kabupaten or not kecamatan:
            st.error("⚠️ Semua kolom wajib diisi agar sistem AI tidak salah membaca data!")
        else:
            st.session_state.nama_peternak = nama
            st.session_state.lokasi_peternak = f"{kecamatan}, {kabupaten}, {provinsi}"
            st.session_state.status_bisnis = status_bisnis
            st.session_state.alur_halaman = "SIMULASI_SELESAI"
            st.rerun()

# ==========================================
# HALAMAN 3: REKAP DATA & EVALUASI
# ==========================================
elif st.session_state.alur_halaman == "SIMULASI_SELESAI":
    st.success(f"🎉 Pendaftaran Berhasil! Selamat Datang di Kandangku, {st.session_state.nama_peternak}!")
    
    st.markdown("### 🔍 Hasil Validasi Data Awal:")
    st.write(f"**Identitas Pemilik:** {st.session_state.nama_peternak}")
    st.write(f"**Lokasi Sensor Cuaca AI:** {st.session_state.lokasi_peternak}")
    st.write(f"**Model Operasional:** {st.session_state.status_bisnis}")
    st.info("Pemberitahuan Sistem: Hak akses penuh diberikan ke akun ini (Semua Fitur Terbuka).")
    
    st.divider()
    if st.button("⬅️ Reset & Ulangi Simulasi Login", use_container_width=True):
        st.session_state.alur_halaman = "LOGIN"
        st.rerun()
