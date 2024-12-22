# tampilan awal
print("----------------------------------------")
print("=== Program Perhitungan Ganjil-Genap ===")
print("----------------------------------------")
bilangan = input("Masukan angka : ")

def cek_bilangan(bilangan):
    if int(bilangan) %2 == 0:
        return "Genap"
    else :
        return "Ganjil"
    
# menampilkan hasil
print(f"Bilangan {bilangan} adalah bilangan {cek_bilangan(bilangan)}")
