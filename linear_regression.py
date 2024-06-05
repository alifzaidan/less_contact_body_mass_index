import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'height_pixels': [414, 420, 380, 390, 424, 426],
    'real_height_cm': [150, 156, 145, 147, 161, 166],
    'width_pixels': [207, 210, 190, 205, 215, 220],
    'real_width_cm': [38, 40, 37, 36, 40, 43],
}

df = pd.DataFrame(data)

# Regresi linear untuk tinggi badan
X_height = df[['height_pixels']]
y_height = df['real_height_cm']
model_height = LinearRegression().fit(X_height, y_height)
line_height = model_height.predict(X_height)

# Regresi linear untuk lebar badan
X_width = df[['width_pixels']]
y_width = df['real_width_cm']
model_width = LinearRegression().fit(X_width, y_width)
line_width = model_width.predict(X_width)

# Menampilkan koefisien dan intercept untuk tinggi badan
slope_height = model_height.coef_[0]
intercept_height = model_height.intercept_
print(f'Persamaan regresi tinggi badan: tinggi(cm) = {slope_height:.2f} * piksel + {intercept_height:.2f}')

# Menampilkan koefisien dan intercept untuk lebar badan
slope_width = model_width.coef_[0]
intercept_width = model_width.intercept_
print(f'Persamaan regresi lebar badan: lebar(cm) = {slope_width:.2f} * piksel + {intercept_width:.2f}')

# Fungsi untuk memprediksi tinggi dan lebar berdasarkan model regresi
def predict_height_width(height_pixels, width_pixels):
    if not isinstance(height_pixels, (int, float)) or not isinstance(width_pixels, (int, float)):
        raise ValueError("Input harus berupa angka (int atau float)")
    
    temp_df_height = pd.DataFrame({'height_pixels': [height_pixels]})
    temp_df_width = pd.DataFrame({'width_pixels': [width_pixels]})
    
    predicted_height_cm = model_height.predict(temp_df_height)[0]
    predicted_width_cm = model_width.predict(temp_df_width)[0]
    
    return predicted_height_cm, predicted_width_cm

# Contoh penggunaan fungsi prediksi
# height_pixels_example = 220
# width_pixels_example = 110
# predicted_height, predicted_width = predict_height_width(height_pixels_example, width_pixels_example)
# print(f'Prediksi Tinggi: {predicted_height:.2f} cm')
# print(f'Prediksi Lebar: {predicted_width:.2f} cm')
