import imt
import pandas as pd
import os

slope_tinggi = 0.38
intercept_tinggi = -0.69
slope_lebar = 0.19
intercept_lebar = -1.33

# lebar_depan_sistem = 37.6
# lebar_samping_sistem = 33.25 - 17
# tinggi_badan_sistem = 150.9
# tinggi_badan_real = 150
# lebar_depan_real = 36.9
# lebar_samping_real = 15.11
# berat_badan_real = 43

# lebar_depan_sistem = 39.8
# lebar_samping_sistem = 35.75 - 17
# tinggi_badan_sistem = 162.71
# tinggi_badan_real = 163
# lebar_depan_real = 38.74
# lebar_samping_real = 19.29
# berat_badan_real = 60

# lebar_depan_sistem = 36.2
# lebar_samping_sistem = 32.33 - 17
# tinggi_badan_sistem = 163.71
# tinggi_badan_real = 164.5
# lebar_depan_real = 35.63
# lebar_samping_real = 16.21
# berat_badan_real = 46

# lebar_depan_sistem = 41.62
# lebar_samping_sistem = 38.53 - 17
# tinggi_badan_sistem = 168.81
# tinggi_badan_real = 169.1
# lebar_depan_real = 43.14
# lebar_samping_real = 22.91
# berat_badan_real = 72

# lebar_depan_sistem = 37.4
# lebar_samping_sistem = 34.93 - 17
# tinggi_badan_sistem = 160.2
# tinggi_badan_real = 159.5
# lebar_depan_real = 35.94
# lebar_samping_real = 19.12
# berat_badan_real = 52

# lebar_depan_sistem = 35.9
# lebar_samping_sistem = 32.93 - 17
# tinggi_badan_sistem = 148.88
# tinggi_badan_real = 150.1
# lebar_depan_real = 34.8
# lebar_samping_real = 17.2
# berat_badan_real = 44

# lebar_depan_sistem = 38.3
# lebar_samping_sistem = 34.33 - 17
# tinggi_badan_sistem = 165.21
# tinggi_badan_real = 166.9
# lebar_depan_real = 40.2
# lebar_samping_real = 18.1
# berat_badan_real = 56

# lebar_depan_sistem = 40.93
# lebar_samping_sistem = 36.42 - 17
# tinggi_badan_sistem = 170.69
# tinggi_badan_real = 172.2
# lebar_depan_real = 41.2
# lebar_samping_real = 20.3
# berat_badan_real = 60

# lebar_depan_sistem = 44.63
# lebar_samping_sistem = 39.96 - 17
# tinggi_badan_sistem = 167.69
# tinggi_badan_real = 169.15
# lebar_depan_real = 42.89
# lebar_samping_real = 24.3
# berat_badan_real = 78

lebar_depan_sistem = 35.73
lebar_samping_sistem = 30.42 - 17
tinggi_badan_sistem = 158.69
tinggi_badan_real = 156.2
lebar_depan_real = 34.25
lebar_samping_real = 14.3
berat_badan_real = 42

tinggi_badan_pixels = tinggi_badan_sistem / slope_tinggi - intercept_tinggi
lebar_depan_pixels = lebar_depan_sistem / slope_lebar - intercept_lebar
lebar_samping_pixels = lebar_samping_sistem / slope_lebar + 17 - intercept_lebar

# Menghitung luas area tubuh (BSA)
bsa = imt.luas_area_tubuh(lebar_depan_sistem, lebar_samping_sistem, tinggi_badan_sistem)
# print(f"Luas area tubuh manusia (BSA): {bsa:.2f} meter persegi\n")

# Menghitung berat badan sistem
berat_badan_sistem = imt.hitung_berat_badan(bsa, tinggi_badan_sistem)

# Menghitung IMT sistem dan kategori
imt_sistem, kategori_sistem = imt.hitung_imt(berat_badan_sistem, tinggi_badan_sistem)

# Menghitung IMT real dan kategori
imt_real, kategori_real = imt.hitung_imt(berat_badan_real, tinggi_badan_real)

print(f"Tinggi Sistem (pixel): {tinggi_badan_pixels:.2f} pixel")
print(f"Lebar Depan Sistem (pixel): {lebar_depan_pixels:.2f} pixel")
print(f"Lebar Samping Sistem (pixel): {lebar_samping_pixels:.2f} pixel")
print()
print(f"Tinggi Sistem (cm): {tinggi_badan_sistem:.2f} cm")
print(f"Lebar Depan Sistem (cm): {lebar_depan_sistem:.2f} cm")
print(f"Lebar Samping Sistem (cm): {lebar_samping_sistem:.2f} cm")
print(f"Berat Sistem (kg): {berat_badan_sistem:.2f} kilogram")
print(f"IMT Sistem: {imt_sistem:.2f}")
print(f"Kategori IMT Sistem: {kategori_sistem}")
print()
print(f"Tinggi Real (cm): {tinggi_badan_real:.2f} cm")
print(f"Lebar Depan Real (cm): {lebar_depan_real:.2f} cm")
print(f"Lebar Samping Real (cm): {lebar_samping_real:.2f} cm")
print(f"Berat Real (kg): {berat_badan_real:.2f} kilogram")
print(f"IMT Real: {imt_real:.2f}")
print(f"Kategori IMT Real: {kategori_real}")

data = {
    'Tinggi Sistem (pixel)': [tinggi_badan_pixels],
    'Lebar Depan Sistem (pixel)': [lebar_depan_pixels],
    'Lebar Samping Sistem (pixel)': [lebar_samping_pixels],
    'Tinggi Sistem (cm)': [tinggi_badan_sistem],
    'Berat Sistem (kg)': [berat_badan_sistem],
    'Lebar Depan Sistem (cm)': [lebar_depan_sistem],
    'Lebar Samping Sistem (cm)': [lebar_samping_sistem],
    'IMT Sistem': [imt_sistem],
    'Kategori IMT Sistem': [kategori_sistem],
    'Tinggi Real (cm)': [tinggi_badan_real],
    'Berat Real (kg)': [berat_badan_real],
    'Lebar Depan Real (cm)': [lebar_depan_real],
    'Lebar Samping Real (cm)': [lebar_samping_real],
    'IMT Real': [imt_real],
    'Kategori IMT Real': [kategori_real]
}

df = pd.DataFrame(data)

file_path = 'data_body_measurements.csv'

if os.path.exists(file_path):
    existing_df = pd.read_csv(file_path)
    df = pd.concat([existing_df, df], ignore_index=True)

df.to_csv(file_path, index=False)