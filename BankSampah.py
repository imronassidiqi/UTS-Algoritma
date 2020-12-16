import getpass
import os
def admin():
    os.system("clear")
    hello = ("-Silahkan Masukan Akun admin Anda-")
    print(hello)
    user = input ("Username : ")
    passw = getpass.getpass(prompt="Password : ")
    password = {"imonassidiqi"}
    if passw in password:
        print("*selamat " + user + ", Anda berhasil Login Sebagai Admin")
    else:
        print("*Username dan Password yang anda masukkan salah")
def harga():
    Nasabah = input ("Masukkan Nama Anda : ")
    hello1 = ("-Silahkan Isi kolom berikut ini-")
    print(hello1)
    user1 = input ("Username : ")
    berat_sampah = int(input("Masukkan berat sampah anda : "))
    menu = 1
    while menu !=0:
        print ()
        print(" pilih jenis sampah")
        print(" 1. Sampah plastik ")
        print(" 2. Sampah kertas") 
        print(" 3. Sampah kaleng")
        print(" 0. exit")
        menu = int(input("Masukkan jenis sampah : "))
        if menu == 1:
            harga_sampah = berat_sampah * 2000
            print()
            print("Harga Sampah: ",harga_sampah)
            print()
        elif menu == 2:
            harga_sampah = berat_sampah * 1500
            print()
            print("Harga sampah: ",harga_sampah)
            print()
        elif menu == 3:
            harga_sampah = berat_sampah * 3000
            print()
            print("Harga sampah: ",harga_sampah)
            print()
        elif menu == 0:
            print("keluar")
        
pilihan = 1
while pilihan !=0:
    print()
    print("---Menu Bank Sampah---")
    print("1. Login Sebagai Admin")
    print("2. Nasabah ")
    print("0. exit")
    print()
    pilihan = int(input("Masukkan Nomor Menu: "))
    if pilihan == 1:
        admin()
        print("Harga Sampah Plastik : 2000")
        print("Harga Sampah Kertas : 1500")
        print("Harga Sampah Kaleng : 3000")
    elif pilihan == 2:
        print("Harga Sampah Plastik : 2000")
        print("Harga Sampah Kertas : 1500")
        print("Harga Sampah Kaleng : 3000")
        harga()
        print("--Terimakasih--")
    elif pilihan == 0:
        print("---Terimakasih telah menggunakan Layanan Bank Sampah---")
