from tkinter import Tk, Label

if __name__ == "__main__":
    tk = Tk()

    tk.grid_rowconfigure(0, weight=1)
    tk.grid_columnconfigure(0, weight=1)

    screen_width = tk.winfo_screenwidth()
    screen_height = tk.winfo_screenheight()

    tk.geometry(f'{screen_width}x{screen_height}')

    label = Label(master=tk, text=f"{screen_width} x {screen_height}")
    label.grid(row=0, column=0, sticky="nswe")

    tk.mainloop()