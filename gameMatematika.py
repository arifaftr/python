import random
import os

SAVE_FILE = "math_game_score.txt"

def load_score():
    """Menampilkan skor saat ini dari file jika ada"""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

def save_score(skor):
    """Menyimpan score ke dalam file"""
    with open(SAVE_FILE,"w") as file:
        file.write(str(skor))

def main():
    print("Selamat datang di Permainan Matematika Sederhana!\n")
    print("Kamu harus menjawab secepat mungkin.")
    print("Ketik 'exit' untuk keluar dari permainan.")
    print("=" * 50)

    konfirmasi = input("Apakah anda ingin memulai dari awal? (y/n): ").strip().lower()
    if konfirmasi == "y":
        skor = 0
    else:
        skor = load_score()
        
    print(f"Skor anda saat ini : {skor}\n")

    while True:
        # Generate angka dan operator acak
        angka1 = random.randint(1, 10)
        angka2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])
        
        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        else:
            hasil = angka1 // angka2

        # Tampilkan soal ke pemain
        soal = f"Berapakah {angka1} {operator} {angka2}? "
        jawaban = input(soal)

        # Periksa jika pemain ingin keluar
        if jawaban.lower() == "exit":
            print(f"Permainan selesai. Skor akhir kamu adalah {skor}.")
            break

        # Periksa jawaban pemain
        try :
            jawaban = float(jawaban) if "." in jawaban else int(jawaban) 
            if jawaban == hasil:
                print("Benar! 🎉")
                skor += 10
            else:
                print(f"Salah! Jawaban yang benar adalah {hasil}.")
                skor -= 5
        except ValueError:
            print("Salah! Jawaban harus berupa angka.")

        print(f"Skor kamu sekarang: {skor}")
        print("-" * 50)

if __name__ == "__main__":
    main()
