import cv2
from os import listdir



def draw_collages(img):
    # draw windows
    
    frame_h, frame_w = 480, 640
    half_w, half_h = int(frame_w/2), int(frame_h/2)

    # add title
    cv2.line(img, (0, 70), (frame_w, 70), (0, 255, 0), 3)
    cv2.putText(img, 'AI Calculator', (180, 50), 1, 3, (0, 255, 0), 3)
    # divide the window into half horezontally
    cv2.line(img, (half_w, 70), (half_w, frame_h), (0, 255, 0), 2)
    
    
    # left side
    # fill the left side
    img[70:, :half_w] = (255, 255, 255)
    
    cv2.line(img, (0, 120), (half_w, 120), (0, 255, 0), 2)
    cv2.putText(img, 'Calculations', (20, 100), 2, .7, (0, 0, 0), 1)    
    
    # right-hand mini-window 
    cv2.line(img, (half_w, 120), (frame_w, 120), (0, 255, 0), 3)
    img[70:120, half_w+2:] = (255, 255, 255)
    cv2.putText(img, 'Fit your hand bellow', (half_w + 20, 100), 2, .7, (0, 0, 0), 1)    
    
    
    # ============================================================================
    # add operators
    # read operators images
    plus = cv2.imread('./images/operators/plus.jpg')
    minus = cv2.imread('./images/operators/minus.jpg')
    mult = cv2.imread('./images/operators/mult.jpg')
    div = cv2.imread('./images/operators/div.jpg')
    equal = cv2.imread('./images/operators/equal.jpg')
    
    y_start = 123
    y_end = 173
    
    x_start = [half_w, half_w+55, half_w+110, half_w+165, half_w+220]
    x_end = [half_w+50, half_w+105, half_w+160, half_w+215, half_w+270]
    
    # +
    img[y_start:y_end, x_start[0]:x_end[0]] = cv2.cvtColor(plus, cv2.COLOR_BGR2RGB)
    # -
    img[y_start:y_end, x_start[1]:x_end[1]] = cv2.cvtColor(minus, cv2.COLOR_BGR2RGB)
    # x
    img[y_start:y_end, x_start[2]:x_end[2]] = cv2.cvtColor(mult, cv2.COLOR_BGR2RGB)
    # /
    img[y_start:y_end, x_start[3]:x_end[3]] = cv2.cvtColor(div, cv2.COLOR_BGR2RGB)
    # =
    img[y_start:y_end, x_start[4]:x_end[4]] = cv2.cvtColor(equal, cv2.COLOR_BGR2RGB)
    # =============================================================================

    return img

def digit_img(digit):
    
    img = cv2.imread(f'./images/numbers/{digit}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

    
def detect_operation(fing_pos_x, fing_pos_y):
    frame_h, frame_w = 480, 640
    half_w, half_h = int(frame_w/2), int(frame_h/2)
    
    # operations positions on the screen
    y_start = 123
    y_end = 173
    
    x_start = [half_w, half_w+55, half_w+110, half_w+165, half_w+220]
    x_end = [half_w+50, half_w+105, half_w+160, half_w+215, half_w+270]
    
    if fing_pos_y >= y_start and fing_pos_y <= y_end+5: # in the scope
        # +
        if fing_pos_x >= x_start[0] and fing_pos_x <= x_end[0]:
            return '+'
        # -
        elif fing_pos_x >= x_start[1] and fing_pos_x <= x_end[1]:
            return '-'
        # x
        elif fing_pos_x >= x_start[2] and fing_pos_x <= x_end[2]:
            return '*'
        # /
        elif fing_pos_x >= x_start[3] and fing_pos_x <= x_end[3]:
            return '/'
        # =
        elif fing_pos_x >= x_start[4] and fing_pos_x <= x_end[4]:
            return '='
        else:
            return None
    else:
        return None
