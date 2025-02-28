import tkinter as tk

#creating the main window
root = tk.Tk()
root.title("Password Checker")
root.geometry("400x350") #width x height
root.configure(bg="Black")

#centering the main thing
center_frame = tk.Frame(root, bg = "Black")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

#creating the text box
password_enter = tk.Entry(center_frame, width=30, font = ("Times New Roman", 14), bg="Black", fg="Green", insertbackground="Green") #single line text box
password_enter.pack(pady=20) #vertical spacing

#message label
message_label = tk.Label(center_frame, text="", font=("Times New Roman", 14), bg="Black", fg="Green")

#creating the Check Strength button
#logic
def check_strength():
    #to be added later
    pass

#button
check = tk.Button(
    center_frame,
    text = "Check Strength",
    command=check_strength, #calling check strength function
    bg="Black",
    fg="Green",
    font=("Times New Roman", 10)
)
check.pack(pady=10)

#creating the Password Generator
#logic
def generate_password():
    #to be added later
    password_enter.delete(0, tk.END)
    password_enter.insert(0, "1234abcd")

#button
generate = tk.Button(
    center_frame,
    text="Generate Strong Password",
    command=generate_password,
    bg="Black",
    fg="Green",
    font=("Times New Roman", 10)
)
generate.pack(pady=10)

#running
root.mainloop()