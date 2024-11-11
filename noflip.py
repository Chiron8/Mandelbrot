from PIL import Image
import time

start = time.time()

resolution = 3000
passes = 100
col = ()

image = Image.new('RGB', (resolution, resolution), 'white')

def calculate(a, b):
    global col
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    c = complex(a, b)
    z = 0
    for i in range(passes):
        z = z ** 100 + c
        if abs(z) > 2:
            col = (round(i*2.55), round(i*2.55), round(i*2.55), 255)
            return False
    return True

for y in range(resolution):
    print(y/resolution*100, "%")
    for x in range(resolution):
        colour = calculate(x, y)
        if colour:
            image.putpixel((x, y), (0, 0, 0, 255))
        else:
            image.putpixel((x, y), col)

end = time.time()

print(end-start)

image.show()
