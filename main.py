from LayerSeparator import generateParallaxBackground

image = input("Select an image (input the path): \n>>> ")
name = input("Select a name for your wallpaper: \n>>> ")
layer_num = int(input("Select the number of layers (numbers greater than 32 are not recommended): \n>>> "))
bg_color = input("Select a background color for your wallpaper (hexadecimal with the hastag. Example: '#000000'): \n>>> ")
blur = input("Do you want to blur the image ? (on complex images it helps get more accurate colors on the layer separation, but if you have quantized an image already don't blur it) (y/n) \n>>> ")
blur = True if blur == "y" else False

generateParallaxBackground(img=image, name=name, n=layer_num, bg_color=bg_color, blur=blur)