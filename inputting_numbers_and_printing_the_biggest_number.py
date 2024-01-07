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
        frame_inquiry = Frame(self.root, bg = "#F0F8FF", highlightbackground ="#DCDCDC" , highlightcolor = "#DCDCDC", highlightthickness = 3, bd = 0)
        frame_inquiry.pack(padx = 20, pady = 20)
        frame_inquiry.place(x = 330, y = 150, width = 500, height = 400)
        
        
        # Headings and subheadings inside the frame
        headings_welcoming_word = Label(frame_inquiry, text = "Welcome User!", font = ("Impact", 35, "bold"), fg = "#BF3EFF", bg = "#F0F8FF", justify = "center").place(x = 90, y = 30)
        subheadings_instructions = Label(frame_inquiry, text = "From 1-10, input your desired number.", font = ("Goudy old style", 12, "bold"), fg = "black", bg = "#F0F8FF").place(x = 90, y = 100)
        
        # Input a Number
        user_fist_desired_number = Label(frame_inquiry, text = "Please input a number", font = ("Goudy old style", 12, "bold"), fg = "grey", bg = "#F0F8FF").place(x = 90, y = 140)
        
        
root = Tk()
root.title("Transparent Window")
obj = Input_A_Number(root)
root.mainloop()




# - Find and print the biggest number
''