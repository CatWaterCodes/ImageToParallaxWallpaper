from LayerSeparator import generateParallaxBackground
from OraArchiveTools import backgroundFromOra

def __main__():
    ora = input("Would you like to convert an image into a wallpaper, or a .ora file? (image/ora) \n>>>")
    ora = True if ora == "ora" else False

    name = input("Select a name for your wallpaper: \n>>> ")
    bg_color = input("Select a background color for your wallpaper (hexadecimal with the hastag. Example: '#000000'): \n>>> ")

    if ora:
        oraFile = input("Select a .ora file (input the path): \n>>> ")

        backgroundFromOra(file=oraFile, name=name, bg_color=bg_color)
    else:
        image = input("Select an image (input the path): \n>>> ")
        blur = input("Do you want to blur the image ? (on complex images it helps get more accurate colors on the layer separation, but if you have quantized an image already don't blur it) (y/n) \n>>> ")
        layer_num = int(input("Select the number of layers (numbers greater than 32 are not recommended): \n>>> "))
        blur = True if blur == "y" else False

        generateParallaxBackground(img=image, name=name, n=layer_num, bg_color=bg_color, blur=blur)