print("=== Penghitung Gaji Karyawan PT. BOM ===")


# Input data karyawan
nama = input("Masukkan nama karyawan: ")
jabatan = input(f"Masukkan jabatan karyawan (peracik/pengantar): ")
hari_kerja = int(input("Masukkan jumlah hari kerja: "))
jam_kerja = int(input("Masukkan jumlah jam kerja per hari: "))
lembur = int(input("Masukkan jumlah lembur: "))

# Harga petasan per pcs
harga_petasan = 5000

# Inisialisasi bayaran
bayaran_per_jam = 0
bayaran_lembur = 0

# Percabangan utama berdasarkan jabatan
if jabatan == "peracik":
    if hari_kerja >= 24 and jam_kerja >= 8 and lembur >= 4:
        bayaran_per_jam = 25000
        bayaran_lembur = 15000
    elif hari_kerja >= 18 and jam_kerja >= 6 and lembur >= 2:
        bayaran_per_jam = 20000
        bayaran_lembur = 10000
    else:
        bayaran_per_jam = 15000
        bayaran_lembur = 10000

elif jabatan == "pengantar":
    if hari_kerja >= 20 and jam_kerja >= 7 and lembur >= 7:
        bayaran_per_jam = 25000
        bayaran_lembur = 20000
    elif hari_kerja >= 16 and jam_kerja >= 5 and lembur >= 4:
        bayaran_per_jam = 20000
        bayaran_lembur = 15000
    else:
        bayaran_per_jam = 15000
        bayaran_lembur = 12000

else:
    print("Jabatan tidak dikenali. Silakan masukkan 'peracik' atau 'pengantar'.")
    

# Perhitungan total gaji
total_gaji = ((bayaran_per_jam * jam_kerja) * hari_kerja) + (lembur * bayaran_lembur)

# Output hasil
print("\n<=== Rincian Gaji Karyawan ===>")
print("Nama Karyawan       :", nama)
print("Jabatan             :", jabatan.capitalize())
print("Harga Petasan/pcs   : Rp{:,.0f}".format(harga_petasan))
print("Hari Kerja          :", hari_kerja)
print("Jam Kerja per Hari  :", jam_kerja)
print("Jumlah Lembur       :", lembur)
print("Bayaran per Jam     : Rp{:,.0f}".format(bayaran_per_jam))
print("Bayaran Lembur      : Rp{:,.0f}".format(bayaran_lembur))
print("Total Gaji          : Rp{:,.0f}".format(total_gaji))
print("\n b Terima kasih telah menggunakan sistem PT. BOM")