import cv2 as cv

image = cv.imread('task.png')
print(image.shape)

y_start = 350
y_end = 790

x_start = 20
x_end = 460

cropping_image = image[x_start:x_end, y_start:y_end]

text = "CUTE DOG!"
coordinates = (450, 100)     
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (100, 255, 255)          
thickness = 5

cv.putText(image, text, coordinates, font, font_scale, color, thickness, cv.LINE_AA)

black_and_white_filtered = cv.cvtColor(image, cv.COLOR_BGR2GRAY) 
gaussian_blur = cv.GaussianBlur(image, (5, 5), 0)
gaussian_black_and_white_filtered = cv.GaussianBlur(black_and_white_filtered, (5, 5), 0)


cv.imshow("cropimage", cropping_image)
cv.imshow("image", image)
cv.imshow("filter1", gaussian_blur)
cv.imshow("filter2", gaussian_black_and_white_filtered)

cv.waitKey(0)
cv.destroyAllWindows