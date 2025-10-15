import os

admin_user = "admin"
admin_pass = "108"
guest_user = "guest"
guest_pass = "801"

akun_tambahan = []


paket_studio = [
    ["Reguler", 2, 75000],
    ["Premium", 4, 120000],
    ["VIP", 6, 200000],
    ["Midnight", 8, 150000],
    ["Pelajar", 2, 52500]
]


data_penyewaan = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM PENYEWAAN STUDIO MUSIK ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")

    pilih_awal = input("Pilih menu: ")

    if pilih_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password baru: ")

        duplikat = False
        if new_user == admin_user or new_user == guest_user:
            duplikat = True
        for a in akun_tambahan:
            if a[0] == new_user:
                duplikat = True

        if duplikat:
            print("Username sudah terdaftar! Silakan coba lagi.")
        else:
            akun_tambahan.append([new_user, new_pass])
            print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")

        input("\nTekan Enter untuk kembali ke menu awal...")

    elif pilih_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN SISTEM STUDIO MUSIK ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        login = False
        is_admin = False

        if username == admin_user and password == admin_pass:
            login = True
            is_admin = True
        elif username == guest_user and password == guest_pass:
            login = True
        else:
            for a in akun_tambahan:
                if username == a[0] and password == a[1]:
                    login = True
                    break

        if not login:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("Login berhasil!\n")

        while login:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== MENU UTAMA ===")
            print("1. Tambah Penyewaan (Create)")
            print("2. Lihat Data Penyewaan (Read)")
            if is_admin:
                print("3. Ubah Data Penyewaan (Update)")
                print("4. Hapus Data Penyewaan (Delete)")
            print("5. Lihat Daftar Paket Studio")
            print("6. Logout")

            menu = input("Pilih menu: ")

            if menu == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== TAMBAH DATA PENYEWAAN ===")
                id_p = input("Masukkan ID penyewa: ")
                nama = input("Masukkan nama penyewa: ")

                print("\nPilih paket studio:")
                for i, p in enumerate(paket_studio):
                    print(f"{i+1}. {p[0]} - {p[1]} jam - Rp{p[2]:,}")

                pilih_paket = input("Masukkan nomor paket: ")
                if pilih_paket.isdigit() and 1 <= int(pilih_paket) <= len(paket_studio):
                    paket = paket_studio[int(pilih_paket)-1][0]
                    harga = paket_studio[int(pilih_paket)-1][2]
                else:
                    print("Pilihan tidak valid, paket diatur ke 'Custom'")
                    paket = "Custom"
                    harga = 0

                status = "Belum Bayar"
                data_penyewaan.append([id_p, nama, paket, status, harga])
                print("\nData penyewaan berhasil ditambahkan!")
                input("Tekan Enter untuk kembali...")

            elif menu == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== DATA PENYEWAAN STUDIO ===")
                if len(data_penyewaan) == 0:
                    print("Belum ada data penyewaan.")
                else:
                    for p in data_penyewaan:
                        print(f"ID: {p[0]}")
                        print(f"Nama: {p[1]}")
                        print(f"Paket: {p[2]}")
                        print(f"Status Pembayaran: {p[3]}")
                        print(f"Total Harga: Rp{p[4]:,}")
                        print("-" * 35)
                    print(f"Total penyewa terdaftar: {len(data_penyewaan)}")
                input("\nTekan Enter untuk kembali...")

            elif menu == "3" and is_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== UBAH DATA PENYEWAAN ===")
                id_cari = input("Masukkan ID penyewa yang ingin diubah: ")
                ketemu = False
                for p in data_penyewaan:
                    if p[0] == id_cari:
                        ketemu = True
                        print("\nData ditemukan!")
                        print("1. Ubah nama")
                        print("2. Ubah paket")
                        print("3. Ubah status pembayaran")
                        pilihan = input("Pilih data yang ingin diubah: ")

                        if pilihan == "1":
                            p[1] = input("Masukkan nama baru: ")
                        elif pilihan == "2":
                            print("\nPilih paket baru:")
                            for i, x in enumerate(paket_studio):
                                print(f"{i+1}. {x[0]} - {x[1]} jam - Rp{x[2]:,}")
                            pilih_paket = input("Masukkan nomor paket: ")
                            if pilih_paket.isdigit() and 1 <= int(pilih_paket) <= len(paket_studio):
                                p[2] = paket_studio[int(pilih_paket)-1][0]
                                p[4] = paket_studio[int(pilih_paket)-1][2]
                            else:
                                print("Pilihan tidak valid, tidak ada perubahan paket.")
                        elif pilihan == "3":
                            p[3] = input("Masukkan status baru (Belum Bayar / Lunas): ")
                        else:
                            print("Pilihan tidak valid.")

                        print("\nData berhasil diubah!")
                        break

                if not ketemu:
                    print("Data dengan ID tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            elif menu == "4" and is_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== HAPUS DATA PENYEWAAN ===")
                id_hapus = input("Masukkan ID penyewa yang ingin dihapus: ")
                ketemu = False
                for p in data_penyewaan:
                    if p[0] == id_hapus:
                        ketemu = True
                        data_penyewaan.remove(p)
                        print("Data penyewaan berhasil dihapus!")
                        break
                if not ketemu:
                    print("Data dengan ID tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            elif menu == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== DAFTAR PAKET STUDIO MUSIK ===")
                for p in paket_studio:
                    print(f"{p[0]} | Durasi: {p[1]} jam | Harga: Rp{p[2]:,}")
                input("\nTekan Enter untuk kembali...")

            elif menu == "6":
                print("\nAnda telah logout. Terima kasih!")
                login = False
                input("Tekan Enter untuk kembali ke menu awal...")
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk kembali...")

    elif pilih_awal == "3":
        print("\nTerima kasih telah menggunakan sistem penyewaan studio musik!")
        print("Sampai jumpa ")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")