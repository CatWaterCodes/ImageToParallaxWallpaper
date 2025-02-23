from PIL import Image, ImageFilter, ImageDraw
from os import mkdir
import shutil

__all__ = ['generateParallaxBackground']
           
def blackAndWhiteFromRGB(RGB):
    r, g, b = RGB
    return (r + g + b) / 3

def processImage(img):
    blurred_image = img.filter(ImageFilter.BoxBlur(1))
    quantized_img = blurred_image.quantize(32, dither=Image.Dither.NONE)
    return quantized_img

def getRGBFromModeP(img: Image.Image):
    raw_palette = img.getpalette()
    colors = [(raw_palette[i], raw_palette[i+1], raw_palette[i+2]) for i in range(0, len(raw_palette), 3)]
    return colors

def generateLayers(img):
    colors = []
    finished_layers = []
    if img.mode == "P":
        colors = getRGBFromModeP(img)
    colors_sorted = colors.copy()
    colors_sorted.sort(reverse=True, key=blackAndWhiteFromRGB) #LIGHTEST COLOR AT THE START OF THE LIST

    layers = [Image.new("RGBA", (640, 640), (0,0,0,0)) for i in range(32)]

    for i in range(32):
        layer = layers[i]

        for y in range(640):
            for x in range(640):

                if colors[img.getpixel((x, y))] == colors_sorted[i]:
                    draw = ImageDraw.Draw(layer)
                    draw.circle((x,y), (i+1)/3.2, fill = colors[i] )
                    continue
        finished_layers.append(layer)
    
    return finished_layers

def makeImageHTML(n: int):
    result = ""
    for i in range(n-1, -1, -1):
        result += f'\n          <img src="layers/{i}.png" class="layers fit">'
    return result

def generateParallaxBackground(img: str, name: str, bg_color = "#000000") -> None:
    """Generates a parallax wallpaper from a single image. The path of the image has to be given in the 'img' parameter. The 'name' parameter is the name of the wallpaper you are making, and it can be anything. The 'bg_color' parameter takes in a hexadecimal value for the background color of the wallpaper, and it is set to '#000000' by default (remember to include the hashtag)."""
    img = Image.open(img)
    processed_image = processImage(img)
    parallax_layers = generateLayers(processed_image)

    #make the directory with the resulting background
    shutil.copytree("template", f"results/{name}")
    #save all layers to the directory
    for i in range(len(parallax_layers)): 
        parallax_layers[i].save(f"results/{name}/layers/{i}.png")

    #modify the template html to include the new layers
    with open(f"results/{name}/index.html", "r") as indexhtml:
        html_content = indexhtml.read()
    new_html = html_content.replace("REPLACEWITHIMAGES", makeImageHTML(32), 1)
    with open(f"results/{name}/index.html", "w") as indexhtml:
        indexhtml.write(new_html)
    
    #modify the css to have the right background color
    with open(f"results/{name}/styles/style.css", "r") as stylecss:
        css_content = stylecss.read()
    new_css = css_content.replace("BACKGROUNDCOLOR", bg_color, 1)
    with open(f"results/{name}/styles/style.css", "w") as stylecss:
        stylecss.write(new_css)

    #modify the json to have the right name
    with open(f"results/{name}/LivelyInfo.json", "r") as livelyinfojson:
        json_content = livelyinfojson.read()
    new_json = json_content.replace("NAMEOFBACKGROUND", name, 1)
    with open(f"results/{name}/LivelyInfo.json", "w") as livelyinfojson:
        livelyinfojson.write(new_json)

    #saves the complete image as a preview
    processed_image.save(f"results/{name}/preview.png")

    #saves the complete image as the preview gif
    processed_image.save(f"results/{name}/preview.gif")