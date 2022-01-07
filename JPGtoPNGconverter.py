import sys
import os
from PIL import Image
from pathlib import Path


def check_new_folder_path(path, folder):
    new_folder = Path(f"{path.absolute()}/{folder}")
    if new_folder.is_dir():
        return new_folder.absolute()
    else:
        new_folder.mkdir()
        print('Destination folder does not exist, new folder was created')
        return new_folder.absolute()

def check_img_folder_path(path, folder):
    img_folder = Path(f"{path.absolute()}/{folder}")
    if img_folder.is_dir():
        return img_folder.absolute()
    else:
        return False

def get_jpgs(img_path):
    imgs = []
    for x in img_path.glob('**/*.jpg'):
        imgs.append(x)
    return  imgs


def convert_jpg_to_png(jpg_list,new_folder_path):
    for x in jpg_list:
            img = Image.open(x)
            img.save(f'{new_folder_path}/{x.stem}.png','png')
    return

if __name__ ==  "__main__":
    path = Path()

    img_folder = sys.argv[1]
    new_folder = sys.argv[2]
    
    img_path   = check_img_folder_path(path,img_folder)
    if img_path:
        new_folder_path = check_new_folder_path(path,new_folder)

        jpg_list   = get_jpgs(img_path)
        if jpg_list:
            convert_jpg_to_png(jpg_list,new_folder_path)
        else:
            print('No .jpgs images in source folder, please try again')
    else:
        print('Source folder does not exist, please try again')

    