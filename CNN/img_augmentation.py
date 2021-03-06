import cv2
import random
import numpy as np

img = cv2.imread('lena.jpg')


def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img


# Horizontal Shift
def horizontal_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = w * ratio
    if ratio > 0:
        img = img[:, :int(w - to_shift), :]
    if ratio < 0:
        img = img[:, int(-1 * to_shift):, :]
    img = fill(img, h, w)
    return img


# Vertical Shift
def vertical_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = h*ratio
    if ratio > 0:
        img = img[:int(h-to_shift), :, :]
    if ratio < 0:
        img = img[int(-1*to_shift):, :, :]
    img = fill(img, h, w)
    return img


# Brightness
def brightness(img, low, high):
    value = random.uniform(low, high)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img


# Zoom
def zoom(img, value):
    if value > 1 or value < 0:
        print('Value for zoom should be less than 1 and greater than 0')
        return img
    value = random.uniform(value, 1)
    h, w = img.shape[:2]
    h_taken = int(value*h)
    w_taken = int(value*w)
    h_start = random.randint(0, h-h_taken)
    w_start = random.randint(0, w-w_taken)
    img = img[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    img = fill(img, h, w)
    return img


# Channel Shift
def channel_shift(img, value):
    value = int(random.uniform(-value, value))
    img = img + value
    img[:,:,:][img[:,:,:]>255]  = 255
    img[:,:,:][img[:,:,:]<0]  = 0
    img = img.astype(np.uint8)
    return img


# Horizontal Flip
def horizontal_flip(img, flag):
    if flag:
        return cv2.flip(img, 1)
    else:
        return img


# Vertical Flip
def vertical_flip(img, flag):
    if flag:
        return cv2.flip(img, 0)
    else:
        return img


# Rotation
def rotation(img, angle):
    angle = int(random.uniform(-angle, angle))
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    return img


def img_aug(img):
    ar = []
    # ar.append(horizontal_shift(img, 0.7))
    # ar.append(vertical_shift(img, 0.7))
    ar.append(brightness(img, 0.5, 3))
    # ar.append(zoom(img, 0.3))
    # ar.append(channel_shift(img, 60))
    # ar.append(horizontal_flip(img, True))
    # ar.append(vertical_flip(img, True))
    ar.append(rotation(img, 35))
    # for i in range(0, len(ar)):
    #     filename = 'augmentation/lena_aug' + str(i + 1) + '.png'
    #     cv2.imwrite(filename, ar[i])


    # cv2.imshow('horizontal', image1)
    # cv2.imshow('vertical', image2)
    # cv2.imshow('bright', image3)
    # cv2.imshow('zoom', image4)
    # cv2.imshow('channelshift', image5)
    # cv2.imshow('horflit', image6)
    # cv2.imshow('verflit', image7)
    # cv2.imshow('rotation', image8)
img_aug(img)
cv2.imshow('bright',ar[0])
cv2.imshow('rotate',ar[1])
cv2.waitKey(0)
cv2.destroyAllWindows()