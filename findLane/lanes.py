import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)     # convert to gray
    blur = cv2.GaussianBlur(gray,(5,5),0)            # reduce noise by GaussianBlur
    canny = cv2.Canny(blur,50,150)
    return canny

def region_of_interest(img):
    height = img.shape[0]
    polygons= np.array([
    [(200,height),(1100,height),(550,250)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)
    masked_img = cv2.bitwise_and(img,mask)
    return masked_img

def display_line(img,lines):
    line_img = np.zeros_like(img)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_img, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0), 10)
    return line_img

def average_slop_intercept(img,line):
    left_fit = []           # negative slope
    right_fit = []          # positive slope
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        # y = mx+b where m = (y2-y1)/(x2-x1)
        parameters = np.polyfit((x1,x2),(y1,y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(img,left_fit_average)
    right_line = make_coordinates(img,right_fit_average)
    return np.array([left_line,right_line])


def make_coordinates(img,line_paremeters):
    slope,intercept = line_paremeters
    y1 = img.shape[0]
    y2 = int(y1*(3/5))

    # x = (y-b)/m
    x1 = (y1-intercept)/slope
    x2 = (y2-intercept)/slope
    return np.array([x1,y1,x2,y2])

cap = cv2.VideoCapture("road.mp4")

while(cap.isOpened()):
    _, frame = cap.read()
    canny_img = canny(frame)
    cropped_img = region_of_interest(canny_img)
    lines = cv2.HoughLinesP(cropped_img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    averaged_lines = average_slop_intercept(frame,lines)
    line_img = display_line(frame,averaged_lines)
    combo_img = cv2.addWeighted(frame,0.8,line_img,1,1)
    cv2.imshow("result", combo_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
