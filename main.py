import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

img = cv.imread('data/img1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))

## Detecting Characters
height, width, channels = img.shape
boxes = pytesseract.image_to_boxes(img)


f = open("data/characters.txt", "a")


for b in boxes.splitlines():
    b = b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv.rectangle(img, (x, height-y), (w, height-h), (0, 0, 255), 1)
    # cv.putText(img, b[0], (x, height-y+25), cv.FONT_HERSHEY_COMPLEX, 1, (40, 40, 55), 1)
    f.write(" "+b[0])
f.close()
cv.imshow('Result', img)
cv.waitKey(0)
