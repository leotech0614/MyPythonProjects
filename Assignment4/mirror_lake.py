"""
File: mirror_lake.py
Name: leo HUNG
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage, a mirrored image of mt-rainier.jpg with the same width but twice height
    """
    img = SimpleImage(filename)

    b_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            # Colored
            img_pixel = img.get_pixel(x, y)

            # White1
            b_img_pixel = b_img.get_pixel(x, y)
            # Drawing1
            b_img_pixel.red = img_pixel.red
            b_img_pixel.green = img_pixel.green
            b_img_pixel.blue = img_pixel.blue

            # White2
            b_img_pixel2 = b_img.get_pixel(x, b_img.height - 1 - y)
            # Drawing2
            b_img_pixel2.red = img_pixel.red
            b_img_pixel2.green = img_pixel.green
            b_img_pixel2.blue = img_pixel.blue
    return b_img


def main():
    """
    This program can make a mirrored image of mt-rainier.jpg with the same width but twice height
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
