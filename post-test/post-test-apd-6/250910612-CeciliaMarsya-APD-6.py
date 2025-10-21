import os

akun = {
    "admin": "108",
    "guest": "801"
}
akun_tambahan = {}

paket_studio = {
    "1": {"nama": "Reguler", "durasi": 2, "harga": 75000},
    "2": {"nama": "Premium", "durasi": 4, "harga": 120000},
    "3": {"nama": "VIP", "durasi": 6, "harga": 200000},
    "4": {"nama": "Midnight", "durasi": 8, "harga": 150000},
    "5": {"nama": "Pelajar", "durasi": 2, "harga": 52500}
}


data_penyewaan = {}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM MANAJEMEN PENYEWAAN STUDIO MUSIK ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")
    pilih_awal = input("Pilih menu: ")


    if pilih_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password baru: ")

        if new_user in akun or new_user in akun_tambahan:
            print("Username sudah terdaftar! Silakan coba lagi.")
        else:
            akun_tambahan[new_user] = new_pass
            print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")
        input("\nTekan Enter untuk kembali ke menu awal...")


    elif pilih_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN SISTEM STUDIO MUSIK ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        login = False
        is_admin = False

        if username in akun and akun[username] == password:
            login = True
            if username == "admin":
                is_admin = True
        elif username in akun_tambahan and akun_tambahan[username] == password:
            login = True

        if not login:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("Login berhasil!\n")

        while login:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== MENU UTAMA ===")
            print("1. Tambah Data Penyewaan (Create)")
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

                if id_p in data_penyewaan:
                    print("ID penyewa sudah ada!")
                else:
                    nama = input("Masukkan nama penyewa: ")
                    print("\nPilih paket studio:")
                    for k, v in paket_studio.items():
                        print(f"{k}. {v['nama']} - {v['durasi']} jam - Rp{v['harga']:,}")

                    pilih_paket = input("Masukkan nomor paket: ")
                    if pilih_paket in paket_studio:
                        paket = paket_studio[pilih_paket]['nama']
                        harga = paket_studio[pilih_paket]['harga']
                    else:
                        paket = "Custom"
                        harga = 0

                    data_penyewaan[id_p] = {
                        "nama": nama,
                        "paket": paket,
                        "status": "Belum Bayar",
                        "harga": harga
                    }
                    print("\nData penyewaan berhasil ditambahkan!")
                input("Tekan Enter untuk kembali...")


            elif menu == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== DATA PENYEWAAN ===")
                if not data_penyewaan:
                    print("Belum ada data penyewaan.")
                else:
                    for id_p, info in data_penyewaan.items():
                        print(f"ID: {id_p}")
                        print(f"Nama: {info['nama']}")
                        print(f"Paket: {info['paket']}")
                        print(f"Status Pembayaran: {info['status']}")
                        print(f"Total Harga: Rp{info['harga']:,}")
                        print("-" * 35)
                    print(f"Total penyewa terdaftar: {len(data_penyewaan)}")
                input("\nTekan Enter untuk kembali...")


            elif menu == "3" and is_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== UBAH DATA PENYEWAAN ===")
                id_cari = input("Masukkan ID penyewa: ")

                if id_cari in data_penyewaan:
                    print("1. Ubah Nama")
                    print("2. Ubah Paket")
                    print("3. Ubah Status Pembayaran")
                    pilihan = input("Pilih data yang ingin diubah: ")

                    if pilihan == "1":
                        data_penyewaan[id_cari]['nama'] = input("Masukkan nama baru: ")
                    elif pilihan == "2":
                        for k, v in paket_studio.items():
                            print(f"{k}. {v['nama']} - {v['durasi']} jam - Rp{v['harga']:,}")
                        pilih_paket = input("Masukkan nomor paket: ")
                        if pilih_paket in paket_studio:
                            data_penyewaan[id_cari]['paket'] = paket_studio[pilih_paket]['nama']
                            data_penyewaan[id_cari]['harga'] = paket_studio[pilih_paket]['harga']
                    elif pilihan == "3":
                        data_penyewaan[id_cari]['status'] = input("Masukkan status baru (Belum Bayar/Lunas): ")
                    else:
                        print("Pilihan tidak valid.")
                    print("Data berhasil diubah!")
                else:
                    print("Data penyewa tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")


            elif menu == "4" and is_admin:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== HAPUS DATA PENYEWAAN ===")
                id_hapus = input("Masukkan ID penyewa: ")

                if id_hapus in data_penyewaan:
                    del data_penyewaan[id_hapus]
                    print("Data penyewa berhasil dihapus!")
                else:
                    print("Data penyewa tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")


            elif menu == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== DAFTAR PAKET STUDIO ===")
                for v in paket_studio.values():
                    print(f"{v['nama']} | Durasi: {v['durasi']} jam | Harga: Rp{v['harga']:,}")
                input("\nTekan Enter untuk kembali...")


            elif menu == "6":
                print("Anda telah logout. Terima kasih!")
                login = False
                input("Tekan Enter untuk kembali ke menu awal...")
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk kembali...")

    elif pilih_awal == "3":
        print("\nTerima kasih telah menggunakan sistem penyewaan studio musik!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")