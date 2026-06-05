import streamlit as st

# Konfigurasi dasar halaman HP
st.set_page_config(page_title="Kandangku - Gerbang Utama", page_icon="🐔")

st.title("🐔 Kandangku")
st.caption("Asisten Pintar Peternakan Ayam KUB & Unggas")
st.divider()

# Wadah Memori Sementara Aplikasi
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"

# ==========================================
# SELEKSI ALUR 1: MENU LOGIN CEPAT
# ==========================================
if st.session_state.halaman_aktif == "MENU_LOGIN":
    st.info("💡 **Gerbang Masuk Instan:** Silakan pilih salah satu tombol integrasi asli di bawah untuk masuk ke sistem tanpa mengetik password.")
    
    # 🟢 Link Tombol WhatsApp Nyata
    link_wa = "https://wa.me"
    st.link_button("🟢 Masuk Cepat via WhatsApp (Buka WA Asli)", link_wa, use_container_width=True)
    
    # 🔴 Link Tombol Google Nyata
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google (Pilih Akun HP)", link_google, use_container_width=True)
    
    st.divider()
    st.warning("👉 **Langkah Simulasi:** Setelah mencoba tombol di atas, kembali ke browser ini dan ketuk tombol di bawah untuk lanjut mengisi biodata.")
    
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.experimental_rerun()

# ==========================================
# SELEKSI ALUR 2: INPUT PROFIL PETERNAK
# ==========================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.subheader("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk personalisasi sistem AI.")
    
    nama_input = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("##### 📍 Wilayah Cakupan Kandang (Akurasi Prediksi Cuaca AI)")
    provinsi_input = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    status_bisnis_input = st.radio("Sistem Tata Kelola Bisnis Peternakan Anda:", ["Peternak Mandiri", "Peternak Kemitraan"])
    
    st.divider()
    if st.button("Simpan Data Profil & Kunci 🔒", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Semua kolom wajib diisi agar sistem AI tidak salah membaca data!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}, {provinsi_input}"
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "MENU_REKAP"
            st.experimental_rerun()

# ==========================================
# SELEKSI ALUR 3: REKAP VALIDASI DATA
# ==========================================
elif st.session_state.halaman_aktif == "MENU_REKAP":
    st.success(f"🎉 Pendaftaran Berhasil! Selamat Datang, {st.session_state.nama_peternak}!")
    st.write(f"**Identitas Pemilik:** {st.session_state.nama_peternak}")
    st.write(f"**Lokasi Sensor Cuaca AI:** {st.session_state.lokasi_peternak}")
    st.write(f"**Model Operasional:** {st.session_state.status_bisnis}")
    st.info("Pemberitahuan Sistem: Hak akses penuh diberikan ke akun ini.")
    
    st.divider()
    if st.button("⬅️ Reset & Ulangi Simulasi Login", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_LOGIN"
        st.experimental_rerun()
