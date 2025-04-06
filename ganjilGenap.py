# tampilan awal
print("----------------------------------------")
print("=== Program Perhitungan Ganjil-Genap ===")
print("----------------------------------------")

while True:
    bilangan = input("Masukan angka : ")

    def cek_bilangan(bilangan):
        if int(bilangan) %2 == 0:
            return "Genap"
        else :
            return "Ganjil"
        
    # validasi jika ingin melanjutkan
    validasi = input("apakah ingin melanjutkan(y/n): ")
    

    if validasi.lower == "y":
        print("terimakasih!")
        break
        
    # menampilkan hasil
    print(f"Bilangan {bilangan} adalah bilangan {cek_bilangan(bilangan)}")
    print(validasi)
    
    

