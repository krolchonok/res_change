from __future__ import print_function
import sys
from tkinter import *


class ScreenRes(object):
    @classmethod
    def set(cls, width=None, height=None, freqs=60, depth=32):
        if width and height:
            print(
                "Setting resolution to {}x{} {}hz".format(width, height, freqs, depth)
            )
        else:
            print("Setting resolution to defaults")

        if sys.platform == "win32":
            cls._win32_set(width, height, freqs, depth)


def fullscreen():
    ScreenRes.set(2560, 1440, 165)


def gamescreen():
    ScreenRes.set(1920, 1440, 165)


# gamescreen()
# fullscreen()

main = Tk()

w = main.winfo_screenwidth()
h = main.winfo_screenheight()

main.geometry(f"150x60+{int(w-250)}+{int(h/2-120)}")
main.resizable(False, False)
main.title("")
btn = Button(
    main,
    width=15,
    height=1,
    text="Полный экран",
    bg="white",
    fg="black",
    command=fullscreen,
)
btn2 = Button(
    main,
    width=15,
    height=1,
    text="Игровой экран",
    bg="white",
    fg="black",
    command=gamescreen,
)

btn.pack(pady=2)
btn2.pack()
main.attributes("-topmost", True)
# main.attributes('-toolwindow', True)
main.mainloop()
