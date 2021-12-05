import cv2 as c
import sys as s

img = c.imread(str(s.argv[0]))
newimg = c.resize(img,(0,0),fx = .5, fy = .5)

c.imwrite('test.gif',newimg)