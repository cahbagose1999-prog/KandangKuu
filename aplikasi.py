import streamlit as st

# Konfigurasi halaman agar pas di layar HP
st.set_page_config(page_title="Kandangku - Blueprint", page_icon="🐔", layout="centered")

st.markdown("<h1 style='text-align: center;'>🐔 Kandangku</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Asisten Pintar Peternakan Ayam KUB & Unggas</p>", unsafe_allow_html=True)
st.divider()

# Navigasi Menggunakan Menu Pilihan yang Aman dari Error Rerun
menu_halaman = st.sidebar.radio("🧭 Navigasi Alur Halaman:", ["1. Halaman Login", "2. Pengisian Profil Peternak", "3. Rekap Validasi Sistem"])

# ==========================================
# SELEKSI MENU 1: HALAMAN LOGIN
# ==========================================
if menu_halaman == "1. Halaman Login":
    st.info("💡 **Gerbang Masuk Instan:** Silakan pilih salah satu tombol integrasi asli di bawah untuk masuk ke sistem tanpa mengetik password.")
    
    # 🟢 Integrasi WhatsApp Asli
    nomor_wa_server = "628123456789" 
    pesan_otomatis = "Halo Admin Kandangku, saya ingin verifikasi masuk ke akun peternak saya."
    link_wa = f"https://wa.me{nomor_wa_server}?text={pesan_otomatis.replace(' ', '%20')}"
    st.link_button("🟢 Masuk Cepat via WhatsApp (Buka WA Asli)", link_wa, use_container_width=True)
    
    # 🔴 Integrasi Google Login Asli
    link_google = "https://google.com"
    st.link_button("🔴 Masuk Cepat via Akun Google (Pilih Akun HP)", link_google, use_container_width=True)
    
    st.divider()
    st.warning("👉 **Langkah Pengujian:** Setelah mengetuk tombol login di atas, silakan buka menu di samping kiri (buka sidebar HP Anda) lalu pindah ke menu **'2. Pengisian Profil Peternak'**.")

# ==========================================
# SELEKSI MENU 2: PROFIL PEMILIK PETERNAK
# ==========================================
elif menu_halaman == "2. Pengisian Profil Peternak":
    st.subheader("👤 Profil Pemilik Peternakan")
    st.write("Silakan lengkapi data diri Anda untuk personalisasi sistem AI.")
    
    nama = st.text_input("Nama Lengkap Peternak:", placeholder="Contoh: Pak Budi")
    
    st.markdown("##### 📍 Wilayah Cakupan Kandang (Akurasi Prediksi Cuaca AI)")
    provinsi = st.selectbox("Provinsi:", ["Jawa Barat", "Jawa Tengah", "Jawa Timur", "Luar Jawa"])
    kabupaten = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan = st.text_input("Kecamatan:", placeholder="Contoh: Kesambi")
    
    st.divider()
    status_bisnis = st.radio("Sistem Tata Kelola Bisnis Peternakan Anda:", ["Peternak Mandiri", "Peternak Kemitraan"])
    
    st.divider()
    if st.button("Simpan Data Profil & Kunci 🔒", use_container_width=True):
        if not nama or not kabupaten or not kecamatan:
            st.error("⚠️ Semua kolom wajib diisi agar sistem AI tidak salah membaca data!")
        else:
            st.success("🎉 Data berhasil disimpan di memori sistem! Silakan pindah ke menu **'3. Rekap Validasi Sistem'** di panel samping untuk melihat hasilnya.")

# ==========================================
# SELEKSI MENU 3: REKAP DATA & EVALUASI
# ==========================================
elif menu_halaman == "3. Rekap Validasi Sistem":
    st.subheader("🔍 Hasil Validasi Data Awal")
    st.info("Pemberitahuan Sistem: Hak akses penuh diberikan ke akun ini (Semua Fitur Terbuka).")
    st.write("Gunakan halaman pendaftaran awal ini sebagai fondasi blueprint kita sebelum membuat menu tambah kandang.")
