# Project Overview:

## Create parallax wallpapers for Lively Wallpaper from a single image:
This program is meant to separate the layers of an image and turn it into a parallax interactive wallpaper made with html/css/js. This wallpaper can be used for any wallpaper app that uses wallpaper made with these tools, but was specifically made with Lively Wallpaper in mind.

## Previews:
Here are some album covers turned into wallpapers and the settings used to accomplish that result:
| Original Photo  | Parallax Result | Settings |
| :---: | :---: | :--- |
| ![the_deal](https://github.com/user-attachments/assets/916232bc-2d58-4701-a076-e7ed6a8327ea) | ![Title-GoogleChrome2025-02-2313-39-45-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/9fe3a4b8-abad-497c-bff4-d9b1a97868c6) | ```layer_num=16```<br>```background_color="#000000"``` |
| ![graduation](https://github.com/user-attachments/assets/a7d365cc-afd7-4f6b-84a2-6907a0fcae5d) | ![Title-GoogleChrome2025-02-2314-41-38-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/540507ab-a59f-48cd-a287-f6c0b2d9b81e) | ```layer_num=32```<br>```background_color="#ab72b5"``` |

# Documentation:

## How to use:
1. Download the source code.
2. Open it inside a terminal:
  ```shell
  cd ImageToParallaxWallpaper
  ```
3. Activate the virtual environment:
  ```shell
  env/Scripts/activate
  ```
4. Run main.py:
  ```shell
  python main.py
  ```
5. Fill out the settings as you like:
  ```shell
  >>> graduation.png
  Select a name for your wallpaper: 
  >>> graduation
  Select the number of layers (numbers greater than 32 are not recommended): 
  >>> 32
  Select a background color for your wallpaper (hexadecimal with the hastag. Example: '#000000'): 
  >>> #ab72b5
  ```
6. The wallpaper will be the folder that has the name you entered in the `results` folder.
7. To use it in Lively Wallpaper, refer back to my [guide on that](https://github.com/CatWaterCodes/LivelyWallpaperParallaxTemplate?tab=readme-ov-file#import-into-lively-wallpaper), in my (parallax walpaper template)[https://github.com/CatWaterCodes/LivelyWallpaperParallaxTemplate].

## Settings:

### The `image` setting:
Chose the image you want to make into a wallpaper by inputing its path.

### The `name` setting:
Chose the name of your wallpaper. It will be the name of the wallpaper folder inside of the `results` folder, but also the name that will appear in Lively Wallpaper.

### The `layer_num` setting:
Chose the number of layers your parallax effect will have. Number under 32 tend to lose some detail on images with a lot of detail, but numbers over 32 are not recommended as the background will shine through at extreme distances from the cursor to the center of the screen.

### The `bg_color` setting:
Chose the background color of your wallpaper, that will show on the sides of the image if it doesn't fill the screen.  If the layers come appart due to a high layer count, this is the color that will shne through, so chose something neutral to the image so that it doesn't clash with the effect. If you use a layer count lower than 32 the background color will not shine through at all and you can use a contrasting color to make the image shine.
