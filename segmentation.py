import cv2
import numpy as np
from matplotlib import pyplot as plt


def seg(image):
    # plt.hist(image.ravel(), bins=256, range=[0,256]), plt.show()

    # 1. Select initial threshold
    T, T_prev = 127, 0
    flat_img = image.ravel()

    # 5.Repeat 2-4 until T does not change
    while T != T_prev:
        T_prev = T
        # 2. Segment the image using T
        G1_th = np.where(flat_img > T)
        G2_th = np.where(flat_img <= T)

        # 3. Compute m1, m2
        m1 = np.delete(image, G1_th).mean()
        m2 = np.delete(image, G2_th).mean()

        # 4. Compute new T1
        T = int((m1 + m2) / 2)
        print(T, T_prev)

    segment = np.where(image > T, 1, 0)
    return segment.astype(np.uint8)
