from PIL import Image
import os


def is_square(img):
    return img.size[0] == img.size[1]


def calculate_gutters(img):
    return round((max(img.size) - min(img.size)) / 2)


def do_padding(img, padding, pad_x):
    w = max(img.size)
    h = w  # since we're making the img square

    res = Image.new(img.mode, (w, h), (255, 255, 255))
    left, top = 0, 0

    if pad_x:
        top = padding
    else:
        left = padding

    res.paste(img, (left, top))
    return res


def change_to_square(img):
    pad_x = img.size[0] > img.size[1]  # if not pad_x, then pad y. Increase width along that specific axis.
    padding = calculate_gutters(img)
    return do_padding(img, padding, pad_x)


def resize_square_image(img, target_size = 512):
    return img.resize((target_size, target_size), Image.LANCZOS)


def resize_image(filepath):
    img = Image.open(filepath)
    final = img.copy

    if not is_square(img):
        final = change_to_square(img)
        
    return resize_square_image(final)


def resize_all():
    input_path = 'input-images/'
    img_quality = 100
    imgs = os.listdir(input_path)

    for img in imgs:
        res = resize_image(input_path + img)
        res.save('output-images/' + img, 'JPEG', quality=img_quality)
        print('Completed image:', img)

    print('COMPLETED ALL!')


if __name__ == '__main__':
    resize_all()
