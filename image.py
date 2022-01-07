from PIL import Image, ImageFilter

img = Image.open(r".\astro.jpg")
img.thumbnail((400,400))

img.show()