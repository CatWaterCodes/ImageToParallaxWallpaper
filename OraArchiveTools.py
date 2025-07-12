import zipfile
import os
import shutil
from PIL import Image
from LayerSeparator import backgroundFromLayers
import xml.etree.ElementTree as ET

__all__ = ['backgroundFromOra']

def makeLayers() -> list:
    image_tree = ET.parse('tempdir/stack.xml')
    image_node = image_tree.getroot()
    image_size = (int(image_node.attrib["w"]), int(image_node.attrib["h"]))
    layers = []
    for image_filename in os.listdir("tempdir/data"):
        image = Image.open(f"tempdir/data/{image_filename}")
        layers.append(image)
    
    layers.reverse()
    new_layers = []

    for i in range(len(layers)):
        fixed_image = Image.new("RGBA", image_size, (0,0,0,0))
        image.copy()
        fixed_image.paste(layers[i], (int(image_node[0][i].attrib["x"]), int(image_node[0][i].attrib["y"])))
        new_layers.append(fixed_image)

    return new_layers



def backgroundFromOra(file: str, name:str, bg_color: str) -> None:
    with zipfile.ZipFile(file,"r") as zip_ref:
        zip_ref.extractall("tempdir")

    new_layers = makeLayers()

    backgroundFromLayers(layers=new_layers, thumbnail=Image.open("tempdir/Thumbnails/thumbnail.png"), name=name, bg_color=bg_color)

    shutil.rmtree("tempdir")