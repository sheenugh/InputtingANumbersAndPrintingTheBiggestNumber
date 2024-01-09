import tkinter as tk
from tkinter import ttk
import time

class WelcomeLoadingScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome Loading Screen")
        self.root.geometry("600x400")

        # Set the background image
        self.background_image = tk.PhotoImage(file="math_image1 - Copy.png")  # Replace with the actual image file path
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, text="Welcome to Your App!", font=("Helvetica", 18), bg='white')
        self.label.pack(pady=20)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate', variable=self.progress_var)
        self.progress_bar.pack(pady=10)

        self.start_loading_process()

    def start_loading_process(self):
        self.progress_var.set(0)
        self.root.update_idletasks()

        for i in range(101):
            time.sleep(0.03)
            self.progress_var.set(i)
            self.root.update_idletasks()

        self.root.destroy()
        self.show_main_app_window()

    def show_main_app_window(self):
        main_app_window = tk.Tk()
        main_app_window.title("Main Application Window")
        main_app_window.geometry("800x600")

        # Add your main application widgets and functionality here

        main_app_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    welcome_loading_screen = WelcomeLoadingScreen(root)
    root.mainloop()