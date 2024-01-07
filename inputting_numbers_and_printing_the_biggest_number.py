#Delima, Sheena Mae D.
#BSCPE 1-5

#---------------------------------------------


# ========== IMPORTS ==========
from tkinter import *
from PIL import ImageTk



# ========== FUNCTIONS ==========

# ========== ACTUAL CODES =========

# --- Pseudocode ---_
# - Tkinter codes window
class Input_A_Number:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Inputting_Random_Numbers")
        self.root.geometry("1199x600+100+50")
        
        #Background image of the window
        self.bg = PhotoImage(file="bg_for_window.png")
        self.bg_image = Label(self.root, image = self.bg).place(x = 0, y = 0, relwidth= 1, relheight = 1) 
        
root = Tk()
obj = Input_A_Number(root)
root.mainloop()



# - Ask user to input 3 numbers
# - Find and print the biggest number
