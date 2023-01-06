from turtle import heading, width
import pyautogui
import keyboard

while keyboard.is_pressed('c')== False:
   # pyautogui.displayMousePosition()

    sc = pyautogui.screenshot(region=( 817, 365, 63, 32))
    width,height = sc.size

    sc.save('Exemplo.png')
    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = sc.getpixel((x,y))
            print(r,g,b)

            if r == 30 and g == 30 and b == 30:
                pyautogui.click(817+x, 365+y)