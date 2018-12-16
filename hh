from PIL import Image

with Image.open('90.jpg') as im:
    old_size = im.size
    x, y = im.size
    new_size = (x+20, y+20)

    if new_size > old_size:
        # Set number of pixels to expand to the left, top, right,
        # and bottom, making sure to account for even or odd numbers
        if old_size[0] % 2 == 0:
            add_left = add_right = (new_size[0] - old_size[0]) // 2
        else:
            add_left = (new_size[0] - old_size[0]) // 2
            add_right = ((new_size[0] - old_size[0]) // 2) + 1

        if old_size[1] % 2 == 0:
            add_top = add_bottom = (new_size[1] - old_size[1]) // 2
        else:
            add_top = (new_size[1] - old_size[1]) // 2
            add_bottom = ((new_size[1] - old_size[1]) // 2) + 1

        left = 0 - add_left
        top = 0 - add_top
        right = old_size[0] + add_right
        bottom = old_size[1] + add_bottom

        # By default, the added pixels are black
        im = im.crop((left, top, right, bottom))
        im.show()
