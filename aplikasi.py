
import streamlit as st

# PROTEKSI UTAMA: Memaksa browser HP agar TIDAK merusak struktur HTML aplikasi
st.markdown("<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>", unsafe_allow_html=True)

# Konfigurasi dasar tampilan agar pas dengan layar HP
st.set_page_config(page_title="Kandangku App", page_icon="🐔", layout="centered")

# Wadah penyimpanan memori sementara di browser HP
if "halaman_aktif" not in st.session_state:
    st.session_state.halaman_aktif = "MENU_LOGIN"
if "nama_peternak" not in st.session_state:
    st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state:
    st.session_state.lokasi_peternak = ""

# ==========================================
# ALUR 1: HALAMAN LOGIN CEPAT
# ==========================================
if st.session_state.halaman_aktif == "MENU_LOGIN":
    st.markdown("<h1 style='text-align: center;'>🐔 Kandangku</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
    st.divider()
    
    st.info("💡 **Gerbang Masuk Instan:** Silakan pilih salah satu tombol di bawah untuk masuk tanpa password.")
    
    # Tombol WA Nyata
    link_wa = "https://wa.me"
    st.link_button("🟢 Masuk Cepat via WhatsApp (Buka WA Asli)", link_wa, use_container_width=True)
    
    # Tombol Google Nyata
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google (Pilih Akun HP)", link_google, use_container_width=True)
    
    st.divider()
    st.caption("⚙️ **Aksi Pengujian (Bypass):**")
    if st.button("Lanjutkan ke Pengisian Profil Peternak ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_PROFIL"
        st.rerun()

# ==========================================
# ALUR 2: INPUT PROFIL PETERNAK
# ==========================================
elif st.session_state.halaman_aktif == "MENU_PROFIL":
    st.subheader("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk konfigurasi awal.")
    
    nama_input = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    provinsi_input = st.selectbox("Provinsi Kandang Berada:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    if st.button("Simpan Data Profil & Kunci 🔒", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Semua kolom data wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}, {provinsi_input}"
            st.session_state.halaman_aktif = "MENU_SUKSES"
            st.rerun()

# ==========================================
# ALUR 3: REKAP HASIL SIMULASI
# ==========================================
elif st.session_state.halaman_aktif == "MENU_SUKSES":
    st.success(f"🎉 Registrasi Sukses! Selamat Datang, {st.session_state.nama_peternak}!")
    st.write(f"**Nama Pemilik:** {st.session_state.nama_peternak}")
    st.write(f"**Cakupan Wilayah AI:** {st.session_state.lokasi_peternak}")
    
    st.divider()
    if st.button("⬅️ Ulangi dari Halaman Login", use_container_width=True):
        st.session_state.halaman_aktif = "MENU_LOGIN"
        st.rerun()
