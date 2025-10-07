import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk  # Import Pillow for image support

# Functionality (Optional Dummy Functions)
def check_balance():
    result_label.config(text="Your Balance: $10,000")

def transfer_money():
    result_label.config(text="Money Transfer Successful!")

def deposit_money():
    result_label.config(text="Deposit Successful!")

# Create the main window
root = tk.Tk()
root.title("Dummy Banking Page")
root.geometry("800x500")  # Window size
root.resizable(0,0)

# Load the background image using Pillow
image = Image.open("bagg.jpg")  # Make sure 'bag.jpg' exists in the same directory
image = image.resize((800, 500))  # Resize image to fit the window
background_image = ImageTk.PhotoImage(image)

# Create Canvas for background
canvas = Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Adding Transparent Labels and Buttons
canvas.create_text(170, 50, text="Welcome to Your Bank", font=("Helvetica", 24, "bold"), fill="white")

# Buttons to simulate banking actions
check_balance_btn = tk.Button(root, text="Check Balance", font=("Arial", 12), command=check_balance)
transfer_money_btn = tk.Button(root, text="Transfer Money", font=("Arial", 12), command=transfer_money)
deposit_money_btn = tk.Button(root, text="Deposit Money", font=("Arial", 12), command=deposit_money)

# Place buttons on the Canvas
canvas.create_window(200, 150, window=check_balance_btn)
canvas.create_window(200, 220, window=transfer_money_btn)
canvas.create_window(200, 290, window=deposit_money_btn)

# Result Label (Displays messages for actions)
result_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="black")
canvas.create_window(200, 350, window=result_label)

# Run the Tkinter main loop
root.mainloop()
