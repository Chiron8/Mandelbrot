from PIL import Image
import time

start = time.time()

resolution = 3000 # image resolutionxresolution
passes = 200
col = ()

image = Image.new('RGB', (resolution, resolution), 'white')

print("generating...")

def calculate(a, b):
    global col
    a = a / ((resolution-1)/4) - 2
    b = b / ((resolution-1)/4) - 2
    c = complex(a, b)
    z = 0
    for i in range(passes):
        z = z ** 2 + c
        if abs(z) > 2:
            col = (round(i/2), round(i/2), round(i*2.55), 255)
            return False
    return True

if resolution % 2 == 0:
    resolutionY = (resolution - 1) / 2 + 1
else:
    resolutionY = resolution / 2 + 1

for y in range(int(resolutionY)+1):
    print(y/resolution*200, "%")
    for x in range(resolution):
        colour = calculate(x, y)
        if colour:
            image.putpixel((x, y), (0, 0, 0, 255))
        else:
            image.putpixel((x, y), col)

print("mirroring...")

im = image.load()

for y in range(int(resolutionY)):
    print(y/resolution*200, "%")
    for x in range(resolution):
        image.putpixel((x, y + round(resolution/2)), im[x, round(resolution/2) - y])

end = time.time()

print(end-start)
print(round(resolution/2))

image.show()
img = image.save("outputNew.jpg")
