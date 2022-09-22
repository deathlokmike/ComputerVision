import numpy as np
import cv2
from task_5 import get_corners


def start():
    original = cv2.imread('dom.jpg')
    # из 5-го задания углы Харриса
    result = get_corners(original)

    # находим контур объекта
    original_0 = cv2.imread('dom.jpg', 0)
    ret, binary = cv2.threshold(original_0, 127, 55, 0)
    contours, hierarchy = cv2.findContours(binary, 1, 2)
    cnt = contours[0]
    # находим моменты изображения
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(result, (cx, cy), 10, (255, 255, 0), -1)

    # SIFT
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 100)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv2.circle(result, (x, y), 12, (255, 0, 255), 3)

    cv2.namedWindow('Result', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Result', original)
    cv2.imwrite('result_task_7.jpg', result)
    cv2.waitKey(0)
