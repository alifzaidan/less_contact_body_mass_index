import cv2
import numpy as np
from sklearn.linear_model import LinearRegression

X_train_width = np.array([[50], [60], [70], [80], [90]])
y_train_width = np.array([45, 54, 63, 72, 81])  # Lebar dalam cm
X_train_height = np.array([[100], [120], [140], [160], [180]])
y_train_height = np.array([150, 160, 170, 180, 190])  # Tinggi dalam cm

model_width = LinearRegression()
model_width.fit(X_train_width, y_train_width)

model_height = LinearRegression()
model_height.fit(X_train_height, y_train_height)

def predict_dimensions(width_px, height_px):
    width_cm = model_width.predict(np.array([[width_px]]))[0]
    height_cm = model_height.predict(np.array([[height_px]]))[0]
    return width_cm, height_cm

# Inisialisasi detektor tubuh
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        width_cm, height_cm = predict_dimensions(w, h)
        cv2.putText(frame, f"Width: {width_cm:.2f} cm", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv2.putText(frame, f"Height: {height_cm:.2f} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow('Camera', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()