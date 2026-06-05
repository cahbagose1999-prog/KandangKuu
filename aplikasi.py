import streamlit as st
import pandas as pd
from datetime import datetime

# =====================================================================
# 1. PROTEKSI UTAMA & STYLING NAVIGASI BAWAH PERSIS SEPERTI GAMBAR
# =====================================================================
st.markdown("""
<html lang='en' translate='no'><head><meta name='google' content='notranslate'></head></html>
<style>
    /* Mengunci ukuran layar rapat pas seperti aplikasi HP asli di gambar */
    .block-container {
        padding-top: 10px !important;
        padding-bottom: 80px !important; /* Ganjal bawah agar tidak tertutup menu */
        padding-left: 14px !important;
        padding-right: 14px !important;
        max-width: 460px !important; 
        margin: 0 auto;
    }
    /* Mengatur gaya kartu melengkung halus warna putih seperti di gambar */
    .kartu-putih {
        background-color: #FFFFFF;
        padding: 16px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        margin-bottom: 14px;
    }
    h2, h3, h4, h5 {
        color: #0F172A !important;
        font-family: 'Inter', sans-serif;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Kandangku Dashboard", page_icon="🐔")

# =====================================================================
# 2. DATABASE SIMULASI PATEN (MEMORI BROWSER HP)
# =====================================================================
if "halaman_aktif" not in st.session_state: st.session_state.halaman_aktif = "LOGIN"
if "nama_peternak" not in st.session_state: st.session_state.nama_peternak = ""
if "lokasi_peternak" not in st.session_state: st.session_state.lokasi_peternak = ""
if "jenis_unggas" not in st.session_state: st.session_state.jenis_unggas = ""
if "status_bisnis" not in st.session_state: st.session_state.status_bisnis = ""

# Sistem Pemicu Navigasi Bawah Gambar Baru
if "menu_bawah_aktif" not in st.session_state: st.session_state.menu_bawah_aktif = "Dashboard"

# Memori Data Logistik & Finansial
if "stok_pakan" not in st.session_state: st.session_state.stok_pakan = 450.0  # Kg
if "saldo_kas" not in st.session_state: st.session_state.saldo_kas = 5000000  # Rp
if "telur_gudang" not in st.session_state: st.session_state.telur_gudang = 0  # Butir

# Status Checklist Tugas Hari Ini (Dinamis)
if "tugas_pakan_done" not in st.session_state: st.session_state.tugas_pakan_done = False
if "tugas_telur_done" not in st.session_state: st.session_state.tugas_telur_done = False
if "tugas_minum_done" not in st.session_state: st.session_state.tugas_minum_done = False
if "tugas_bersih_done" not in st.session_state: st.session_state.tugas_bersih_done = False

# Database Buku Riwayat Paten Pengisi Data AI
if "jurnal_riwayat" not in st.session_state:
    st.session_state.jurnal_riwayat = [
        {"Tanggal": "2026-06-04", "Pakan (Kg)": 20.0, "Ayam Mati": 0, "Panen Telur": 150},
        {"Tanggal": "2026-06-05", "Pakan (Kg)": 20.0, "Ayam Mati": 1, "Panen Telur": 145}
    ]

# Daftar Kandang Aktif
if "daftar_kandang" not in st.session_state:
    st.session_state.daftar_kandang = [
        {"nama": "Kandang Blok A", "tipe": "Ayam KUB Pembesaran", "populasi": 170, "mortalitas": 0},
        {"nama": "Kandang Blok B", "tipe": "Ayam KUB Petelur", "populasi": 150, "mortalitas": 0},
        {"nama": "Kandang Blok C", "tipe": "Ayam KUB Indukan", "populasi": 100, "mortalitas": 0}
    ]

# =====================================================================
# HALAMAN SIKLUS 1 & 2: LOGIN DAN SETUP BIODATA
# =====================================================================
if st.session_state.halaman_aktif == "LOGIN":
    st.markdown("<h2 style='text-align: center; color: #1E293B;'>🐔 KANDANGKU</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray; font-size:14px; margin-top:0;'>Asisten Peternakan Unggas Berbasis AI & IoT</p>", unsafe_allow_html=True)
    st.write("")
    if st.button("Masuk Cepat Ke Dashboard Aplikasi ➡️", use_container_width=True):
        st.session_state.halaman_aktif = "PROFIL"
        st.rerun()

elif st.session_state.halaman_aktif == "PROFIL":
    st.markdown("<h3>👤 Setup Awal Akun</h3>", unsafe_allow_html=True)
    nama_input = st.text_input("Nama Lengkap Pemilik:", placeholder="Contoh: Pak Budi")
    kabupaten_input = st.text_input("Kabupaten / Kota:", placeholder="Contoh: Cirebon")
    kecamatan_input = st.text_input("Kecamatan Kandang:", placeholder="Contoh: Kesambi")
    unggas_input = st.selectbox("Komoditas Unggas Utama:", ["Ayam Kampung Unggul (Ayam KUB)", "Ayam Broiler", "Ayam Layer Ras", "Bebek"])
    status_bisnis_input = st.radio("Sistem Operasional:", ["Peternak Mandiri", "Peternak Kemitraan"])
    
    if st.button("Buka Dashboard Utama 🔓", use_container_width=True):
        if not nama_input or not kabupaten_input or not kecamatan_input:
            st.error("⚠️ Kolom pendaftaran wajib diisi!")
        else:
            st.session_state.nama_peternak = nama_input
            st.session_state.lokasi_peternak = f"{kecamatan_input}, {kabupaten_input}"
            st.session_state.jenis_unggas = unggas_input
            st.session_state.status_bisnis = status_bisnis_input
            st.session_state.halaman_aktif = "APLIKASI_UTAMA"
            st.rerun()

# =====================================================================
# HALAMAN SIKLUS 3: EKSEKUSI SATU LAYAR UTAMA (5 NAVIGASI BAWAH ASLI)
# =====================================================================
elif st.session_state.halaman_aktif == "APLIKASI_UTAMA":
    
    # -----------------------------------------------------------------
    # MENU BAWAH 1: DASHBOARD (REPLIKA PERSIS GAMBAR ANDA)
    # -----------------------------------------------------------------
    if st.session_state.menu_bawah_aktif == "Dashboard":
        st.markdown("<small style='color:gray; font-weight:bold; letter-spacing:1px;'>KANDANGKU</small>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-top:0px; margin-bottom:15px;'>Dashboard</h2>", unsafe_allow_html=True)
        
        # Sektor Kotak 1: Tugas Hari Ini (Persis Gambar Referensi)
        st.markdown("#### Tugas Hari Ini")
        with st.container(border=True):
            # Logika hitung penyelesaian tugas
            tugas_list = [st.session_state.tugas_pakan_done, st.session_state.tugas_telur_done, st.session_state.tugas_minum_done, st.session_state.tugas_bersih_done]
            selesai = sum(1 for t in tugas_list if t)
            st.markdown(f"<div style='text-align:right; color:gray; font-size:13px; margin-bottom:5px;'>{selesai}/4 selesai</div>", unsafe_allow_html=True)
            
            # Checkbox 1: Beri Pakan Pagi (Memotong gudang & kas uang otomatis)
            total_populasi = sum(k['populasi'] for k in st.session_state.daftar_kandang)
            pakan_hari_ini = total_populasi * 0.1
            biaya_pakan = pakan_hari_ini * 8500
            
            cek_pakan = st.checkbox(f"Beri pakan pagi ({pakan_hari_ini:.1f} Kg)", value=st.session_state.tugas_pakan_done)
            if cek_pakan and not st.session_state.tugas_pakan_done:
                st.session_state.stok_pakan -= pakan_hari_ini
                st.session_state.saldo_kas -= biaya_pakan
                st.session_state.tugas_pakan_done = True
                st.rerun()
            elif not cek_pakan and st.session_state.tugas_pakan_done:
                st.session_state.stok_pakan += pakan_hari_ini
                st.session_state.saldo_kas += biaya_pakan
                st.session_state.tugas_pakan_done = False
                st.rerun()
                
            # Checkbox 2: Ambil Telur Kandang A
            cek_telur = st.checkbox("Ambil telur kandang A", value=st.session_state.tugas_telur_done)
            if cek_telur and not st.session_state.tugas_telur_done:
                st.session_state.telur_gudang += 120  # Otomatis masuk inventaris
                st.session_state.tugas_telur_done = True
                st.success("🥚 120 Butir telur sukses masuk ke menu Inventaris Gudang!")
                st.rerun()
            elif not cek_telur and st.session_state.tugas_telur_done:
                st.session_state.telur_gudang -= 120
                st.session_state.tugas_telur_done = False
                st.rerun()
                
            # Checkbox 3 & 4: Catatan Rutin Lapangan
            st.session_state.tugas_minum_done = st.checkbox("Cek air minum", value=st.session_state.tugas_minum_done)
            st.session_state.tugas_bersih_done = st.checkbox("Bersihkan kandang B", value=st.session_state.tugas_bersih_done)

        # Sektor Kotak 2: Ringkasan Peternakan (Persis Gambar Kanan-Kiri)
        st.markdown("<br>#### Ringkasan Peternakan", unsafe_allow_html=True)
        
        col_rg1, col_rg2 = st.columns(2)
        with col_rg1:
            st.markdown(f"<div style='background-color:#E8F5E9; padding:14px; border-radius:14px; border:1px solid #C8E6C9;'>🟢 <b>Total Kandang</b><br><span style='font-size:24px; font-weight:bold; color:#2E7D32;'>{len(st.session_state.daftar_kandang)}</span><br><small style='color:gray;'>Blok Aktif</small></div>", unsafe_allow_html=True)
        with col_rg2:
            st.markdown(f"<div style='background-color:#F8FAFC; padding:14px; border-radius:14px; border:1px solid #E2E8F0;'>👤 <b>Populasi</b><br><span style='font-size:24px; font-weight:bold; color:#0F172A;'>{total_populasi}</span><br><small style='color:gray;'>Ekor Hidup</small></div>", unsafe_allow_html=True)

        # Widget Tambahan: Cuaca Lokasi & IoT Pengingat Darurat (Saran Penting Anda)
        st.markdown("<br>##### 🌤️ Kondisi Lingkungan Hari Ini", unsafe_allow_html=True)
