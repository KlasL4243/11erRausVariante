from tkinter import Tk, Label

if __name__ == "__main__":
    tk = Tk()

    tk.grid_rowconfigure(0, weight=1)
    tk.grid_columnconfigure(0, weight=1)

    width = tk.winfo_screenwidth()
    height = tk.winfo_height()

    label = Label(master=tk, text=f"{width}, {height}")
    label.grid(row=0, column=0, sticky="nswe")

    tk.mainloop()