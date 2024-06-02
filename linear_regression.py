import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'height_pixels': [100, 150, 200, 250, 300],
    'real_height_cm': [150, 170, 190, 210, 230],
    
    'front_width_pixels': [50, 75, 100, 125, 150],
    'real_front_width_cm': [70, 80, 90, 100, 110],
    
    'side_width_pixels': [25, 40, 60, 80, 100],
    'real_side_width_cm': [30, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

# Regresi linear untuk tinggi badan
X_height = df[['height_pixels']]
y_height = df['real_height_cm']
model_height = LinearRegression().fit(X_height, y_height)
line_height = model_height.predict(X_height)

# Regresi linear untuk lebar tampak depan
X_front_width = df[['front_width_pixels']]
y_front_width = df['real_front_width_cm']
model_front_width = LinearRegression().fit(X_front_width, y_front_width)
line_front_width = model_front_width.predict(X_front_width)

# Regresi linear untuk lebar tampak samping
X_side_width = df[['side_width_pixels']]
y_side_width = df['real_side_width_cm']
model_side_width = LinearRegression().fit(X_side_width, y_side_width)
line_side_width = model_side_width.predict(X_side_width)

# Menampilkan koefisien dan intercept untuk tinggi badan
slope_height = model_height.coef_[0]
intercept_height = model_height.intercept_
print(f'Persamaan regresi tinggi badan: tinggi(cm) = {slope_height:.2f} * piksel + {intercept_height:.2f}')

# Menampilkan koefisien dan intercept untuk lebar tampak depan
slope_front_width = model_front_width.coef_[0]
intercept_front_width = model_front_width.intercept_
print(f'Persamaan regresi lebar tampak depan: lebar(cm) = {slope_front_width:.2f} * piksel + {intercept_front_width:.2f}')

# Menampilkan koefisien dan intercept untuk lebar tampak samping
slope_side_width = model_side_width.coef_[0]
intercept_side_width = model_side_width.intercept_
print(f'Persamaan regresi lebar tampak samping: lebar(cm) = {slope_side_width:.2f} * piksel + {intercept_side_width:.2f}')

# Plot hasil regresi untuk tinggi badan
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.scatter(df['height_pixels'], df['real_height_cm'], color='black', label='Data')
plt.plot(df['height_pixels'], line_height, color='blue', label='Regresi Linear')
plt.xlabel('Tinggi (piksel)')
plt.ylabel('Tinggi (cm)')
plt.title('Regresi Linear untuk Tinggi Badan')
plt.legend()
plt.grid(True)

# Plot hasil regresi untuk lebar tampak depan
plt.subplot(1, 3, 2)
plt.scatter(df['front_width_pixels'], df['real_front_width_cm'], color='black', label='Data')
plt.plot(df['front_width_pixels'], line_front_width, color='red', label='Regresi Linear')
plt.xlabel('Lebar Tampak Depan (piksel)')
plt.ylabel('Lebar Tampak Depan (cm)')
plt.title('Regresi Linear untuk Lebar Tampak Depan')
plt.legend()
plt.grid(True)

# Plot hasil regresi untuk lebar tampak samping
plt.subplot(1, 3, 3)
plt.scatter(df['side_width_pixels'], df['real_side_width_cm'], color='black', label='Data')
plt.plot(df['side_width_pixels'], line_side_width, color='green', label='Regresi Linear')
plt.xlabel('Lebar Tampak Samping (piksel)')
plt.ylabel('Lebar Tampak Samping (cm)')
plt.title('Regresi Linear untuk Lebar Tampak Samping')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
