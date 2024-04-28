from PIL import Image
import time

def change_pixel_color(pixel, generated_number):
    r, g, b = pixel
    new_r = (r + generated_number) %252
    new_g = (g + generated_number) %336
    new_b = (b + generated_number) %504
    return new_r, new_g, new_b

original_image_path = "C:\\Users\\sserg\\Downloads\\SERGEI ASS 2\\Chapter1.jpg"
original_image = Image.open(original_image_path)

current_time = int(time.time())
generated_number =(current_time % 100) + 50
if generated_number %2 == 0:
    generated_number += 10

new_image = Image.new('RGB', original_image.size)

for y in range(original_image.height):
    for x in range(original_image.width):
        pixel = original_image.getpixel((x, y))
        new_pixel = change_pixel_color(pixel, generated_number)
        new_image.putpixel((x, y), new_pixel)

new_image.show()
new_image.save("Chapter1_edited.jpg")