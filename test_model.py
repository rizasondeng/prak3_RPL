from models.buku_models import BukuModel


model = BukuModel()

# 1. Menguji fungsi Create (menambahkan data buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke dalam MySQL!")

# 2. Menguji fungsi Read (mengambil data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(
        f"{buku['id_buku']} - {buku['judul']} - {buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )