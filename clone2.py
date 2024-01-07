#Delima, Sheena Mae D.
#BSCPE 1-5



#---------------------------------------------



# ========== IMPORTS ==========
from tkinter import *
from PIL import ImageTk



# ========== FUNCTIONS ==========




# ========== ACTUAL CODES =========
# --- Pseudocode ---
# - Tkinter codes window
class Input_A_Number:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Inputting_Random_Numbers")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)
        
        # Background image of the window
        self.bg = ImageTk.PhotoImage(file="bg_for_window.jpg")
        self.bg_image = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth= 1, relheight = 1) 

# - Ask user to input 3 numbers
        # A frame that the user will input a number 
        frame_inquiry = Frame(self.root, bg = "#F0F8FF")
        frame_inquiry.place(x = 330, y = 150, width = 500, height = 400)
        
        shadow_frame = Frame(self.root, bd=2, relief=SUNKEN)
        shadow_frame.place(relx=frame_inquiry.winfo_x() + 0.02, rely=frame_inquiry.winfo_y() + 0.02, relwidth=frame_inquiry.winfo_reqwidth(), relheight=frame_inquiry.winfo_reqheight())

        
        # Welcoming words for the user
        welcoming_words_headings = Label(frame_inquiry, text = "Welcome User!", font = ("Impact", 35, "bold"), fg = "#BF3EFF", bg = "#F0F8FF", justify = "center").place(x = 90, y = 30)
        instruction_subtitle = Label(frame_inquiry, text = "From the numbers 1-10, please input your desired number.", font = ("Goudy old style", 10, "bold"), fg = "#1d1d1d", bg = "#F0F8FF").place(x = 90, y = 100)
        
root = Tk()
root.title("Transparent Window")
obj = Input_A_Number(root)
root.mainloop()




# - Find and print the biggest number
''