from PIL import Image
import argparse


def rotate(image):
    im = Image.open(image)
    im.show()
    degree = input('Enter Degree to rotate: ')
    im.rotate(int(degree)).save(image)


