#Delima, Sheena Mae D.
#BSCPE 1-5

#---------------------------------------------


# ========== IMPORTS ==========
from tkinter import *



# ========== FUNCTIONS ==========

# ========== ACTUAL CODES =========

# --- Pseudocode ---_
# - Tkinter codes window
class Input_A_Number:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Inputting_Random_Numbers")
        self.root.geometry("1199x600+100+50")
        
root = Tk()
obj = Input_A_Number(root)
root.mainloop()



# - Ask user to input 3 numbers
# - Find and print the biggest number
