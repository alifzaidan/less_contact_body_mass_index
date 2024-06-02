import cv2
import numpy as np
from sklearn.linear_model import LinearRegression

# Fungsi untuk mendeteksi tinggi dan lebar tubuh manusia dari kamera
def detect_height_front_width_from_camera():
    # Inisialisasi detektor HOG untuk mendeteksi tubuh manusia
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)  # Nomor 0 menunjukkan kamera default, bisa disesuaikan jika ada lebih dari satu kamera

    # Load model regresi linear untuk tinggi dan lebar tampak depan
    model_height_front_width = LinearRegression()
    model_height_front_width.coef_ = np.array([[slope_height]])
    model_height_front_width.intercept_ = np.array([intercept_height_front_width])

    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()
        if not ret:
            break

        # Deteksi objek menggunakan detektor HOG
        boxes, weight = hog.detectMultiScale(frame, winStride=(5, 5), padding=(0, 0), scale=1.03)

        # Prediksi tinggi dan lebar tampak depan menggunakan model regresi
        for (x, y, w, h) in boxes:
            height_pixels = h
            width_pixels = w

            # Prediksi tinggi menggunakan model regresi linear untuk tinggi
            predicted_height_cm = model_height_front_width.predict([[height_pixels]])[0]

            # Prediksi lebar tampak depan menggunakan model regresi linear
            predicted_front_width_cm = model_front_width.predict([[width_pixels]])[0]

            # Gambar kotak deteksi dan tampilkan hasil prediksi
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'Height: {predicted_height_cm:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f'Front Width: {predicted_front_width_cm:.2f} cm', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Tampilkan frame yang telah diproses
        cv2.imshow('Body Measurement', frame)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Stop kamera dan tutup jendela
    cap.release()
    cv2.destroyAllWindows()

# Panggil fungsi untuk mendeteksi tinggi dan lebar tampak depan tubuh manusia dari kamera
detect_height_front_width_from_camera()
