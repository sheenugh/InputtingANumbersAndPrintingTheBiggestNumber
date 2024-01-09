from tkinter import Tk, Entry, Button, messagebox

class InputANumber:
    def __init__(self, root):
        self.root = root
        self.root.title("Input Numbers")

        frame_inquiry = Frame(self.root, bg="white")
        frame_inquiry.pack()

        self.user_inputting_the_first_number = Entry(frame_inquiry, font=("Goudy old style", 12), bg="#F0F8FF", highlightbackground="#C1CDCD", highlightcolor="#838B8B", highlightthickness=3, bd=0)
        self.user_inputting_the_first_number.pack()

        self.user_inputting_the_second_number = Entry(frame_inquiry, font=("Goudy old style", 12), bg="#F0F8FF", highlightbackground="#C1CDCD", highlightcolor="#838B8B", highlightthickness=3, bd=0)
        self.user_inputting_the_second_number.pack()

        self.user_inputting_the_third_number = Entry(frame_inquiry, font=("Goudy old style", 12), bg="#F0F8FF", highlightbackground="#C1CDCD", highlightcolor="#838B8B", highlightthickness=3, bd=0)
        self.user_inputting_the_third_number.pack()

        submit_button = Button(frame_inquiry, text="Submit", command=self.check_function)
        submit_button.pack()

    def check_function(self):
        try:
            first_number = int(self.user_inputting_the_first_number.get())
            second_number = int(self.user_inputting_the_second_number.get())
            third_number = int(self.user_inputting_the_third_number.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid integers.")
        else:
            if first_number != 1 or second_number != 1 or third_number != 1:
                messagebox.showerror("Error", "Invalid input. Numbers should be equal to 1.")
            else:
                messagebox.showinfo("Welcome", f"You have entered {first_number}, {second_number}, {third_number}")

if __name__ == "__main__":
    root = Tk()
    app = InputANumber(root)
    root.mainloop()