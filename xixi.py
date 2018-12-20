from PIL import Image
from PIL import EpsImagePlugin
import math
filename = 'meituan.jpg'


def open_eps(filename, dpi=300.0):
    img = Image.open(filename)
    original = [float(d) for d in img.size]
    # scale = width / original[0] # calculated wrong height
    scale = dpi/72.0            # this fixed it
    if dpi is not 0:
        img.load(scale=math.ceil(scale))
    if scale != 1:
        img.thumbnail([round(scale * d) for d in original], Image.ANTIALIAS)
    return img


img = open_eps(filename, dpi=300.0)
img.save('pil_test.png', dpi=(300.0, 300.0))
