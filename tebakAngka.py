import random
print("|--------Game Tebak Angka--------|\n")

username = input("Masukan username : ")
print(f"Selamat datang {username} di permainan tebak angka!\n")

#perulangan game
while True:
    angka = random.randint(1, 10)
    
    #input angka
    print("silahkan tebak angka 1-10")
    tebakan = int(input("Masukan tebakan anda :"))
    print(f"tebakan anda adalah {tebakan}")
    input("tekan enter untuk melanjutkan...")
    
    #validasi kebenaran
    if tebakan == angka:
        print("selamat anda benar!")
    else:
        print("maaf tebakan anda salah!")
        
    print(f"angka yang benar adalah {angka}")
    
    #konformasi user
    konfirmasi = input("apakah anda ingin melanjutkan permainan (y/n) : ")
    
    if konfirmasi == "y":
        input("tekan enter untuk memuat permainan...")
        continue
    elif konfirmasi == "n":
        print("terimakasih telah bermain!")
        break

