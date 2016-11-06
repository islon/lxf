import Image


im = Image.open('I:\\python\\pic\\pi2.jpg')

w, h = im.size

im.thumbnail((w//2, h//2))

im.save('I:\\python\\pic\\pi3.jpg', 'jpeg')