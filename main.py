import cv2 as cv

image_file = 'data/img1.jpg'

img = cv.imread(image_file)

# cv.imshow("original image", img)
# cv.waitKey(0)

# invert image
inverted_image = cv.bitwise_not(img)
cv.imwrite('data/inverted.jpg', inverted_image)


# imgshow = cv.imread('data/inverted.jpg')
# cv.imshow("original image", imgshow)
# cv.waitKey(0)

# Binarization

def grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

gray_image = grayscale(img)
cv.imwrite("temp/gray.jpg", gray_image)

thresh, image_bw = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)
cv.imwrite("temp/bw_image.jpg", image_bw)
