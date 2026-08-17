from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (800, 200), color=(255, 255, 255))
d = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 24)
except:
    font = ImageFont.load_default()

text = "Invalid text! Please try again!"

d.text((50, 80), text, fill=(0, 0, 0), font=font)
img.save('7c_error_handling_interface.png')
