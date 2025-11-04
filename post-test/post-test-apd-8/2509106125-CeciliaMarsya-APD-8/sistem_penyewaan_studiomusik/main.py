import os
from datetime import datetime
from data import akun, akun_tambahan, data_pelanggan
from pelanggan import tambah_pelanggan, tampilkan_pelanggan, ubah_data
from paket import tampilkan_paket_studio
from out import konfirmasi_keluar

def main_menu(is_admin):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"=== MENU UTAMA ({'ADMIN' if is_admin else 'USER'}) ===")
        print(f"Tanggal & Waktu: {waktu}\n")
        print("1. Tambah Data Penyewa")
        print("2. Lihat Data Penyewa")
        if is_admin:
            print("3. Ubah Data Penyewa")
            print("4. Hapus Data Penyewa")
        print("5. Lihat Daftar Paket Studio Musik")
        print("6. Logout")

        menu = input("Pilih menu: ")
        if menu == "1":
            id_p = input("Masukkan ID penyewa: ")
            nama = input("Masukkan nama penyewa: ")
            tambah_pelanggan(id_p, nama)
        elif menu == "2":
            tampilkan_pelanggan()
        elif menu == "3" and is_admin:
            id_edit = input("Masukkan ID penyewa yang ingin diubah: ")
            ubah_data(id_edit)
        elif menu == "4" and is_admin:
            id_hapus = input("Masukkan ID penyewa yang ingin dihapus: ")
            if id_hapus in data_pelanggan:
                del data_pelanggan[id_hapus]
                print("\nData penyewa berhasil dihapus!")
            else:
                print("\nData tidak ditemukan.")
            input("\nTekan Enter untuk kembali...")
        elif menu == "5":
            tampilkan_paket_studio()
        elif menu == "6":
            break
        else:
            print("Menu tidak valid.")
            input("\nTekan Enter untuk kembali...")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
        print("=== SISTEM MANAJEMEN PENYEWAAN STUDIO MUSIK ===")
        print(f"Tanggal & Waktu: {waktu}\n")
        print("1. Login")
        print("2. Register Akun Baru")
        print("3. Keluar")

        pilih_awal = input("Pilih menu: ")

        if pilih_awal == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== LOGIN SISTEM STUDIO MUSIK ===\n")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            if username in akun and akun[username] == password:
                print("\nLogin berhasil sebagai admin!" if username == "admin" else "\nLogin berhasil!")
                input("Tekan Enter untuk lanjut...")
                main_menu(username == "admin")
            elif username in akun_tambahan and akun_tambahan[username] == password:
                print("\nLogin berhasil!")
                input("Tekan Enter untuk lanjut...")
                main_menu(False)
            else:
                print("\nLogin gagal! Username atau password salah.")
                input("Tekan Enter untuk kembali...")

        elif pilih_awal == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== REGISTER AKUN BARU ===\n")
            new_user = input("Masukkan username baru: ")
            new_pass = input("Masukkan password baru: ")

            if new_user in akun or new_user in akun_tambahan:
                print("\nUsername sudah terdaftar! Silakan coba lagi.")
            else:
                akun_tambahan[new_user] = new_pass
                print("\nAkun berhasil dibuat! Silakan login menggunakan akun baru.")
            input("\nTekan Enter untuk kembali ke menu awal...")

        elif pilih_awal == "3":
            if konfirmasi_keluar():
                break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

if __name__ == "__main__":
    main()