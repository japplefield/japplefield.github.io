import sys
import csv
import os

image_template = '''<div class="blog-image">
    <img src="/img/PATH" alt="CAPTION" />
</div>'''

paragraph_template = '''<div class="blog-paragraph">
    CONTENT 
</div>'''

def main(name, csv_dir, img_dir):
    infile = f"{csv_dir}/{name}.csv"
    images = list(filter(lambda x: name in x, os.listdir(img_dir)))
    images.sort()
    with open(infile) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['type'] == 'img':
                content = image_template.replace("PATH", images[0]).replace("CAPTION", row['content'])
                images.pop(0)
                print(content)
            elif row['type'] == 'p':
                content = paragraph_template.replace("CONTENT", row['content'])
                print(content)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])