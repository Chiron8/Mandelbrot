from PIL import Image
import time
start = time.time()
#img = Image.effect_mandelbrot((50000, 50000), (0.33, 0.35, 0.38, 0.4), 200)
img = Image.effect_mandelbrot((50000, 50000), (-2, -2, 2, 2), 200)
img = img.save("output1.jpg")
end = time.time()
print(end-start)