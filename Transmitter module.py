import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

def nothing(x):
    pass

LaserGPIO = 27 #PIN11/GPIO17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LaserGPIO, GPIO.OUT)
# GPIO.output(LaserGPIO, GPIO.LOW)

sendWarningFlag = False

def sendWARNING(): # WARNING - 1010  #
#     GPIO.output(LaserGPIO, GPIO.LOW)
#     time.sleep(2)
    # Signal start
    
    # Bit 1: Laser ON (85ms), then OFF (115ms)
    GPIO.output(LaserGPIO, GPIO.HIGH)
    time.sleep(85 / 1000)
    GPIO.output(LaserGPIO, GPIO.LOW)
    time.sleep(115 / 1000)

    # Bit 0: Laser stays OFF for 200ms
    time.sleep(200 / 1000)

    # Bit 1: Laser ON (85ms), then OFF (115ms)
    GPIO.output(LaserGPIO, GPIO.HIGH)
    time.sleep(85 / 1000)
    GPIO.output(LaserGPIO, GPIO.LOW)
    time.sleep(115 / 1000)

    # Bit 0: Laser stays OFF for 200ms
    time.sleep(200 / 1000)

#     # Reset transmission
#     GPIO.output(LaserGPIO, GPIO.HIGH)

# Initilize and Delay before start transmitting data
# GPIO.output(LaserGPIO, GPIO.HIGH)
# print("Preparing...")
# time.sleep(1)
# print("Ready...")

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX        #Font style for writing text on video frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480) #Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
Kernal = np.ones((3, 3), np.uint8)

while(1):
    ret, frame = cap.read() ##Read image frame
    systime = time.time()
    camtime = cap.get(cv2.CAP_PROP_POS_MSEC)/1000.
    GPIO.output(LaserGPIO, GPIO.LOW)

    frame = cv2.flip(frame, +1)     ##Mirror image frame
    if not ret:                     ##If frame is not read then exit
        break
    if cv2.waitKey(1) == ord('s'):  ##While loop exit condition
        break
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         ##BGR to HSV
    lb = np.array([39, 0, 116])
    ub = np.array([222, 255, 255])

    mask = cv2.inRange(frame2, lb, ub)                      ##Create Mask
#     cv2.imshow('Masked Image', mask)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, Kernal)        ##Morphology
#     cv2.imshow('Opening', opening)

    res = cv2.bitwise_and(frame, frame, mask= opening)             ##Apply mask on original image
#     cv2.imshow('Resuting Image', res)

    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE,      ##Find contours
                                           cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        cnt = contours[0]
        area = cv2.contourArea(cnt)
        distance = (2*(10**(-7))* (area**2) - (0.0067 * area) + 83.487)/100
        M = cv2.moments(cnt)
        Cx = int(M['m10']/M['m00'])
        Cy = int(M['m01'] / M['m00'])
        ##S = 'Location of object:' + '(' + str(Cx) + ',' + str(Cy) + ')'
        ##cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
        S = 'Area of contour: ' + str(area)
        ##cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
        #S = 'Distance : ' + str(distance)
        cv2.putText(frame, "Distance: {:.2f}metres".format(distance), (280, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 69, 255), 2)
        if distance < 5:
            cv2.putText(frame, "Warning!!!", (140, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # print (systime)
            # print (camtime)
            if sendWarningFlag == False:
                sendWARNING()  # WARNING - 1010
                sendWarningFlag = True
            else:
                sendWarningFlag = False
            # pathlib.Path("output.txt").write_text("Timestamps: {:.2f}".format(camtime))
        
        # cv2.putText(frame, "Frame Count: %.2f" % (frames_count), (300, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 69, 255), 2)
        ##cv2.putText(frame, S, (5, 50), font, 2, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.drawContours(frame, cnt, -1, (0, 255, 0), 1)
        (x, y, w, h) = cv2.boundingRect(cnt)
        br_centroid = (x + int(w / 2), y + int(h / 2))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    ##Lets Detect a red ball
    cv2.imshow('Original Image', frame)

cap.release()                   ##Release memory
cv2.destroyAllWindows()         ##Close all the windows
