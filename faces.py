import cv2

RIGHT = 0
LEFT = 0
UP = 0
DOWN = 0
cnt = -1
MAX = 0
NRPECOL = 7

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imgfinal = cv2.imread('assets/test2.jpg', -1)
imgfinal = cv2.resize(imgfinal, (0, 0), fx=0.7, fy=0.7)

for i in range(len(imgfinal)):
    for j in range(imgfinal.shape[1]):
        imgfinal[i][j] = [255, 255, 255]

img = cv2.imread('assets/test2.jpg', -1)
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)

faces = face_cascade.detectMultiScale(img, 1.05, 4)

for (x, y, w, h) in faces:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cnt += 1
    if cnt % NRPECOL == 0:
        UP = MAX + 10
        MAX = 0
        LEFT = 0

    DOWN = UP + h
    MAX = max(DOWN, MAX)
    RIGHT = LEFT + w
    imgfinal[UP: DOWN, LEFT: RIGHT] = img[y: y + h, x: x + w]
    LEFT = RIGHT + 10

cv2.imshow('img', imgfinal)
cv2.waitKey(0)
