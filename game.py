import random
import os

# Ukuran peta
WIDTH = 10
HEIGHT = 10

# Posisi awal perawat
nurse_x = WIDTH // 2
nurse_y = HEIGHT // 2

# Posisi pasien secara acak
patient_x = random.randint(0, WIDTH - 1)
patient_y = random.randint(0, HEIGHT - 1)

# Fungsi untuk menampilkan peta
def display_map():
    os.system('cls' if os.name == 'nt' else 'clear')  # Membersihkan layar
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == nurse_x and y == nurse_y:
                print('O', end=' ')  # Posisi perawat
            elif x == patient_x and y == patient_y:
                print('X', end=' ')  # Posisi pasien
            else:
                print('.', end=' ')  # Area kosong
        print()
    print("Gunakan keyboard untuk bergerak (W=Atas, A=Kiri, S=Bawah, D=Kanan)")

# Fungsi utama permainan
def main():
    global nurse_x, nurse_y
    while True:
        display_map()

        # Jika perawat menemukan pasien
        if nurse_x == patient_x and nurse_y == patient_y:
            print("Selamat! Perawat menemukan pasien!")
            break

        # Input pergerakan
        move = input("Arah: ").upper()
        if move == 'W' and nurse_y > 0:
            nurse_y -= 1
        elif move == 'S' and nurse_y < HEIGHT - 1:
            nurse_y += 1
        elif move == 'A' and nurse_x > 0:
            nurse_x -= 1
        elif move == 'D' and nurse_x < WIDTH - 1:
            nurse_x += 1

if __name__ == "__main__":
    main()
