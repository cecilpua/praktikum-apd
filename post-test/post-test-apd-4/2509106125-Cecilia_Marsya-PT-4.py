# Input stamina dari 3 digit NIM terakhir
stamina = int(input("Masukkan stamina (3 digit terakhir NIM): "))
chakra = 0

# Proses pengumpulan chakra
while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

# Output hasil
print(f"Chakra yang berhasil dikumpulkan: {chakra}")
print(f"Sisa stamina: {stamina}")

if chakra >= 200:
    print("Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra.")

# Input tinggi menara dari 2 digit terakhir NIM
tinggi_menara = int(input("Masukkan tinggi menara (2 digit terakhir NIM): "))
gulungan = 0

# Proses pengumpulan gulungan
for ketinggian in range(3, tinggi_menara + 1, 3):
    gulungan += 1

# Output hasil
print(f"Gulungan informasi yang didapatkan: {gulungan}")

# Input jumlah koridor dari digit kedua terakhir NIM
jumlah_koridor = int(input("Masukkan jumlah koridor (digit kedua terakhir NIM): "))
intelijen = 0
perangkap = 0

# Proses penyelidikan
for koridor in range(1, jumlah_koridor + 1):
    for ruangan in range(1, 4):  # Setiap koridor memiliki 3 ruangan
        nomor_ruangan = (koridor - 1) * 3 + ruangan
        if nomor_ruangan % 2 == 1:
            intelijen += 1
        else:
            perangkap += 1

# Output hasil
print(f"Data Intelijen yang didapatkan: {intelijen}")
print(f"Perangkap Peledak yang berhasil dijinakkan: {perangkap}")
