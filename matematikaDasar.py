import os

def hitung_kecepatan():
    print("hitung kecepatan ready!")
    jarak = float(input("masukan jarak: "))
    waktu = float(input("masukan waktu: "))
    kecepatan = jarak*waktu
    print("kecepatan: ", kecepatan, "\n")
    
def luas_segitiga():
    print("hitung segitiga!")
    tinggi = float(input("masukan tinggi segitiga: "))
    alas = float(input("masukan panjang alas: "))
    luas = (alas * tinggi)/2
    print("Luas segitiga: ", luas, "\n")
    
def luas_balok():
    print("hitung balok!")
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    tinggi = float(input("masukan tinggi: "))
    luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
    print("luas balok: ", luas, "\n")
    
def luas_bola():
    print("hitung luas bola!")
    jari_jari = float(input("masukan jari-jari bola : "))
    luas = 4 * 3.14 * (jari_jari **2)
    print("luas bola: ", luas, "\n")
    
    
while True:
    userInput = int(input("Pilih rumus yang akan dipakai: \n\n1.hitung kecepatan\n2.luas segitiga\n3.luas balok\n4.luas bola\n5.keluar\npilih nomor berapa: "))
    os.system('cls')
    if userInput == 1:
        hitung_kecepatan()
    elif userInput == 2:
        luas_segitiga()
    elif userInput == 3:
        luas_balok()
    elif userInput == 4:
        luas_bola()
    else:
        break