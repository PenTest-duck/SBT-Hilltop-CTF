# Blindsighted - Writeup

This steganography challenge requires the solver to adjust brightness and contrast levels and convert Braille to decimal numbers and finally to ASCII.

Finding the Braille within the image shouldn't be difficult, as its transparency isn't very low and the challenge prompt gave a very critical clue that (a) the flag is visible, and (b) the flag is somewhere within the night background.
Sure enough, if we take a very close look at the top of the image, we can faintly see a strip of Braille characters.
Alternatively, we can use Stegsolve to XOR invert the image to see the Braille more clearly.

In order to improve the readability of the Braille, any image editor, such as PhotoShop, GIMP or even Microsoft Word can be used to modify the brightness, contrast, colours, sharpness etc..

# Deciphering the Braille

