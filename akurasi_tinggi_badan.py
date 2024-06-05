import numpy as np
import pandas as pd

df = pd.read_csv('data_body_measurements.csv')

tinggi_real = df['Tinggi Real (cm)'].tolist()
tinggi_sistem = df['Tinggi Sistem (cm)'].tolist()

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