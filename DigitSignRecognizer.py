# import required libraries
import cv2
import numpy as np
import mediapipe as mp


class DigitSignRecognizer():
    '''
    This class aims to provide a way to detect and recognize hand sign for digits. (American Sign Language)
    '''
    def __init__(self):
        # initializations
        self.__img = None
        self.__img_w = 0
        self.__img_h = 0
        
        
        self.__mpHands = mp.solutions.hands
        self.__hands = self.__mpHands.Hands()
        
        # tips indices in mediapipe
        self.__tipsInds = [4, 8, 12, 16, 20]


    def __from_perc(self, perc, dim='w'):
        '''
        This method changes percentage to pixel value regarding the width and the height of the image accordingly.
        '''
        if dim=='h' or dim=='height':
            return int(perc * self.__img_h / 1)
        elif dim=='w' or dim=='width':
            return int(perc * self.__img_w / 1)

    def __count_num_util(self, fingers_up_down):
        '''
        This method takes the list of fingers up or down e.g. [1, 1, 1, 0, 1],
        and returns 1 to 9, 'select', or -1 accordingly.
        '''
        if fingers_up_down[0] == 1 and fingers_up_down.count(1) == 0:
            return -1
        elif fingers_up_down[1] == 1 and fingers_up_down.count(1) == 1:
            return 1
        elif all(fingers_up_down[1:3]) == 1 and fingers_up_down.count(1) == 2:
            return 2
        elif all(fingers_up_down[:3]) == 1 and fingers_up_down.count(1) == 3:
            return 3
        elif all(fingers_up_down[1:]) == 1 and fingers_up_down.count(1) == 4:
            return 4
        elif fingers_up_down.count(1) == 5:
            return 5
        elif all(fingers_up_down[1:4]) == 1 and fingers_up_down.count(1) == 3:
            return 6
        elif all(fingers_up_down[1:3]) == 1 and fingers_up_down[4] == 1 and fingers_up_down.count(1) == 3:
            return 7
        elif fingers_up_down[1] == 1 and all(fingers_up_down[3:]) == 1 and fingers_up_down.count(1) == 3:
            return 8
        elif all(fingers_up_down[2:]) == 1 and fingers_up_down.count(1) == 3:
            return 9
        # if only thumb is up
        elif fingers_up_down[0] == 1 and fingers_up_down.count(1) == 1:
            thumb_tip = (self.__from_perc(self.tips_lms[0][1].x), self.__from_perc(self.tips_lms[0][1].y, dim='h'))
            fing_tip = (self.__from_perc(self.tips_lms[1][1].x), self.__from_perc(self.tips_lms[1][1].y, dim='h'))
            
            # to make sure it is not mistaken with ZERO
            if np.linalg.norm([thumb_tip[0] - fing_tip[0], thumb_tip[1] - fing_tip[1]]) > 80:
                return 'get_num'
        # if thumb and finger are up
        elif all(fingers_up_down[0:2]) == 1 and fingers_up_down.count(1) == 2:
            return 'select'
        
        else:
            return -1
    
    def __is_zero(self, tips_lms):
        '''
        This method takes tips lanmarks and detect wether or not the sign is indicating ZERO
        '''
        # extract xs and ys of tips
        x = [self.__from_perc(lm[1].x) for lm in tips_lms]
        y = [self.__from_perc(lm[1].y, 'h') for lm in tips_lms]
        
        # distance between thumb's tip and any other finger's tip
        dis1 = np.linalg.norm([x[0] - x[1],  y[0] - y[1]])
        dis2 = np.linalg.norm([x[0] - x[2],  y[0] - y[2]])
        dis3 = np.linalg.norm([x[0] - x[3],  y[0] - y[3]])
        dis4 = np.linalg.norm([x[0] - x[4],  y[0] - y[4]])
        dis5 = np.linalg.norm([x[1] - x[4],  y[1] - y[4]])
        if dis1 <= 35 and dis2 <= 35 and  dis3 <= 35 and  dis4 <= 35 and dis5 <= 30:
            return True
        return False

    def get_finger_postion(self):
        '''
        This method takes no argument and returns the position of finger x and y
        '''
        return self.__from_perc(self.tips_lms[1][1].x), self.__from_perc(self.tips_lms[1][1].y, dim='h')

    def main(self, img):
        '''
        This method, in its simplest definition, takes an image, if it can detect a hand in it, it will then
        see wether the hand sign is representing a number. Finally, it returns the detected number or None if no hand is detected. 
        '''
        self.__img = img
        self.__img_h, self.__img_w, _ = img.shape
        
        fingers_up_down = []
        is_zero = False
        
        result = self.__hands.process(self.__img)
        if result.multi_hand_landmarks:
            
            # pick only one hand (left most in the picture if there are more than one)
            hand_lms = result.multi_hand_landmarks[0]
            
            self.tips_lms = [(id, lm) for id, lm in enumerate(hand_lms.landmark) if id in self.__tipsInds]
            
            # this loop's aim is to detect wether fingers are up (straight) or down
            for tip_lm in self.tips_lms:
                x_tip, y_tip = self.__from_perc(tip_lm[1].x, 'w'), self.__from_perc(tip_lm[1].y, 'h')
                center_tip = (x_tip, y_tip)
                # tip
                cv2.circle(self.__img, center_tip, 5, (0, 255, 0), cv2.FILLED)
                # MCP
                x_mcp, y_mcp = self.__from_perc(hand_lms.landmark[tip_lm[0]-2].x, 'w'), self.__from_perc(hand_lms.landmark[tip_lm[0]-2].y, 'h')
                
                # thumbs          
                if tip_lm[0] == 4:
                    if hand_lms.landmark[1].x <= hand_lms.landmark[0].x:
                        if x_tip < self.__from_perc(hand_lms.landmark[2].x, 'w'):
                            fingers_up_down.append(1)
                        else:
                            fingers_up_down.append(0)
                    else:
                        if x_tip > self.__from_perc(hand_lms.landmark[2].x, 'w'):
                            fingers_up_down.append(1)
                        else:
                            fingers_up_down.append(0)
                # other fingers
                elif y_tip < y_mcp:
                    fingers_up_down.append(1)
                else:
                    fingers_up_down.append(0)
                
            # Detect ZERO
            is_zero = self.__is_zero(self.tips_lms)
            
            
            # count number
            if is_zero:
                number = '0'
            else:
                number = self.__count_num_util(fingers_up_down)
            
            return number # 0-9, -1
            
        # if no hand detected
        return None
    
