import numpy as np
import pandas as pd

berat_real = [60.25, 59.60, 70.10, 98.60, 52.92, 64.35, 54.85, 38.80, 42.50, 33.70, 49.16, 47.60, 66.75, 50.80, 45.90, 84.00, 55.30, 81.15, 92.50, 86.10, 67.45, 44.50, 52.50, 53.64, 61.20, 75.50, 72.80, 39.45, 30.95, 74.60]
berat_sistem = [60.38, 72.55, 55.40, 85.00, 46.78, 61.51, 57.14, 45.00, 43.10, 40.43, 57.14, 44.60, 60.84, 48.56, 51.40, 75.90, 59.40, 93.70, 63.50, 89.73, 64.94, 53.40, 61.00, 64.90, 74.10, 53.40, 75.67, 46.97, 80.87, 64.62]

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
