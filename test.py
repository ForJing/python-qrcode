from PIL import Image
import qrcode
import json
import os
import shutil
# img = qrcode.make('Some data here')
# img.show()


def generate(data):
    for vm_code, url in data.items():
        im = Image.open('temp.jpg')
        print('im info keys', im.info.keys())
        print('dpi', im.info['dpi'])

        exif = im.info['exif']
        qr_img = qrcode.make(url, box_size=22)
        (w, h) = qr_img.size
        x = int((750 - w) / 2 + 290)  # 居中
        y = 250
        box = (x, y, x + w, y + h)
        im.paste(qr_img, box)
        im.save('./result/{}.jpg'.format(vm_code),
                'jpeg', exif=exif, quanlity=100)


with open('data.json') as f:
    data = json.load(f)
    if os.path.isdir('./result'):
        shutil.rmtree('./result')
    os.mkdir('./result')
    generate(data)
