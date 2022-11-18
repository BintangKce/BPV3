#!/python/bin

# module
import os,sys,time

# pembersih
def bersih():
    os.system("clear")

# menu
def menu():
    bersih()
    print(" \x1b[0;34m_     ___   ____ ___ _   _")
    print("| |   / _ \ / ___|_ _| \ | |")
    print("| |  | | | | |  _ | ||  \| |")
    print("| |__| |_| | |_| || || |\  |")
    print("|_____\___/ \____|___|_| \_|")
    print("[\033[93m•\033[93m] \x1b[1;91mAuthor   : BintangPrawira")
    print("[\033[93m•\033[93m] \x1b[1;91mWhatsapp : +62 856-0938-5987")
    print("[\033[93m•\033[93m] \x1b[1;91mTikTok   : bintangprawira348")
    print("\033[95m_________________________________________")
    print("                Pilih                     ")
    print("\033[32m1.CobaAjaDulu")
    print("\033[32m2.Tema")
    print("\033[32m3.Mode Google")
    contoh = input ("pilih : ")
    if contoh == ("1"):
       bintang = input("Siapa Nama Pacarmu : ")
       print("Yang Benar Si " + bintang +" Mau sama kamu")
       os.system("figlet Mungkin Takut Sendirian")
       print("     \33[1;96mmakanya mau pacaran sama kamu.   ")
       print("==========================================================")
    elif contoh == '2':
         os.system("cmatrix")
         os.system("#")
    elif contoh == '3':
         print("katakan hallo ")
         bintang = input(" : ")
         print("hallo juga")
         print("__________________")
         print("Siapa nama kamu?")
         bintang = input (" : ")
         print(" Ok Mulai sekarang saya panggil kamu " + bintang)
         print("___________________________________________________")
         print("Apakah Ada Yang Bisa saya bantu " + bintang)
         BINTANG1 = input  ("Ya/Tidak ? ")
         Ya = input ("Tentang apa ? ")
         Tidak = input ("Oh : ")
         print("Tentang " +  Ya + " maaf kami sedang offline")
         Mulai = input ("apakah anda mau mulai lagi ? ")
         print(Mulai + " Ok Kontol")
         os.system("cd downloads")
         os.system("python gg.py")
menu()


P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
