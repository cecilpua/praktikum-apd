def konfirmasi_keluar():
    keluar = input("Yakin ingin keluar? (y/n): ").lower()
    if keluar == "y":
        print("Terima kasih telah menggunakan sistem studio musik.")
        return True
    elif keluar == "n":
        return False
    else:
        print("Input tidak valid, silakan ulangi.")
        return konfirmasi_keluar()
    