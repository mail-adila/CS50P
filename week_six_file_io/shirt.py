#In a file called shirt.py, implement a program that expects exactly two command-line arguments:
# in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
# in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
# The program should then overlay shirt.png (which has a transparent background) on the input after
# resizing and cropping the input to be the same size, saving the result as its output.
#
# Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.I
# mage.open, resize and crop the input with ImageOps.fit, per
# pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for
# method, bleed, and centering, overlay the shirt with Image.paste, per
# pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the
# result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
#
# The program should instead exit via sys.exit:
# if the user does not specify exactly two command-line arguments,
# if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
# if the input’s name does not have the same extension as the output’s name, or
# if the specified input does not exist.
# Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
import sys
import os
from PIL import Image, ImageOps
from PIL import UnidentifiedImageError

def get_images():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    valid_extensions = {".jpg", ".jpeg", ".png"}
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    return input_file, output_file


def apply_shirt(input_file, output_file):
    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    # Resize and crop photo to exactly match the shirt's dimensions
    photo = ImageOps.fit(photo, shirt.size)

    # Overlay the shirt (second arg is the transparency mask)
    photo.paste(shirt, shirt)
    photo.save(output_file)

def main():
    input_file, output_file = get_images()
    apply_shirt(input_file, output_file)

if __name__ == "__main__":
    main()