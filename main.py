from tkinter import Tk, Label

if __name__ == "__main__":
    tk = Tk()

    tk.grid_rowconfigure(0, weight=1)
    tk.grid_columnconfigure(0, weight=1)

    width = 1080
    height = 2076

    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()

    if height != screen_height:  # not mobile
        width //= 2
        height //= 2


    tk.geometry(f'{width}x{height}+0+0')

    label = Label(master=tk, text=f"{width} x {height}")
    label.grid(row=0, column=0, sticky="nswe")

    tk.mainloop()