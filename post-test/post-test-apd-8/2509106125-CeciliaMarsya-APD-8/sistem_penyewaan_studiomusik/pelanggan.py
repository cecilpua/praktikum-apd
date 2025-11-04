import os
from prettytable import PrettyTable
from data import data_penyewa, paket_studio

def tampilkan_penyewa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DATA PENYEWA STUDIO MUSIK ===\n")

    if not data_penyewa:
        print("Belum ada data penyewa.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["ID", "Nama", "Paket", "Status Pembayaran"]

        for id_p, info in data_penyewa.items():
            tabel.add_row([id_p, info["nama"], info["paket"], info["status"]])

        print(tabel)
        print(f"\nTotal penyewa terdaftar: {len(data_penyewa)}")
    input("\nTekan Enter untuk kembali...")


def tambah_penyewa(id_penyewa, nama_penyewa):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== TAMBAH DATA PENYEWA ===\n")

    if id_penyewa in data_penyewa:
        print("ID penyewa sudah ada!")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Nama Paket", "Durasi (jam)", "Harga (Rp)"]
        for k, v in paket_studio.items():
            durasi_jam = v["durasi"] / 60
            tabel.add_row([k, v["nama"], f"{durasi_jam:.2f}", f"{v['harga']:,}"])
        print(tabel)

        pilih_paket = input("Masukkan nomor paket: ")
        if pilih_paket in paket_studio:
            paket = paket_studio[pilih_paket]["nama"]
        else:
            paket = "Custom"

        data_penyewa[id_penyewa] = {
            "nama": nama_penyewa,
            "paket": paket,
            "status": "Belum Bayar"
        }
        print("\nData penyewa berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali...")


def ubah_data(id_penyewa):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== UBAH DATA PENYEWA ===\n")

    if id_penyewa in data_penyewa:
        print("1. Ubah Nama")
        print("2. Ubah Paket")
        print("3. Ubah Status Pembayaran")
        pilihan = input("Pilih data yang ingin diubah: ")

        if pilihan == "1":
            data_penyewa[id_penyewa]['nama'] = input("Masukkan nama baru: ")
        elif pilihan == "2":
            tabel = PrettyTable()
            tabel.field_names = ["No", "Nama Paket", "Durasi (jam)", "Harga (Rp)"]
            for k, v in paket_studio.items():
                durasi_jam = v["durasi"] / 60
                tabel.add_row([k, v["nama"], f"{durasi_jam:.2f}", f"{v['harga']:,}"])
            print(tabel)
            pilih_paket = input("Masukkan nomor paket: ")
            if pilih_paket in paket_studio:
                data_penyewa[id_penyewa]['paket'] = paket_studio[pilih_paket]['nama']
        elif pilihan == "3":
            data_penyewa[id_penyewa]['status'] = input("Masukkan status baru (Belum Bayar/Lunas): ")
        else:
            print("Pilihan tidak valid.")
        print("\nData berhasil diubah!")
    else:
        print("Data penyewa tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")

