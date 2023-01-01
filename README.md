# AI Calculator |||| Computer Vision
A fascinating AI based calculator
---

## Table of contents
- [Project overview](#project-overview)
    - [What is this AI Calculator](#what-is-this-AI-Calculator)
    - [How to use it](#how-to-use-it)
    - [Benefits](#benefits)
    - [Screen shots](#screen-shots)
- [Project stracture](#project-stracture)
    - [Tools/technologies used](#tools-technologies-used)
- [Author](#author)

---

## Project overview
### What is this AI Calculator
This computer vision project is an AI based Calculator which assists the user to use their hand signs to do arithmetic calculations through a webcam.
Advances in deep learning, particularly image processing, has enabled me to create this project so as to utilize *American Sign Language (ASL)*
to make computer do our desired calculations. It also has a pretty good UI<br>
Bellow are hand signs for numbers from 0 to 9: <br>
0: ![0](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/0.JPG?raw=true)
1: ![1](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/1.JPG?raw=true)
2: ![2](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/2.JPG?raw=true)
3: ![3](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/3.JPG?raw=true)
4: ![4](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/4.JPG?raw=true)
5: ![5](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/5.JPG?raw=true)
6: ![6](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/6.JPG?raw=true)
7: ![7](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/7.JPG?raw=true)
8: ![8](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/8.JPG?raw=true)
9: ![9](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/numbers/9.JPG?raw=true)



### How to use it
First it detects your hand via the webcam, then it tries to check your hands' sign. If the hand sign is representing a number,
it will display the number and the digit sign on screen (bottom left). Next, it it detects that your hand is in 'select' mode (only thumb is up or thumb and finger are up),
it will check the cursor (wether the number belongs to operand1 or operand2) and inputs the detected number to the proper operand. When you are in 'select' mode, you can
use your finger to choose an operator from the screen (upper right), or select equal'=' to see the result. To reset, after getting the result, you can try to enter any number, then it will reset. Pressing 'q' or 'Esc' closes the app.


### Benefits
- Entertainment: you can just play arround with it, and use it a friendly hobby.
- It is useful when you don't have access to a keyboard, or the keyboard is broken.
- Playing with mathematics is super impressive to foster the development of children's brain and logic.
So long as this is a funny and entertaining calculator, it can be used as a tool to keep children busy
with math operations which is good for their brain development.

### Screen shots
Scr shot-1:<br>
![1](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/scr_shots/1.JPG?raw=true)<br>
Scr shot-2:<br>
![2](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/scr_shots/2.JPG?raw=true)<br>
Scr shot-3:<br>
![3](https://github.com/hikmatullah-mohammadi/ai_calculator_cv/blob/master/images/scr_shots/3.JPG?raw=true)<br>

## Project stracture
### Tools/technologies used
- [Python](https://www.python.org): a general purpose programming language.
- [OpenCV | cv2](https://www.opencv.org): OpenCV or cv2 is a Python library which deal with computer vision.
- [Mediapipe](https://google.github.io/mediapipe/): Mediapipe is a framework developed by [Google](https://www.google.com) offering cross-platform, customizable ML solutions for live and streaming media.
- [Numpy](https://www.numpy.org): Numpy (Numeric Python) is also a Python library which deals with math calculations.

## Author
- LinkedIn - [@hikmatullah-mohammadi](https://www.linkedin.com/in/hikmatullah-mohammadi-871550225)
- Github - [hikmatullah-mohammadi](https://www.github.com/hikmatullah-mohammadi)
- Website - [Hikmatullah Mohammadi](https://hikmatullah-mohammadi.netlify.app)
