import numpy as np
from PIL import Image
import cv2


def transfer(style, file):
    image = np.array(Image.open(file))
    model = config.STYLES[style]
    output, resized = style_model.inference(model, image)
    name = "image.jpg"
    cv2.imwrite(name, output)
    return name


dir(PIL)

