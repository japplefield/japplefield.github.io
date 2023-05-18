import sys
import csv
import os

def main(name, img_dir):
    count = 0
    images = list(filter(lambda x: x.lower().endswith(('jpeg', 'jpg', 'png', 'gif')), os.listdir(img_dir)))
    images.sort()
    for file in images:
        ext = file.split('.')[-1]
        os.rename(f"{img_dir}/{file}", f"{img_dir}/{name}-{str(count).zfill(2)}.{ext}")
        count += 1
    

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])