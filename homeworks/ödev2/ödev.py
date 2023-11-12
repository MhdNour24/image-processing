import cv2
import numpy as np

# Kamera girişi
cap = cv2.VideoCapture(0)

while True:
    # Görüntüyü yakala
    ret, frame = cap.read()

    # Görüntüyü HSV formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Kırmızı renk aralığını belirleme
    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    
    # Kırmızı renk aralığını maskeleme
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Orijinal görüntüde sadece kırmızı nesneleri gösterme
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Sonuçları gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)
    cv2.imshow('mask', mask)
    
    # Çıkış için 'q' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırakma
cap.release()
cv2.destroyAllWindows()
