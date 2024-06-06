import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('data_body_measurements.csv')

height_pixels = df['Tinggi Sistem (pixel)'].tolist()
height_system = df['Tinggi Sistem (cm)'].tolist()
height_real = df['Tinggi Real (cm)'].tolist()
front_width_pixels = df['Lebar Depan Sistem (pixel)'].tolist()
front_width_system = df['Lebar Depan Sistem (cm)'].tolist()
front_width_real = df['Lebar Depan Real (cm)'].tolist()
side_width_pixels = df['Lebar Samping Sistem (pixel)'].tolist()
side_width_system = df['Lebar Samping Sistem (cm)'].tolist()
side_width_real = df['Lebar Samping Real (cm)'].tolist()

X_height = np.array(height_pixels).reshape((-1, 1))
y_height = height_real
model_height = LinearRegression().fit(X_height, y_height)
line_height = model_height.predict(X_height)

X_front_width = np.array(front_width_pixels).reshape((-1, 1))
y_front_width = front_width_real
model_front_width = LinearRegression().fit(X_front_width, y_front_width)
line_front_width = model_front_width.predict(X_front_width)

X_side_width = np.array(side_width_pixels).reshape((-1, 1))
y_side_width = side_width_real
model_side_width = LinearRegression().fit(X_side_width, y_side_width)
line_side_width = model_side_width.predict(X_side_width)

plt.figure(figsize=(20, 10))

plt.subplot(2, 2, 1)
plt.scatter(height_pixels, height_real, color='black', label='Tinggi Rata-rata (pixel) vs Tinggi Real (cm)')
plt.scatter(height_pixels, height_system, facecolors='white', edgecolors='black', label='Tinggi Rata-rata (pixel) vs Tinggi Sistem (cm)')
plt.plot(height_pixels, line_height, color='blue', label='Regresi Linear')
plt.xlabel('Tinggi (piksel)')
plt.ylabel('Tinggi (cm)')
plt.title('Grafik Regresi Linear Tinggi Badan')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter(front_width_pixels, front_width_real, color='black', label='Lebar Depan Rata-rata (pixel) vs Lebar Depan Real (cm)')
plt.scatter(front_width_pixels, front_width_system, facecolors='white', edgecolors='black', label='Lebar Depan Rata-rata (pixel) vs Lebar Depan Sistem (cm)')
plt.plot(front_width_pixels, line_front_width, color='blue', label='Regresi Linear')
plt.xlabel('Lebar Depan (piksel)')
plt.ylabel('Lebar Depan (cm)')
plt.title('Grafik Regresi Linear Lebar Depan')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.scatter(side_width_pixels, side_width_real, color='black', label='Lebar Samping Rata-rata (pixel) vs Lebar Samping Real (cm)')
plt.scatter(side_width_pixels, side_width_system, facecolors='white', edgecolors='black', label='Lebar Samping Rata-rata (pixel) vs Lebar Samping Sistem (cm)')
plt.plot(side_width_pixels, line_side_width, color='blue', label='Regresi Linear')
plt.xlabel('Lebar Samping (piksel)')
plt.ylabel('Lebar Samping (cm)')
plt.title('Grafik Regresi Linear Lebar Samping')
plt.legend()
plt.grid(True)

plt.savefig('visualisation_regression.png')
plt.tight_layout()
plt.show()