import numpy as np
import pandas as pd

df = pd.read_csv('data_body_measurements.csv')

berat_real = df['Berat Real (kg)'].tolist()
berat_sistem = df['Berat Sistem (kg)'].tolist()

def calculate_error(real, sistem):
    errors = np.abs((np.array(sistem) - np.array(real)) / np.array(real)) * 100
    return errors

errors = calculate_error(berat_real, berat_sistem)

average_error = np.mean(errors)

accuracy = 100 - average_error

data = {
    "Data": list(range(1, len(berat_real) + 1)),
    "Berat Real (kg)": berat_real,
    "Berat Sistem (kg)": berat_sistem,
    "Error (%)": errors
}

df = pd.DataFrame(data)
print(df)

print(f'Error Rata-Rata (%) : {average_error}')
print(f'Akurasi (100% - Error Rata-rata) : {accuracy}')
