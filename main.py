from wand.image import Image
from wand.color import Color
import os
import sys

def get_filename(filepath):
    """
    Returns the filename without extension and path
    """
    filename = os.path.basename(filepath)
    filename_without_extension = os.path.splitext(filename)[0]
    return filename_without_extension

input_file = sys.argv[1]

if not os.path.exists(input_file):
    print('File does not exist')
    exit(1)

intermediate_folder = 'intermediate'
print('Starting conversion')
print('Creating intermediate folder')
if not os.path.exists(intermediate_folder):
    os.mkdir(intermediate_folder)

# First pass: Remove background from pdf and convert to png
# White background may still exists behind text
# Ref: https://stackoverflow.com/q/27826854/13617136
with Image(filename=input_file, resolution=300) as img:
    img.alpha_channel = True
    print('Saving intermediate image(s)')
    img.save(filename=f'{intermediate_folder}/page.png')

# To completely remove white background behind text, run a second pass
# If you're converting from png, you can skip the first pass

# Load image from first pass
files = os.listdir(intermediate_folder)
images = [os.path.join(intermediate_folder, file) for file in files]

print(f'{len(images)} images loaded')
print('Creating output folder')
if not os.path.exists('output'):
    os.mkdir('output')

for image in images:
    print('Processing image', get_filename(image))
    # Ref: https://stackoverflow.com/a/32740702/13617136
    with Image(filename=image, resolution=300) as img:
        with Color('#ffffff') as white:
            twenty_percent = int(65535 * 0.2)  # Note: percent must be calculated from Quantum
            img.transparent_color(white, alpha=0.0, fuzz=twenty_percent)
        img.save(filename=f'output/{get_filename(image)}.png')  

print('Conversion complete')  

# clear intermediate folder
print('Removing intermediate folder')
for image in images:
    os.remove(image)
os.rmdir(intermediate_folder)
