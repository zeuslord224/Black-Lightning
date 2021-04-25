import cv2
import numpy as np
from matplotlib import pyplot as plt
def crtooonify(object):
  cv=cv2.imread(object)
  tadda=cv2.cvtColor(cv, cv2.COLOR_BGR2GRAY)
  tadda=cv2.medianBlur(tadda, 5)
  edges=cv2.adaptiveThreshold(tadda, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11)
  color = cv2.bilateralFilter(cv, 9, 300, 300)
  cartoon=cv2.bitwise_and(color, color, mask=edges)
  cv2.imwrite('cartoonify.png', cartoon)
  return 'cartoonify.png'

# Tadda1 By KeinShin Kangers! ( and Devs)


# Nani Kanger Twt ?!