from LayerSeparator import generateParallaxBackground

image = input("Select an image (input the path): \n>>> ")
name = input("Select a name for your wallpaper: \n>>> ")
layer_num = int(input("Select the number of layers (numbers greater than 32 are not recommended): \n>>> "))
bg_color = input("Select a background color for your wallpaper (hexadecimal with the hastag. Example: '#000000'): \n>>> ")

generateParallaxBackground(img=image, name=name, n=layer_num, bg_color=bg_color)