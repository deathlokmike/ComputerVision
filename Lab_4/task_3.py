import cv2


def start():
    print('Задача: выполнить операцию шарипнга изображения')
    original = cv2.imread('P1.jpg')
    # перевод изображения в оттенки серого
    gray_image = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("P1_gray.jpg", gray_image)
    # используем размытие
    gaussian = cv2.GaussianBlur(original, (0, 0), 2.0)
    unsharp_image = cv2.addWeighted(original, 2.0, gaussian, -1.0, 0)
    gaussian = cv2.GaussianBlur(gray_image, (0, 0), 2.0)
    # dst = source * alpha + blur * beta + gamma
    unsharp_gray_image = cv2.addWeighted(gray_image, 2.0, gaussian, -1.0, 0)
    # сохранение изображений

    cv2.imwrite("result_task_3.jpg", unsharp_image)
    cv2.imwrite("result_task_3_gray.jpg", unsharp_gray_image)


