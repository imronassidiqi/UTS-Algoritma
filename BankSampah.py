#Imron Assidiqi
import getpass
import os
def menu():
    print("===Selamat Datang di Layanan Bank Sampah Terpadu===")
    print("---Menu---")
    print("1. Login Sebagai Admin")
    print("2. Register Sebagai User Nasabah Bank Sampah")
    print("3. Exit")
    menu1=int(input("Masukkan Menu Yang Anda Pilih :"))
    if menu1==1:
        os.system("clear")
        hello = ("-Silahkan Masukan Akun admin Anda-")
        print(hello)
        user = input ("Username : ")
        passw = getpass.getpass(prompt="Password : ")
        password = {"imonassidiqi"}
        if passw in password:
            print("*selamat " + user + ", Anda berhasil Login Sebagai Admin")
            return menu()
        else:
            print("*Username dan Password yang anda masukkan salah")
            return menu()
    if menu1==2:
        Nasabah = input ("Masukkan Nama Anda : ")
        hello1 = ("-Silahkan Isi kolom berikut ini-")
        print(hello)
        user1 = input ("Username : ")
        if passw in password:
            print("selamat " + user + ", Anda berhasil Membuat Akun")
            return harga()
    if menu1==3:
        print("---Terimakasih telah Menggunakan Layanan Bank Sampah---")
        
menu()
