from PIL import Image, ImageDraw, ImageFont
import qrcode
import json
import os
import shutil

def generate(data):

    for vm_code, url in data.items():
        im = Image.open('youying.jpg')
        exif = im.info['exif']
        qr_img = qrcode.make(url, box_size=21, border =1 )
        (w, h) = qr_img.size
        x = int((1063 - w) / 2)  # 居中
        y = int((730 - h) / 2) + 480
        box = (x, y, x + w, y + h)
        im.paste(qr_img, box)

        # 文字
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("arial.ttf", 52)
        draw.text((590, 3630), vm_code, font=font, fill=(0, 0, 0, 0))
        # im.show()
        im.save('./result/{}.jpg'.format(vm_code),'jpeg', exif=exif, quanlity=100)


with open('data.json') as f:
    data = json.load(f)
    if os.path.isdir('./result'):
        shutil.rmtree('./result')
    os.mkdir('./result')
    generate(data)
