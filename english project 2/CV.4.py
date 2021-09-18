import cv2

webcam = cv2.VideoCapture(0)
algoritimo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
algoritimo_olho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')


while True:
    verificacao, frame = webcam.read()
    webcam_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = algoritimo.detectMultiScale(webcam_cinza, minSize=(100, 100))
    for (x, y, l, a) in face:
        leitura = cv2.rectangle(frame, (x, y), (x + l, y + a), (0, 255, 0), 2)
        cv2.putText(frame, "VINICIUS", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.70, (0,255,0),2, cv2.LINE_AA)

        local_olho = leitura[y: y + a, x: x + l]
        local_olho_cinza = cv2.cvtColor(local_olho, cv2.COLOR_BGR2GRAY)
        olhos = algoritimo_olho.detectMultiScale(local_olho_cinza, scaleFactor=2.81, minSize=(50,50))

        for (olho_x, olho_y, olho_l, olho_a) in olhos:
            cv2.rectangle(local_olho, (olho_x, olho_y), (olho_x + olho_l, olho_y + olho_a), (255, 0, 0), 2)

    cv2.imshow("Video", frame)
    cv2.waitKey(1)

    if cv2.waitKey(1) == ord("q"):
        break

webcam.release()
cv2.destroyWindow()