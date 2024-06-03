import cv2
from linear_regression import predict_height_width

def detect_height_front_width_from_camera():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cap = cv2.VideoCapture(0)
    slope_height = 0.40
    intercept_height = 110
    slope_width = 0.30
    intercept_width = 50

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        boxes, weight = hog.detectMultiScale(frame, winStride=(5, 5), padding=(0, 0), scale=1.03)

        for (x, y, w, h) in boxes:
            height_pixels = h
            width_pixels = w
            
            height_cm = slope_height * height_pixels + intercept_height
            width_cm = slope_width * width_pixels + intercept_width

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'Height: {height_cm:.2f} cm', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f'Width: {width_cm:.2f} cm', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Body Measurement', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
detect_height_front_width_from_camera()
