import numpy as np
import pandas as pd

df = pd.read_csv('data_body_measurements.csv')

imt_real = df['IMT Real'].tolist()
imt_sistem = df['IMT Sistem'].tolist()
kategori_real = df['Kategori IMT Real'].tolist()
kategori_sistem = df['Kategori IMT Sistem'].tolist()

def calculate_error(real, sistem):
    errors = np.abs((np.array(sistem) - np.array(real)) / np.array(real)) * 100
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
