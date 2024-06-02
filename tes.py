import numpy as np
import pandas as pd
import cv2
from sklearn.linear_model import LinearRegression

# Fungsi untuk mendeteksi tinggi tubuh manusia dari kamera
def detect_height_from_camera():
    # Inisialisasi detektor HOG untuk mendeteksi tubuh manusia
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)  # Nomor 0 menunjukkan kamera default, bisa disesuaikan jika ada lebih dari satu kamera

    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()

        # Deteksi objek menggunakan detektor HOG
        # Anda dapat menyesuaikan parameter deteksi sesuai kebutuhan
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.03)

        # Gambar kotak deteksi dan tampilkan tinggi
        for (x, y, w, h) in boxes:
            # Gambar kotak deteksi
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Hitung tinggi dalam piksel
            height_pixels = h

            # Prediksi tinggi menggunakan model regresi linear untuk tinggi
            predicted_height_cm = model_height.predict([[height_pixels]])[0]

            # Tampilkan hasil
            cv2.putText(frame, f'Height: {predicted_height_cm:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Tampilkan frame yang telah diproses
        cv2.imshow('Human Height Detection', frame)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop kamera dan tutup jendela
    cap.release()
    cv2.destroyAllWindows()

# Data untuk pelatihan model regresi linear
data = {
    'height_pixels': [100, 150, 200, 250, 300], # Data piksel untuk tinggi badan
    'real_height_cm': [150, 170, 190, 210, 230]  # Data tinggi badan sebenarnya dalam cm
}

df = pd.DataFrame(data)

# Melakukan regresi linear untuk tinggi badan
X_height = df[['height_pixels']]
y_height = df['real_height_cm']
model_height = LinearRegression().fit(X_height, y_height)

# Panggil fungsi untuk mendeteksi tinggi tubuh manusia dari kamera
detect_height_from_camera()
