import cv2
from sklearn.linear_model import LinearRegression

def detect_height_from_camera():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        boxes, weight = hog.detectMultiScale(frame, winStride=(5, 5), padding=(0, 0), scale=1.03)

        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            height_pixels = h
            width_pixels = w

            cv2.putText(frame, f'Height: {height_pixels:.2f} pixel', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f'Width: {width_pixels:.2f} pixel', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Body Measurement', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

detect_height_from_camera()
