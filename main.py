from PIL import Image
import math
import time as t
import pyautogui as pygui

characters = ["##", "@@", "%%", "&&", "$$", "==", "!!", "**", "++", "~~", "--", "^^", "˜˜"]


while True:
    art = ""
    t0 = t.time()
    pygui.screenshot("img.png")

    img = Image.open('img.png')
    img = img.convert("L")
    width, height = img.size

    if width > 500:
        new_width = 500
        new_height = int(height * (500/width))
        img = img.resize((new_width, new_height))
        img.save('img.png')
        #print("Downscaled+Grayscaled successfully!")


    for y in range(img.size[1]):
        for x in range(img.size[0]):
            brightness = img.getpixel((x, y))/255*12
            #print(f"Pixel at ({x}, {y}) is {brightness} light.")

            char = characters[round(brightness)]

            art += str(char)
        art += "\n"

    with open("art.txt", "w") as f:
        f.write(art)
    f.close()

    t1 = t.time()

    time = t1-t0

    print(f"Only took {time}s, amazing ✨, that'd be {1/time}FPS :D")
    print(art)

    #t.sleep(0.3)