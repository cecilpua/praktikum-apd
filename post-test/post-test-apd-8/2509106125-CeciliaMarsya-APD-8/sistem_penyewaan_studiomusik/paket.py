import os
from prettytable import PrettyTable
from data import paket_studio

def tampilkan_paket_studio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== DAFTAR PAKET STUDIO MUSIK ===\n")
    
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Paket", "Durasi (menit)", "Harga (Rp)"]
    
    for k, v in paket_studio.items():
        tabel.add_row([k, v["nama"], v["durasi"], f"{v['harga']:,}"])
    
    print(tabel)
    input("\nTekan Enter untuk kembali...")