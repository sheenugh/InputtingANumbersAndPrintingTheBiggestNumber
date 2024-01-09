#Delima, Sheena Mae D.
#BSCPE 1-5



#---------------------------------------------
# ========== IMPORTS ==========
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import pygame
import os

# ========== MUST PROGRAM FIRST THE "FUNCTIONS" =========
# - BG music
def play_background_music(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)  
        
music_file_path = 'math_song.mp3'
play_background_music(music_file_path)
pygame.time.delay(10)  


# ========== ACTUAL CODES =========
# --- Pseudocode ---
# - Tkinter codes window
class Finding_the_Greatest_Number:
        def __init__(self, root):
                self.root = root
                self.root.title = ("Inputting_Random_Numbers_and_Determine_the_Biggest_Number")
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
                subheadings_instructions = Label(frame_inquiry, text = "Input a unique number in each box.", font = ("Georgia", 12), fg = "black", bg = "#F0F8FF").place(x = 90, y = 80)
        
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
                submit_button = Button(frame_inquiry, cursor = "hand2", text = "Submit", font = ("Goudy old sty", 15), fg = "white", bg = "#6162FF", bd = 0, command=self.inputting_numbers).place(x = 90, y = 340, width = 100, height = 40)

# - Find and print the biggest number
        # def and if,else,elif function
        def inputting_numbers(self):
                try:
                        first_number = int(self.user_inputting_the_first_number.get())
                        second_number = int(self.user_inputting_the_second_number.get())
                        third_number = int(self.user_inputting_the_third_number.get())      
                except ValueError:
                        messagebox.showerror("Error", "Invalid input. Please enter valid integers.")
                else:
                        messagebox.showinfo("Yahoo!", f"You have entered {first_number}, {second_number}, {third_number} \n Do you want to know the biggest number you have entered? \n Click 'OK' if Yes. Click the 'Exit Tab' if No.")
        
                # Compare the values
                if first_number > second_number and first_number > third_number:
                        messagebox.showinfo("Result", f"The biggest number is: {first_number}")
                elif second_number > first_number and second_number > third_number:
                        messagebox.showinfo("Result", f"The biggest number is: {second_number}")
                elif third_number > first_number and third_number > second_number:
                        messagebox.showinfo("Result", f"The biggest number is: {third_number}")
                else:
                        messagebox.showinfo("Result", "All/Some numbers are equal.")

root = Tk()
root.title("Finding the Greatest Number Among the 3 Inputted Numbers")
obj = Finding_the_Greatest_Number(root)
root.mainloop()

