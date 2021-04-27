
# By Kienshin Bitch.




import cv2
# import numpy as np
# from matplotlib import pyplot as plt
def crtooonify(img):
  cv=cv2.imread(img)
  tadda=cv2.cvtColor(cv, cv2.COLOR_BGR2GRAY)
  tadda=cv2.medianBlur(tadda, 5)
  edges=cv2.adaptiveThreshold(tadda, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)
  color = cv2.bilateralFilter(cv, 9, 300, 300)
  cartoon=cv2.bitwise_and(color, color, mask=edges)
  cv2.imwrite('cartoonify.png', cartoon)
  return 'cartoonify.png' # Remember!, do not forget to do os.remove('cartoonify.png) 
def rotate(img):
    
  cv=cv2.imread(img)
  while True:
      cv2.rotate(cv)


# by keinshin Tadda!
# Nani TwT!?