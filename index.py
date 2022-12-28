import cv2

import utils
from DigitSignRecognizer import DigitSignRecognizer

img_w, img_h = 640, 480
    
cap = cv2.VideoCapture(0)
cap.set(3, img_w)
cap.set(4, img_h)

digitSignRecognizer = DigitSignRecognizer()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img = utils.draw_collages(img)
    
    number = digitSignRecognizer.main(img)
    if number and number != -1:
        # cv2.putText(img, str(number), (10, img_h-10), 1, 8, (0, 255, 0), 8)
        img[img_h-110:img_h-10, 10:110] = utils.digit_img(number)
            
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('AI Calculator', img)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
        
        
cv2.destroyAllWindows()
