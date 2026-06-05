import streamlit as st

st.set_page_config(page_title="Kandangku - Blueprint", page_icon="🐔", layout="centered")

if "alur_halaman" not in st.session_state:
    st.session_state.alur_halaman = "LOGIN"

# --- HALAMAN 1: LOGIN CEPAT ---
if st.session_state.alur_halaman == "LOGIN":
    st.markdown("<h1 style='text-align: center;'>🐔 Kandangku</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.write("")
    st.info("💡 Selamat datang! Pilih salah satu metode di bawah untuk masuk secara instan tanpa password.")
    
    if st.button("🟢 Masuk Cepat via WhatsApp", use_container_width=True):
        st.session_state.alur_halaman = "PROFIL_PETERNAK"
        st.rerun()
    if st.button("🔴 Masuk Cepat via Akun Google", use_container_width=True):
        st.session_state.alur_halaman = "PROFIL_PETERNAK"
        st.rerun()

# --- HALAMAN 2: PROFIL PETERNAK ---
elif st.session_state.alur_halaman == "PROFIL_PETERNAK":
    st.title("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk personalisasi sistem AI.")
    nama = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("##### 📍 Wilayah Cakupan Kandang (Untuk AI Deteksi Cuaca)")
    col1, col2 = st.columns(2)
    with col1:
        provinsi = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    with col2:
        kabupaten = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    status_bisnis = st.radio("Sistem Tata Kelola Bisnis Peternakan Anda:", ["Peternak Mandiri", "Peternak Kemitraan"])
    
    if st.button("Simpan Data & Lanjutkan ➡️", use_container_width=True):
        if not nama or not kabupaten or not kecamatan:
            st.error("⚠️ Semua kolom wajib diisi!")
        else:
            st.session_state.nama_peternak = nama
            st.session_state.lokasi_peternak = f"{kecamatan}, {kabupaten}, {provinsi}"
            st.session_state.status_bisnis = status_bisnis
            st.session_state.alur_halaman = "SIMULASI_SELESAI"
            st.rerun()

# --- HALAMAN 3: PRATINJAU HASIL ---
elif st.session_state.alur_halaman == "SIMULASI_SELESAI":
    st.success(f"🎉 Pendaftaran Berhasil! Selamat Datang, {st.session_state.nama_peternak}!")
    st.write(f"**Nama Pengguna:** {st.session_state.nama_peternak}")
    st.write(f"**Lokasi Deteksi AI:** {st.session_state.lokasi_peternak}")
    st.write(f"**Model Bisnis:** {st.session_state.status_bisnis}")
    st.info("Pemberitahuan Sistem: Hak akses penuh diberikan ke akun ini.")
    if st.button("⬅️ Ulangi Simulasi", use_container_width=True):
        st.session_state.alur_halaman = "LOGIN"
        st.rerun()
