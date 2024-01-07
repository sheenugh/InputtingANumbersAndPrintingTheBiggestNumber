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
        frame_inquiry = Frame(self.root)
        frame_inquiry.bg = ImageTk.PhotoImage(file = "math_image1.jpg")
        frame_inquiry.bg_image = Label(self.root, image = frame_inquiry.bg).place(x = 330, y = 150, width = 500, height = 400) 
        
        # Welcoming words for the user
        
root = Tk()
root.title("Transparent Window")
obj = Input_A_Number(root)
root.mainloop()




# - Find and print the biggest number
