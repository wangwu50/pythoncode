from PIL import Image


# 压缩图片
def thum(image_path):
    im = Image.open(image_path)
    w, h = im.size
    print('size: %sx%s' % (w, h))
    im.thumbnail((w // 2, h // 2))
    im.save('thumbnail.jpg', 'jpeg')


if __name__ == '__main__':
    thum('C:\\Users\\王文超\\Pictures\\Camera Roll\\DSC_0186.jpg')
