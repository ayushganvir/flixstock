import cv2

input = 'input.jpg'
red = 'red.png'
mask = 'mask.png'
alpha_scale = 2.24
background_y_scale = 33.6
background_x_scale = 22.4
foreground = cv2.imread(input)
background = cv2.imread(red)
alpha = cv2.imread(mask)
alpha = cv2.resize(alpha, (0, 0), fx = alpha_scale, fy = alpha_scale)
background = cv2.resize(background, (0, 0), fx = background_x_scale, fy = background_y_scale)


foreground = foreground.astype(float)
background = background.astype(float)

alpha = alpha.astype(float)/255

foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1.0 - alpha, background)
outImage = cv2.add(foreground, background)
outImage = cv2.resize(outImage, (0, 0), fx = 0.05, fy = 0.05)

cv2.imwrite("alpha_blending/result.jpg", outImage)
cv2.imshow("result", outImage/255)
# cv2.destroyWindow('result')

cv2.waitKey(0)