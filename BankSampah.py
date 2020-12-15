#Imron Assidiqi
import getpass
import os
print("Selamat Datang di Layanan Bank Sampah Terpadu")
print("---Menu---")
print("1. Login Sebagai Admin")
print("2. Login Sebagai User")
print("3. Register Sebagai User Nasabah Bank Sampah")
print("4. Exit")
menu1=int(input("Masukkan Menu Yang Anda Pilih :"))
if menu1==1:
    os.system("clear")
    hello = ("-Silahkan Masukan Akun admin Anda-")
    print(hello)
    user = input ("Username : ")
    passw = getpass.getpass(prompt="Password : ")
    password = {"imonassidiqi"}
    if passw in password:
        print("selamat " + user + ", Anda berhasil Login")
    else:
        print("Username dan Password yang anda masukkan salah")
if menu1==2:
    print ("Hallo Bosku")
