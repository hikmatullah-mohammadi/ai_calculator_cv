import cv2

import utils
from DigitSignRecognizer import DigitSignRecognizer

img_w, img_h = 640, 480
    
cap = cv2.VideoCapture(0)
cap.set(3, img_w)
cap.set(4, img_h)

digitSignRecognizer = DigitSignRecognizer()

prev_num = None
operation = None

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    img = utils.draw_collages(img)
    
    number = digitSignRecognizer.main(img)
    if number and number != -1:
        # cv2.putText(img, str(number), (10, img_h-10), 1, 8, (0, 255, 0), 8)
        if number != 'select':    
            img[img_h-110:img_h-10, 10:110] = utils.digit_img(number)
            prev_num = number
        
        # 'select' sign is detected
        elif prev_num:
            img[img_h-110:img_h-10, 10:110] = utils.digit_img(prev_num)
            img[123:173, img_w-50:] = (0, 255, 0)
            
            fings_pos_x, fings_pos_y = digitSignRecognizer.get_finger_postion()
            operation = utils.detect_operation(fings_pos_x, fings_pos_y)            
            
        
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('AI Calculator', img)
    
    # press q or Esc to exit
    if (cv2.waitKey(1) & 0xff==ord('q')) or cv2.waitKey(1) == 27 :
        break
        
        
cv2.destroyAllWindows()
