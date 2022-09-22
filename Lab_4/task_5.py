import numpy as np
import cv2


def get_corners(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10, useHarrisDetector=True)
    # преообразуем в целочисленный массив
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()  # считываем координаты
        cv2.circle(image, (x, y), 3, (0, 255, 255), -1)
    print(f'Количество углов: {len(corners)}')
    return image


def start():
    original = cv2.imread('dom.jpg')
    original = get_corners(original)
    cv2.namedWindow('Result', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Result', original)
    cv2.imwrite('result_task_5.jpg', original)
    cv2.waitKey(0)
