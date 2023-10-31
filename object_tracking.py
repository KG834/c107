import cv2
import time
import math

basket_x = 530
basket_y = 300

ball_x = []
ball_y = []

video = cv2.VideoCapture("bb3.mp4")
check,img = video.read()  

box = cv2.selectROI("Tracking", img, False)
tracker = cv2.TrackerCSRT_create() #load the tracker
tracker.init(img,box) #initializing the tracker

def rectangle(image, box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    cv2.rectangle(image, (x,y), (x+w, y+h), (55,0,0), 3)
    cv2.putText(image, "Tracking", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))

def tracking(image,box):
    x, y, w, h = int(box[0]), int(box[1]), int(box[2]), int(box[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)

    cv2.circle(image, (c1,c2), 2 , (0,225,0), 5 )    #BALL
    cv2.circle(image, (basket_x,basket_y) , 2 , (255,0,0), 5)  #BASKET

    #Calculate the distance
    distance = math.sqrt(((c1-basket_x)**2) + ((c2-basket_y)**2))
    if(distance < 20):
        cv2.putText(image, "GOAL", (375,90), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
    
    ball_x.append(c1)
    ball_y.append(c2)

    for index in range(0,len(ball_x)-1):
        cv2.circle(image, (ball_x[index],ball_y[index]), 1 , (0,0,225), 3)
    
while True:
    check,img = video.read()
    
    success, box = tracker.update(img)   

    if success:
        rectangle(img, box)
    else:
        cv2.putText(img, "Lost", (75,90), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255))        

    tracking(img,box)
    cv2.imshow("result",img)

            
    key = cv2.waitKey(25) # 25 ms

    if key == 32: #ASCII - AMERICAN STANDARD CODE FOR INFORMATION INTERCHANGE
        print("Stopped!")
        break
 

video.release()
cv2.destroyALLwindows()


