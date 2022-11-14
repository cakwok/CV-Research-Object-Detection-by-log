from PIL import Image
import os

src_folder = "/Users/casca/Library/Mobile Documents/com~apple~CloudDocs/Northeastern Courses/CV Fish Research/FISH"
dst_folder = "/Users/casca/Library/Mobile Documents/com~apple~CloudDocs/Northeastern Courses/CV Fish Research/FISH_resized/"

w = 600
h = 400

for i in os.listdir(src_folder):
    file = f"{src_folder}/{i}"
    if ".JPG" in file:
       im = Image.open(file)
       im = im.resize((w, h), Image.ANTIALIAS)
       dst_path = dst_folder + file.split("/")[-1].strip(".JPG") + "_resized.jpg"
       print(dst_path)
       im.save(dst_path)
