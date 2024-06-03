import numpy as np
import pandas as pd

tinggi_real = [167.20, 169.90, 170.80, 165.60, 162.20, 152.30, 170.50, 147.20, 150.00, 149.90, 166.00, 160.74, 170.60, 169.90, 168.10, 178.00, 168.00, 157.50, 172.00, 162.40, 162.00, 152.30, 148.00, 144.50, 165.50, 158.00, 159.16, 156.70, 160.44, 163.00]
tinggi_sistem = [168.86, 169.45, 170.17, 166.09, 163.12, 155.40, 171.63, 150.05, 150.90, 152.43, 166.46, 160.46, 171.04, 166.09, 167.28, 176.19, 165.89, 158.76, 172.62, 161.73, 164.90, 153.60, 150.64, 150.64, 163.91, 159.65, 161.66, 149.45, 162.77, 163.71]

def calculate_error(real, sistem):
    errors = np.abs((np.array(sistem) - np.array(real)) / np.array(real)) * 100
    return errors

errors = calculate_error(tinggi_real, tinggi_sistem)

average_error = np.mean(errors)

accuracy = 100 - average_error

data = {
    "Data": list(range(1, len(tinggi_real) + 1)),
    "Tinggi Real (cm)": tinggi_real,
    "Tinggi Sistem (cm)": tinggi_sistem,
    "Error (%)": errors
}

df = pd.DataFrame(data)
print(df)

print(f'Error Rata-Rata (%) : {average_error}')
print(f'Akurasi (100% - Error Rata-rata) : {accuracy}')