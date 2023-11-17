from tkinter import Tk, Label

class App:
    def __init__(self):
        self.tk = Tk()

        self.tk.grid_rowconfigure(0, weight=1)
        self.tk.grid_columnconfigure(0, weight=1)

        self.width = 1080
        self.height = 2076

        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()

        if self.height != self.screen_height:  # not mobile
            self.width //= 2
            self.height //= 2

        self.tk.geometry(f'{self.width}x{self.height}+0+0')

        label = Label(master=self.tk, text=f"{self.width} x {self.height}")
        label.grid(row=0, column=0, sticky="nswe")


if __name__ == "__main__":
    app = App()

    app.tk.mainloop()