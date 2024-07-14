"""
File: blur.py
Name: leo HUNG
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original image(smiley-face.png)
    :return img: the first-time blurred image(smiley-face.png)
    """
    new_image = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            red_sum += pixel.red
                            green_sum += pixel.green
                            blue_sum += pixel.blue
                            count += 1
            new_image.pixel = new_image.get_pixel(x, y)
            new_image.pixel.red = red_sum // count
            new_image.pixel.green = green_sum // count
            new_image.pixel.blue = blue_sum // count
    return new_image


def main():
    """
    This program can create a blurred image according to the original image we input(smiley-face.png)
    , and more Blurred_Time(5) we input, more blurred image we can get.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
