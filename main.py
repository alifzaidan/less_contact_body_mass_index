import imt
import pandas as pd
import os

# dalam satuan cm
lebar_depan_sistem = 30
lebar_samping_sistem = 15
tinggi_badan_sistem = 165
tinggi_badan_real = 166
berat_badan_real = 40

# Menghitung luas area tubuh (BSA)
bsa = imt.luas_area_tubuh(lebar_depan_sistem, lebar_samping_sistem, tinggi_badan_sistem)
# print(f"Luas area tubuh manusia (BSA): {bsa:.2f} meter persegi\n")

# Menghitung berat badan sistem
berat_badan_sistem = imt.hitung_berat_badan(bsa, tinggi_badan_sistem)

# Menghitung IMT sistem dan kategori
imt_sistem, kategori_sistem = imt.hitung_imt(berat_badan_sistem, tinggi_badan_sistem)

# Menghitung IMT real dan kategori
imt_real, kategori_real = imt.hitung_imt(berat_badan_real, tinggi_badan_real)

print(f"Tinggi Sistem (cm): {tinggi_badan_sistem:.2f} cm")
print(f"Berat Sistem (kg): {berat_badan_sistem:.2f} kilogram")
print(f"IMT Sistem: {imt_sistem:.2f}")
print(f"Kategori IMT Sistem: {kategori_sistem}")
print()
print(f"Tinggi Real (cm): {tinggi_badan_real:.2f} cm")
print(f"Berat Real (kg): {berat_badan_real:.2f} kilogram")
print(f"IMT Real: {imt_real:.2f}")
print(f"Kategori IMT Real: {kategori_real}")

data = {
    'Tinggi Sistem (cm)': [tinggi_badan_sistem],
    'Berat Sistem (kg)': [berat_badan_sistem],
    'IMT Sistem': [imt_sistem],
    'Kategori IMT Sistem': [kategori_sistem],
    'Tinggi Real (cm)': [tinggi_badan_real],
    'Berat Real (kg)': [berat_badan_real],
    'IMT Real': [imt_real],
    'Kategori IMT Real': [kategori_real]
}

df = pd.DataFrame(data)

file_path = 'data_body_measurements.csv'

if os.path.exists(file_path):
    existing_df = pd.read_csv(file_path)
    df = pd.concat([existing_df, df], ignore_index=True)

df.to_csv(file_path, index=False)