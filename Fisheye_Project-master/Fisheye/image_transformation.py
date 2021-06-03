from wand.image import Image
import numpy as np
import os

from .loger import log


@log
def barrel_distortion(filepath: str, distortion_params: set, save_img=False, save_location=None) -> Image:
    k = distortion_params

    # transforming the image
    with Image(filename=filepath) as img:

        # print(img.size)
        img.virtual_pixel = 'transparent'
        img.distort('barrel', k)

        # saving image
        save_path = ''
        save_name = os.path.basename(filepath)

        if save_img == True:
            if save_location != None:
                save_path = os.path.join(save_location, save_name)
            else:
                save_path = save_name
                print(save_path)
            img.save(filename=save_path)

    return img
