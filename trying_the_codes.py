import tkinter as tk

class CenteredShadowFrameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Centered Shadow Frame")
        self.root.geometry("400x300")

        # Create the main frame
        main_frame = tk.Frame(self.root, bg="lightblue", width=200, height=100)
        main_frame.pack(pady=20)

        # Create a shadow frame
        shadow_frame = tk.Frame(self.root, bg="gray", bd=2, relief=tk.SUNKEN)
        shadow_frame.place(relx=main_frame.winfo_x() + 0.02, rely=main_frame.winfo_y() + 0.02, relwidth=main_frame.winfo_reqwidth(), relheight=main_frame.winfo_reqheight())

        # Create other widgets inside the main frame
        label = tk.Label(main_frame, text="Hello, Centered Shadow World!", font=("Arial", 14))
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CenteredShadowFrameApp(root)
    root.mainloop()
    
    
    frame_inquiry = Frame(self.root, bg = "#F0F8FF", highlightbackground = "#DCDCDC", highlightcolor = "#DCDCDC", highlightthickness = 3, bd = 0)
        frame_inquiry.pack(padx = 20, pady = 20)
        frame_inquiry.place(x = 330, y = 150, width = 500, height = 400)