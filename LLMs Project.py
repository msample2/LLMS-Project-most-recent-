import tkinter as tk
from PIL import ImageTk, Image

def show_model_menu():
    print("Model Menu")

window = tk.Tk()
window.title("Audi: Past to Present")
menubar = tk.Menu(window)

#Function to switch to the About page
def switch_to_about():
    about_window = tk.Toplevel(window)
    about_window.title("About")
    header = tk.Label(about_window, text="About", font=("Montserrat", 24))
    header.pack()

#Function to switch to the Model Menu page
def switch_to_model_menu():
    model_menu_window = tk.Toplevel(window)
    model_menu_window.title("Model Menu")
    header = tk.Label(model_menu_window, text="Model Menu", font=("Montserrat", 24))
    header.pack()

    #a3_image = Image.open("audi_a3.png")
    #resized_audia3_image = a3_image.resize((a3_image.width // 10, a3_image.height // 10))
    #a3_image = ImageTk.PhotoImage(resized_audia3_image)
    #audi_a3_label = tk.Label(image=a3_image)
    #audi_a3_label.pack()

#Menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Main Menu", menu=file_menu)
file_menu.add_command(label="About", command=switch_to_about)
file_menu.add_command(label="Model Menu", command=switch_to_model_menu)

#Labels
header = tk.Label(window, text="Audi: Past to Present", font=("Montserrat", 24))
header.pack()

#Buttons
about_button = tk.Button(window, text='About', command=switch_to_about)
about_button.pack()

model_menu_button = tk.Button(window, text='Model Menu', command=switch_to_model_menu)
model_menu_button.pack()

#Images
#Main Page
audi_image = Image.open("audi_logo.png")
resized_audi_image = audi_image.resize((audi_image.width // 10, audi_image.height // 10))
audi_logo = ImageTk.PhotoImage(resized_audi_image)
audi_logo_label = tk.Label(image=audi_logo)
audi_logo_label.pack()

window.config(menu=menubar)
window.mainloop()
