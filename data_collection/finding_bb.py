import cv2
from PIL import ImageGrab


img = cv2.imread("/home/anandhakrishnanh/Pictures/Screenshot from 2020-10-02 00-18-45.png")

#reso = [1920,1080]

resolution = ImageGrab.grab()
reso = resolution.size
print(reso)

x = int(reso[0] * (266/1920))
y = int(reso[1] * (555/1080))
len_x = int(reso[0] * (177/1920))
len_y = int(reso[1] * (183/1080))

bb_box = [x,y,len_x,len_y]

img = img[bb_box[1]:bb_box[3] + bb_box[1], bb_box[0]:bb_box[2] + bb_box[0], :]

cv2.imshow("test",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

