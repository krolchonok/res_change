from __future__ import print_function
import sys
from tkinter import *

class ScreenRes(object):
    @classmethod
    def set(cls, width=None, height=None, freqs=60, depth=32):
        if width and height:
            print('Setting resolution to {}x{} {}hz'.format(width, height, freqs, depth))
        else:
            print('Setting resolution to defaults')

        if sys.platform == 'win32':
            cls._win32_set(width, height, freqs, depth)

    @staticmethod
    def _win32_set(width=None, height=None, freqs=60, depth=32):
        import win32api
        from pywintypes import DEVMODEType
        if width and height and freqs:

            if not depth:
                depth = 32
            if not freqs:
                freqs = 60

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth = width
            mode.PelsHeight = height
            mode.BitsPerPel = depth
            mode.DisplayFrequency = freqs

            win32api.ChangeDisplaySettings(mode, 0)
        else:
            win32api.ChangeDisplaySettings(None, 0)

def fullscreen():
    ScreenRes.set(1920, 1080, 165)
    
def gamescreen():
    ScreenRes.set(1440, 1080, 165)

# gamescreen()
# fullscreen()

main = Tk()

w = main.winfo_screenwidth()
h = main.winfo_screenheight()

main.geometry(f'150x60+{int(w-250)}+{int(h/2-120)}')
main.resizable(False, False)
main.title("")
btn = Button(main, width=15,
             height=1, text="Полный экран",
             bg="white", fg="black",
             command=fullscreen)
btn2 = Button(main, width=15,
             height=1, text="Игровой экран",
             bg="white", fg="black",
             command=gamescreen)

btn.pack(pady=2)
btn2.pack()
main.attributes('-topmost', True)
# main.attributes('-toolwindow', True)
main.mainloop()

