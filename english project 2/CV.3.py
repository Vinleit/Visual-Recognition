import cv2

algoritimo_face = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')
algoritimo_olhos = cv2.CascadeClassifier('haarcascades\haarcascade_eye.xml')

imagem = cv2.imread('foto_pessoas\pessoa_1.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = algoritimo_face.detectMultiScale(imagem_cinza)
print(faces)

for (x, y, l, a) in faces:
    leitura = cv2.rectangle(imagem, (x, y), (x + l,y + a), (0,255,0), 2)
    local_olho = leitura[y:y + a, x:x + l]

    local_olho_cinza = cv2.cvtColor(local_olho, cv2.COLOR_BGR2GRAY)
    detectado = algoritimo_olhos.detectMultiScale(local_olho_cinza, scaleFactor=1.99)


for(olho_x, olho_y, olho_l, olho_a) in detectado:
    cv2.rectangle(local_olho, (olho_x, olho_y), (olho_x + olho_l, olho_y + olho_a), (0,225,0), 2)


cv2.imshow('Identificador', imagem)

cv2.waitKey()