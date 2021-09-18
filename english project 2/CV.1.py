import cv2

Algoritimo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('foto_pessoas/pessoa_1.jpg')

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  #Coloquei a imagem em cinza pra aumentar a acurácia

faces = Algoritimo.detectMultiScale(imagem_cinza)
print(faces)

for(eixo_X, eixo_Y, largura, altura) in faces:
    cv2.rectangle(imagem, (eixo_X, eixo_Y), (eixo_X + largura, eixo_Y + altura), (0,255,0), 2)  #Criando o retângulo na imagem colorida


cv2.imshow("FACE", imagem)
cv2.waitKey()