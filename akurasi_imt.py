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
    "Data": list(range(1, len(imt_real) + 1)) + ['Error Rata-Rata (%)', 'Akurasi (100% - Error Rata-rata)', 'Akurasi Kategori'],
    "IMT Real": imt_real + [np.nan, np.nan, np.nan],
    "Kategori Real": kategori_real + [np.nan, np.nan, np.nan],
    "IMT Sistem": imt_sistem + [np.nan, np.nan, np.nan],
    "Kategori Sistem": kategori_sistem + [np.nan, np.nan, np.nan],
    "Error (%)": imt_errors.tolist() + [average_error, accuracy, category_accuracy]
}

df = pd.DataFrame(data)
print(df)

df.to_excel('akurasi_imt.xlsx', index=False)