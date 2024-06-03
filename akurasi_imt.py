import numpy as np
import pandas as pd

imt_real = [
    21.55, 20.65, 24.00, 35.95, 20.11, 27.74, 18.87, 17.91, 18.90, 15.00, 
    19.20, 18.95, 23.12, 18.19, 16.24, 26.51, 19.59, 32.71, 32.65, 31.62, 
    23.12, 24.93, 23.97, 25.69, 22.34, 20.13, 28.65, 17.86, 32.77, 28.10
]

imt_sistem = [
    21.18, 25.27, 19.13, 30.81, 17.58, 25.47, 17.37, 19.13, 18.93, 17.27, 
    17.99, 17.34, 21.29, 17.60, 18.37, 24.45, 21.45, 37.18, 34.30, 27.10, 
    23.88, 23.68, 21.26, 22.15, 27.38, 27.58, 19.05, 21.80, 28.83, 24.11
]

kategori_real = [
    'I', 'I', 'I', 'O I', 'I', 'K', 'I', 'K', 'I', 'K', 
    'I', 'I', 'K', 'I', 'K', 'L', 'I', 'O I', 'O I', 'O I', 
    'K', 'O I', 'K', 'K', 'K', 'K', 'L', 'K', 'O I', 'L'
]

kategori_sistem = [
    'I', 'L', 'I', 'O I', 'K', 'K', 'K', 'K', 'I', 'K', 
    'K', 'K', 'K', 'I', 'K', 'L', 'I', 'O I', 'O I', 'I', 
    'K', 'K', 'K', 'K', 'I', 'K', 'I', 'K', 'K', 'I'
]

def calculate_error(imt_real, imt_sistem):
    errors = np.abs((np.array(imt_sistem) - np.array(imt_real)) / np.array(imt_real)) * 100
    return errors

imt_errors = calculate_error(imt_real, imt_sistem)

average_error = np.mean(imt_errors)

accuracy = 100 - average_error

correct_categories = sum([1 for real, system in zip(kategori_real, kategori_sistem) if real == system])
category_accuracy = (correct_categories / len(kategori_real)) * 100

data = {
    "Data": list(range(1, len(imt_real) + 1)),
    "IMT Real": imt_real,
    "Kategori Real": kategori_real,
    "IMT Sistem": imt_sistem,
    "Kategori Sistem": kategori_sistem,
    "Error (%)": imt_errors
}

df = pd.DataFrame(data)
print(df)

print(f'Error Rata-Rata (%) : {average_error}')
print(f'Akurasi (100% - Error Rata-rata) : {accuracy}')
print(f'Akurasi Kategori: {category_accuracy}')
