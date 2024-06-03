import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'height_pixels': [100, 150, 200, 250, 300],
    'real_height_cm': [150, 170, 190, 210, 230],
    
    'width_pixels': [50, 75, 100, 125, 150],
    'real_width_cm': [70, 80, 90, 100, 110],
}

df = pd.DataFrame(data)

# Regresi linear untuk tinggi badan
X_height = df[['height_pixels']]
y_height = df['real_height_cm']
model_height = LinearRegression().fit(X_height, y_height)
line_height = model_height.predict(X_height)

# Regresi linear untuk lebar
X_width = df[['width_pixels']]
y_width = df['real_width_cm']
model_width = LinearRegression().fit(X_width, y_width)
line_width = model_width.predict(X_width)

# Menampilkan koefisien dan intercept untuk tinggi badan
slope_height = model_height.coef_[0]
intercept_height = model_height.intercept_
print(f'Persamaan regresi tinggi badan: tinggi(cm) = {slope_height:.2f} * piksel + {intercept_height:.2f}')

# Menampilkan koefisien dan intercept untuk lebar
slope_width = model_width.coef_[0]
intercept_width = model_width.intercept_
print(f'Persamaan regresi lebar badan: lebar(cm) = {slope_width:.2f} * piksel + {intercept_width:.2f}')

# Plot hasil regresi untuk tinggi badan
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(df['height_pixels'], df['real_height_cm'], color='black', label='Data')
plt.plot(df['height_pixels'], line_height, color='blue', label='Regresi Linear')
plt.xlabel('Tinggi (piksel)')
plt.ylabel('Tinggi (cm)')
plt.title('Regresi Linear untuk Tinggi Badan')
plt.legend()
plt.grid(True)

# Plot hasil regresi untuk lebar
plt.subplot(1, 2, 2)
plt.scatter(df['width_pixels'], df['real_width_cm'], color='black', label='Data')
plt.plot(df['width_pixels'], line_width, color='red', label='Regresi Linear')
plt.xlabel('Lebar (piksel)')
plt.ylabel('Lebar (cm)')
plt.title('Regresi Linear untuk Lebar Badan')
plt.legend()
plt.grid(True)


plt.tight_layout()
plt.show()