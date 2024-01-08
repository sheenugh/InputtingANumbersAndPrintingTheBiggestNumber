#Delima, Sheena Mae D.
#BSCPE 1-5



#---------------------------------------------



# ========== IMPORTS ==========
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox



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
                frame_inquiry.place(x = 330, y = 100, width = 500, height = 420)

                
                # # Headings and subheadings inside the frame
                headings_welcoming_word = Label(frame_inquiry, text = "Welcome User!", font = ("Impact", 25, "bold"), fg = "#BF3EFF", bg = "#F0F8FF") .place(x = 90, y = 30)
                subheadings_instructions = Label(frame_inquiry, text = "From 1-10, input your desired number.", font = ("Georgia", 12), fg = "black", bg = "#F0F8FF").place(x = 90, y = 80)
                
                # User will input the 3 Numbers
                user_fist_desired_number = Label(frame_inquiry, text = "Input a number", font = ("Goudy old style", 12, "bold"), fg = "black", bg = "#F0F8FF").place(x = 90, y = 120)
                self.user_inputting_the_first_number = Entry(frame_inquiry, font = ("Goudy old style", 12), bg = "#F0F8FF", highlightbackground = "#C1CDCD", highlightcolor = "#838B8B", highlightthickness = 3, bd = 0)
                self.user_inputting_the_first_number.place(x = 90, y = 150, width = 320, height = 35) 
                user_second_desired_number = Label(frame_inquiry, text = "Input a number", font = ("Goudy old style", 12, "bold"), fg = "black", bg = "#F0F8FF").place(x = 90, y = 190)
                self.user_inputting_the_second_number = Entry(frame_inquiry, font = ("Goudy old style", 12), bg = "#F0F8FF", highlightbackground = "#C1CDCD", highlightcolor = "#838B8B", highlightthickness = 3, bd = 0)
                self.user_inputting_the_second_number.place(x = 90, y = 220, width = 320, height = 35)
                
                user_third_desired_number = Label(frame_inquiry, text = "Input a number", font = ("Goudy old style", 12, "bold"), fg = "black", bg = "#F0F8FF").place(x = 90, y = 260)
                self.user_inputting_the_third_number = Entry(frame_inquiry, font = ("Goudy old style", 12), bg = "#F0F8FF", highlightbackground = "#C1CDCD", highlightcolor = "#838B8B", highlightthickness = 3, bd = 0)
                self.user_inputting_the_third_number.place(x = 90, y = 290, width = 320, height = 35)
                
                # Button of the Submit
                submit_button = Button(frame_inquiry, text = "Submit", font = ("Goudy old sty", 15), fg = "white", bg = "#6162FF", bd = 0, command=self.check_function)
                submit_button.place(x = 90, y = 340, width = 180, height = 40)
        
        # def and if-else function
        def check_function(self):
                if self.user_inputting_the_first_number.get()=="" or  self.user_inputting_the_second_number.get()=="" or  self.user_inputting_the_third_number.get()=="":
                        messagebox.showerror("Error", "All fields are required to fill out", parent = self.root)        
                elif self.user_inputting_the_first_number.get()!="Sheena" or  self.user_inputting_the_second_number.get()!="Mae" or  self.user_inputting_the_third_number.get()!="Delima":
                        messagebox.showerror("Error", "Invalid", parent = self.root)
                else:
                        messagebox.showinfo("Welcome", f"You have entered {self.user_inputting_the_first_number.get()}")
                
root = Tk()
root.title("Transparent Window")
obj = Input_A_Number(root)
root.mainloop()




# - Find and print the biggest number
''