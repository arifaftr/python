import random
print("| Game Tebak Angka |\n")
username = input("Masukan username : ")
print(f"Selamat datang {username} di permainan tebak angka!\n")

#perulangan game
while True:
    angka = random.randint(1, 10)
    
    #input angka
    print("silahkan tebak angka 1-10")
    tebakan = int(input("Masukan tebakan anda :"))
    print(f"tebakan anda adalah {tebakan}")
    input("...")
    
    #validasi kebenaran
    if tebakan == angka:
        print("selamat anda benar!")
    else:
        print("maaf tebakan anda salah!")
        
    print(f"angka yang benar adalah {angka}")
    
    #konformasi user
    konfirmasi = input("tekan enter jika ingin melanjutkan...")
    print("\n")
    if konfirmasi == "":
        continue
    else:
        break

