import cv2

Algoritimo = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')

imagem = cv2.imread('foto_pessoas\pessoas_4.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = Algoritimo.detectMultiScale(imagem_cinza, scaleFactor=1.02, minNeighbors=4, minSize=(20, 20), maxSize=(30, 30))
print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 255, 0), 2)

cv2.imshow("Identificador", imagem)

cv2.waitKey()