print("==Masukan Data Diri==")

# List atribut data diri
data_labels = [
    "Nama Lengkap", "Nama Panggilan", "Umur", "Jenis Kelamin", "Alamat", "Tempat Lahir", "Tanggal Lahir", "Berat Badan", "Tinggi Badan", "Kewarganegaraan", "Agama", "Status Perkawinan", "Pendidikan Terakhir", "Pekerjaan/Profesi", "Instansi", "Golongan darah", "Hobi", "Warna Favorit","Makanan Favorit", "Minuman Favorit"
]

# dictionary untuk menyimpan data
data_diri = {}

# loop untuk input data
for label in data_labels:
    data_diri[label] = input(f"Masukan {label} : ")
    
print("\n==Data Diri==\n")

# Loop untuk menampilkan data
for label, value in data_diri.items():
    print(f"{label} : {value}")