import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image,ImageTk
import winsound
import keyboard

ISRUN=False

time.sleep(3)

dir = os.path.dirname(os.path.abspath(sys.argv[0]))

pyautogui.hotkey("win", "d")

time.sleep(0.7)

im = pyautogui.screenshot('desktop.png')

w = tk.Tk()
w.geometry("{}x{}+0+0".format(w.winfo_screenwidth(), w.winfo_screenheight()))

bg=tk.PhotoImage(file='desktop.png')
bgl=tk.Label(w, image=bg, width=w.winfo_screenwidth(), height=w.winfo_screenheight(), borderwidth=0)
bgl.place(x=0, y=0)

def updateImg(number, sleepNum):
    imgName=dir+"/BSOD/bsod"+str(number)+".png"
    img=Image.open(imgName).resize(
        (w.winfo_screenwidth(), w.winfo_screenheight()), Image.LANCZOS)
    bg1= ImageTk.PhotoImage(img)
    bgl.configure(image=bg1, cursor='none')
    w.update()
    time.sleep(sleepNum)

def toggle_geom():
    pass

def initiate(e):
    global ISRUN
    if ISRUN==False:
        ISRUN=True
        time.sleep(1)
        updateImg(1, 3)
        updateImg(2, 2)
        updateImg(3, 4)
        updateImg(4, 0.2)
        winsound.PlaySound(dir+"/noise1.wav", winsound.SND_ASYNC)
        updateImg(3, 2)
        winsound.PlaySound(dir+"/noise2.wav", winsound.SND_ASYNC)
        updateImg(6, 0.2)
        updateImg(3, 1.5)
        winsound.PlaySound(dir + "/noise3.wav", winsound.SND_ASYNC)
        updateImg(4, 0.1)
        updateImg(3, 0.75)
        winsound.PlaySound(dir + "/final.wav", winsound.SND_ASYNC)
        updateImg(5,1)
        winsound.PlaySound(dir + "/loop.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

bgl.bind('<Button-1>', initiate)
w.attributes("-fullscreen", True)
w.attributes('-topmost', True)
w.protocol("WM_DELETE_WINDOW", toggle_geom)

keyboard.block_key('win')

w.update()

w.mainloop()