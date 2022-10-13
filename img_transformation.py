import cv2
import numpy as np
import matplotlib.pyplot as plt
from segmentation import seg

def get_image(image, dn = 0.1, i = 3):
    image = cv2.imread(image, 0)
    plt.imshow(image, cmap='gray')
    plt.show()

    edges_ = cv2.Canny(image, 100, 200)     # canny edge detection을 하면 검은 배경에 흰 edge가 나옴
    edges = np.where(edges_ == 0, 255, 0)   # 반전
    threshold = seg(image)
    and_op = cv2.bitwise_and(edges.astype(np.uint8), threshold.astype(np.uint8))

    plt.subplot(1,3,1)
    plt.imshow(edges, cmap='gray')
    plt.subplot(1,3,2)
    plt.imshow(threshold, cmap='gray')
    plt.subplot(1,3,3)
    plt.imshow(and_op, cmap='gray')
    plt.show()


    kernel = np.ones((3,3), np.uint8)
    erosion = cv2.erode(and_op, kernel, iterations=i)


    plt.imshow(erosion, cmap='gray')
    plt.show()


    d_erosion = cv2.resize(erosion, dsize=(0,0), fx=dn, fy=dn)

    result = d_erosion

    H, W = result.shape


    # 눈금 종이에 출력하기
    plt.imshow(result, cmap='gray')
    plt.xticks(range(W))
    plt.yticks(range(H))

    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])
    plt.grid(True)
    plt.show()

    return result
