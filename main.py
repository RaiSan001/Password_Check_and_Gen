import tkinter as tk
import random

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
message_label = tk.Label(center_frame, text= "", font=("Times New Roman", 14), bg="Black", fg="Green")
message_label.pack()

#creating the Check Strength button
#logic
def check_strength():
    password = password_enter.get()

    if len(password) < 8:
        message_label.configure(text= "Enter at least 8 characters", fg= "Red")
        return

    #character checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit()for c in password)
    has_special = any(c in ".!@#$%^&*()" for c in password)

    #calculating strength
    score = sum([has_special, has_digit, has_lower, has_upper])

    #determining rating
    if score == 1:
        rating = "Bad"
    elif score == 2:
        rating = "Weak"
    elif score == 3:
        rating = "Good"
    elif score == 4:
        rating = "Strong"
    else:
        rating = "Invalid Password"

    message_label.configure(text= rating, fg="Green" if score > 1 else "Red")



#button
check = tk.Button(
    center_frame,
    text = "Check Strength",
    command = check_strength, #calling check strength function
    bg="Black",
    fg="Green",
    font=("Times New Roman", 10)
)
check.pack(pady=10)

#creating the Password Generator
#logic
def generate_password():
    #types of chars
    lower = "qwertyuiopasdfghjklzxcvbnm"
    upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
    digit = "1234567890"
    special = "!@#$%^&*()"

    #ensuring every at least one character of each type in password
    password = [random.choice(lower), random.choice(upper), random.choice(digit), random.choice(special)]

    #remaining fully randomized
    chars = lower + upper + digit + special
    password += [random.choice(chars) for _ in range(8)]

    #shuffeling the characters
    random.shuffle(password)
    password = "".join(password)

    #UI
    password_enter.delete(0, tk.END)
    password_enter.insert(0, password)
    check_strength() #auto checks the strength

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