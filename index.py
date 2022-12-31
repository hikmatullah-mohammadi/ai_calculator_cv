import cv2

import utils
from DigitSignRecognizer import DigitSignRecognizer

img_w, img_h = 640, 480
    
cap = cv2.VideoCapture(0)
cap.set(3, img_w)
cap.set(4, img_h)

digitSignRecognizer = DigitSignRecognizer()

prev_num = ''
operation = ''
operand1 = '0'
operand2 = '0'
answer = ''
cursor = 0 # where to enter input

# read the images of operators
plus = cv2.imread('./images/operators/plus.jpg')
minus = cv2.imread('./images/operators/minus.jpg')
mult = cv2.imread('./images/operators/mult.jpg')
div = cv2.imread('./images/operators/div.jpg')
equal = cv2.imread('./images/operators/equal.jpg')

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # do the drawings
    img = utils.draw_collages(img, plus=plus, minus=minus, mult=mult, div=div, equal=equal)
    # detect number
    number = digitSignRecognizer.main(img)
    if number and number != -1:
        
        if number != 'select':    
            # add digit image and digit text (detected digit)
            img[img_h-110:img_h-10, 10:110] = utils.digit_img(number)
            cv2.putText(img, str(number), (120, img_h-10), 1, 8, (0, 255, 0), 8)
            prev_num = str(number)
        
        # 'select' sign is detected
        elif number == 'select':
            # add a green square to indicate select mode
            img[123:173, img_w-50:] = (0, 255, 0)
            
            
            if prev_num:
                # keep digit image and digit text (detected digit)
                img[img_h-110:img_h-10, 10:110] = utils.digit_img(prev_num)
                cv2.putText(img, str(prev_num), (120, img_h-10), 1, 8, (0, 255, 0), 8)
                
                if cursor==0:    
                    operand1 = str(int(operand1 + str(prev_num)))
                elif cursor == 1:
                    operand2 = str(int(operand2 + str(prev_num)))
                    # reset if answer is not empty (end of calculations)
                    if answer != '':
                        cursor = 0
                        operation = ''
                        operand1 = '0'
                        operand2 = '0'
                        answer = ''
                        
                prev_num = ''
                
            # detect operations
            fings_pos_x, fings_pos_y = digitSignRecognizer.get_finger_postion()
            op = utils.detect_operation(fings_pos_x, fings_pos_y)
            
            if op and op != '=':
                operation = op
                cursor = 1
            # do calculations based on the current operation
            elif op == '=':
                if operation == '+':
                    answer = str(int(operand1) + int(operand2))
                elif operation == '-':
                    answer = str(int(operand1) - int(operand2))
                elif operation == '*':
                    answer = str(int(operand1) * int(operand2))
                elif operation == '/':
                    try:
                        answer = str(round(int(operand1) / int(operand2), 4))
                    except:
                        answer = ''
                else:
                    answer = ''
                
    # =============================================================================
    # display calculations (operands, operator and answer)
    # operand 1
    cv2.putText(img, operand1, (20, 160), 2, 1, (0, 0, 0), 2)
    # operator
    cv2.putText(img, operation, (20, 190), 2, 1, (0, 0, 0), 2)
    # operand 2
    cv2.putText(img, operand2, (20, 220), 2, 1, (0, 0, 0), 2)
    
    # line to seperate the answer
    cv2.line(img, (10, 250), (img_w//2-10, 250), (0, 255, 0), 2)
    # answer
    cv2.putText(img, answer, (20, 280), 2, 1, (0, 0, 0), 2)     
    # =============================================================================
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow('AI Calculator', img)
    
    # press q or Esc to exit
    if (cv2.waitKey(1) & 0xff==ord('q')) or cv2.waitKey(1) == 27 :
        break
        
        
cv2.destroyAllWindows()
