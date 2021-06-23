from datetime import datetime
import tkinter as tk
from time import time


def main() -> None:
    display = tk.Tk()
    display.geometry('215x62')
    display.title('Clock')

    lbl = tk.Label(
        display,
        background='black',
        font=('Helvetica', 37),
        foreground='red',
    )
    lbl.place(x=0, y=0)

    def tick() -> None:
        now = datetime.now()
        lbl.config(text=now.strftime('%I:%M %p'))

        until_next = round(
            1000 * (60 - time()%60)
        )
        display.after(ms=until_next, func=tick)

    tick()
    display.mainloop()


if __name__ == '__main__':
    main()
