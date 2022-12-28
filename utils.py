import cv2
from os import listdir

def draw_collages(img):
    # draw windows
    
    frame_h, frame_w, _ = img.shape
    half_w, half_h = int(frame_w/2), int(frame_h/2)
    

    # add title
    cv2.line(img, (0, 70), (frame_w, 70), (0, 255, 0), 3)
    cv2.putText(img, 'AI Calculator', (180, 50), 1, 3, (0, 255, 0), 3)
    # divide the window into half horezontally
    cv2.line(img, (half_w-90, 70), (half_w-90, frame_h), (0, 255, 0), 2)
    # fill the left side
    img[70:, :half_w-90] = (255, 255, 255)
    
    # right-hand mini-window 
    cv2.line(img, (half_w-90, 120), (frame_w, 120), (0, 255, 0), 3)
    img[70:120, half_w+2-90:] = (255, 255, 255)
    cv2.putText(img, 'Fit your hand bellow', (half_w + 10, 100), 2, .7, (0, 0, 0), 1)    
    
    return img

def digit_img(digit):
    images_path = listdir('./images/numbers')
    
    img = cv2.imread(f'./images/numbers/{digit}.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img