# Program Kalkulator Biaya Bahan Bangunan
# Dibuat untuk membantu menghitung estimasi biaya pembelian batu bata dan semen dengan skema diskon.

# --- Data Harga Dasar ---
harga_batu_bata = 100
harga_semen = 100000

# --- Input Pengguna ---
print("==========================================")
print("     KALKULATOR BIAYA BAHAN BANGUNAN")
print("==========================================")

nama_pelanggan = input("Masukkan nama Pelanggan: ")
jumlah_batu_bata = int(input("Masukkan jumlah batu: "))
jumlah_semen = int(input("Masukkan jumlah karung semen: "))


total_biaya_awal = (jumlah_batu_bata * harga_batu_bata) + (jumlah_semen * harga_semen)

# Tentukan logika diskon
diskon_persentase = 0.0
keterangan_diskon = "Tidak Ada Diskon"

is_paket_ultra_mantap = jumlah_batu_bata == 2000 and jumlah_semen == 16
is_paket_hemat = jumlah_batu_bata == 500 and jumlah_semen == 5

if is_paket_ultra_mantap:
    diskon_persentase = 0.30  # 30%
    keterangan_diskon = "Paket Ultra Mantap (30%)"
elif is_paket_hemat:
    diskon_persentase = 0.15  # 15%
    keterangan_diskon = "Paket Hemat (15%)"


jumlah_diskon = total_biaya_awal * diskon_persentase
total_biaya_akhir = total_biaya_awal - jumlah_diskon

# --- Output Ringkasan Pesanan ---
print("\n" + "="*42)  
print("         RINGKASAN PEMBELIAN PAK ZULFIKAR")
print("="*42)
print(f"Nama Pelanggan: {nama_pelanggan}")
print("-" * 42)
print(f"{'| Barang':<12} | {'Jumlah':<8} | {'Harga Satuan':<15} |")
print("-" * 42)
print(f"| {'Batu Bata':<10}  | {jumlah_batu_bata:<8} | {(harga_batu_bata):<15} |")
print(f"| {'Semen':<10} | {jumlah_semen:<8} | {(harga_semen):<15} |")
print("-" * 42)
print(f"Total Biaya Awal{'':.<22}: {(total_biaya_awal)}")
print(f"Diskon yang Didapat{'':.<21}: {keterangan_diskon}")
print(f"Jumlah Diskon{'':.<27}: {(jumlah_diskon)}")
print("-" * 42)
print(f"TOTAL BIAYA AKHIR{'':.<22}: {(total_biaya_akhir)}")
print("="*42)