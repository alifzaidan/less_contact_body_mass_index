import imt

lebar_depan = 30
lebar_samping = 15
tinggi_badan = 155

# Menghitung luas area tubuh (BSA)
bsa = imt.luas_area_tubuh(lebar_depan, lebar_samping, tinggi_badan)
print(f"Luas area tubuh manusia (BSA): {bsa:.2f} meter persegi")

# Menghitung berat badan
berat_badan = imt.hitung_berat_badan(bsa, tinggi_badan)
print(f"Berat badan manusia: {berat_badan:.2f} kilogram")

# Menghitung IMT dan kategori
imt, kategori = imt.hitung_imt(berat_badan, tinggi_badan)
print(f"Indeks Massa Tubuh (IMT): {imt:.2f}")
print(f"Kategori IMT: {kategori}")
