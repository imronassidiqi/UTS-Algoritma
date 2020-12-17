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
    hello1 = ("--Silahkan Isi kolom berikut ini--")
    print(hello1)
    Nasabah = input ("Masukkan Nama Lengkap Anda : ")
    user1 = input ("Username : ")
    berat_sampah = int(input("Masukkan berat sampah anda (kg) : "))
    menu = 1
    while menu !=0:
        print ()
        print(" ---pilih jenis sampah (harga sampah)---")
        print(" 1. Sampah plastik (Rp. 2000)")
        print(" 2. Sampah kertas (Rp. 1500)") 
        print(" 3. Sampah kaleng (Rp. 3000)")
        print(" 4. Sampah botol (Rp. 4500)")
        print(" 0. exit (kembali ke menu utama)")
        menu = int(input("Masukkan jenis sampah : "))
        if menu == 1:
            harga_sampah = berat_sampah * 2000
            print()
            print("Harga Sampah anda: Rp.",harga_sampah)
            print()
        elif menu == 2:
            harga_sampah = berat_sampah * 1500
            print()
            print("Harga sampah anda: Rp.",harga_sampah)
            print()
        elif menu == 3:
            harga_sampah = berat_sampah * 3000
            print()
            print("Harga sampah anda: Rp.",harga_sampah)
            print()
        elif menu == 4:
            harga_sampah = berat_sampah * 4500
            print()
            print("Harga sampah anda: Rp.",harga_sampah)
            print()
        elif menu == 0:
            print("--keluar---")
        
pilihan = 1
while pilihan !=0:
    print()
    print("=====Selamat Datang di Layanan Bank Sampah======")
    print("---Menu Bank Sampah---")
    print("1. Login Sebagai Admin")
    print("2. Masuk Sebagai Nasabah")
    print("0. exit")
    print()
    pilihan = int(input("Masukkan Nomor Menu: "))
    if pilihan == 1:
        admin()
    elif pilihan == 2:
        harga()
        print("--Terimakasih--")
    elif pilihan == 0:
        print("---Terimakasih telah menggunakan Layanan Bank Sampah---")
        print()
    else :
        print("---Pilihan Menu Yang Anda Masukkan Salah---")
        print()
