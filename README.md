# Project Overview:

## Create parallax wallpapers for Lively Wallpaper from a single image:
This program is meant to separate the layers of an image and turn it into a parallax interactive wallpaper made with html/css/js. This wallpaper can be used for any wallpaper app that uses wallpaper made with these tools, but was specifically made with Lively Wallpaper in mind.
It's also compatible with .ora archives, which you can export layered images as in most image editing or digital art applications (such as Krita and Gimp). The layers will be used as they are, without being resized or moved (aside from the parallax movement of course) to make it to convert layered digital art into an interactive parallax wallpaper using this tool.

## Previews:
Here are some album covers turned into wallpapers and the settings used to accomplish that result:
| Original Photo  | Parallax Result | Settings |
| :---: | :---: | :--- |
| <img src="https://github.com/user-attachments/assets/916232bc-2d58-4701-a076-e7ed6a8327ea" style="width: 250px; height: auto;"> | <img src="https://github.com/user-attachments/assets/cf02a08e-e46e-4b06-a798-a59fda2525f7" style="width: 250px; height: auto;"> | ```layer_num=16```<br>```background_color="#000000"```<br>```blur=True``` |
| <img src="https://github.com/user-attachments/assets/a7d365cc-afd7-4f6b-84a2-6907a0fcae5d" style="width: 250px; height: auto;"> | <img src="https://github.com/user-attachments/assets/972abfb7-e792-4659-be36-e64bdd216275" style="width: 250px; height: auto;"> | ```layer_num=32```<br>```background_color="#ab72b5"```<br>```blur=True``` |
| <img src="https://github.com/user-attachments/assets/a22b1440-8019-4fb9-9f9f-3c2c22517549" style="width: 250px; height: auto;"> | <img src="https://github.com/user-attachments/assets/040b92c9-cec4-437b-854a-b239e3913069" style="width: 250px; height: auto;"> | ```layer_num=3```<br>```background_color="#050808"```<br>```blur=False``` |

# Documentation:

## How to use:
1. Download the source code.
2. Install the required packages:
  ```python
  pip install -r requirements.txt
  ```
3. Run main.py:
  ```shell
  python main.py
  ```
4. Fill out the settings as you like in the program's dialog:
  ```
  Select the image you want to use (path to the image):
  >>> graduation.png
  Select a name for your wallpaper: 
  >>> graduation
  Select the number of layers (numbers greater than 32 are not recommended): 
  >>> 32
  Select a background color for your wallpaper (hexadecimal with the hastag. Example: '#000000'): 
  >>> #ab72b5
  ```
5. The wallpaper will be the folder that has the name you entered in the `results` folder.
6. To use it in Lively Wallpaper, refer back to my [guide on that](https://github.com/CatWaterCodes/LivelyWallpaperParallaxTemplate?tab=readme-ov-file#import-into-lively-wallpaper), in my [parallax wallpaper template](https://github.com/CatWaterCodes/LivelyWallpaperParallaxTemplate).

## Settings:

### The `image` setting:
Chose the image you want to make into a wallpaper by inputing its path.

### The `name` setting:
Chose the name of your wallpaper. It will be the name of the wallpaper folder inside of the `results` folder, but also the name that will appear in Lively Wallpaper.

### The `layer_num` setting:
Chose the number of layers your parallax effect will have. Number under 32 tend to lose some detail on images with a lot of detail, but numbers over 32 are not recommended as the background will shine through at extreme distances from the cursor to the center of the screen.

### The `bg_color` setting:
Chose the background color of your wallpaper, that will show on the sides of the image if it doesn't fill the screen.  If the layers come appart due to a high layer count, this is the color that will shne through, so chose something neutral to the image so that it doesn't clash with the effect. If you use a layer count lower than 32 the background color will not shine through at all and you can use a contrasting color to make the image shine.

### The `blur` setting:
The blur setting defines whether or not your image will be blurred before it's quantized. Blurring does not really make a difference in how much detail will be lost in the image, because information will be lost anyways by quantizing, and the layer drawing procedure loses some detail to given that the deeper the layer is in the parallax effect the bigger the "pixels" will be so that when the higher images move around the background doesn't show through. You should only be turning blur off when you are [working with an already quantized imaged](#working-with-an-already-quantized-image).

## Working with an already quantized image:

### Remove blur:
Turn blur off so that the quantization isn't ruined.

### Make sure the image is the right file format:
If you want to pre-quantize an image, you will have to export it as a `.png` because other file formats have lossy compression that can ruin the quantization. If you still run into problems, try turning off all compression methods in your image editing software of choice.

### Set the correct layer count:
When you are asked how many layers you want, please answer the exact number of colors you quantized your image to. If you input a wrong value that is greater you will get an error, and if you input a lower value, part of the image will be lost in the end result.
